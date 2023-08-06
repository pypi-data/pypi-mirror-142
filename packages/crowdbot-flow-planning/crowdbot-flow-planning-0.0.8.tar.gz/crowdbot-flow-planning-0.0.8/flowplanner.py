import numpy as np
from matplotlib import pyplot as plt
from CMap2D import CMap2D
from CMap2D import gridshow

from rvo import NavigationPlanner, RVONavigationPlanner
from flowplanningtools import crowdflow_dijkstra, calculate_crowd_velocity, fast_discrete_model

class DiscreteFlowModel(object):
    def __init__(self):
        self.observations = []
        self.static_obstacles_map = None
        # constant parameters
        self.mu = 5. # the viscosity constant. higher -> less feasible to oppose crowd
        self.gamma = 1.  # error-importance parameter for distant observations
        self.sigma = 1. # density smoothing parameter

    def get_latest_observation_time(self):
        if not self.observations:
            return None
        return self.observations[-1][0]

    def get_latest_observation(self):
        if not self.observations:
            return None
        return self.observations[-1][1]

    def get_observation_sample(self, sample_size=2000, time_horizon=np.inf, weight_decay=None):
        # some models need to know not only what was observed, but what wasn't.
        # this lets one know how much the space was observed (1 = once, 2 = twice, etc)
        measurement_count_grid = np.zeros_like(self.static_obstacles_map.occupancy())
        # apply filters: exclude samples from superset
        sample_superset = []
        for obs in self.observations:
            age = self.get_latest_observation_time() - obs[0]
            if age > time_horizon:
                continue
            # add 1 for every place in the grid that this observation observed
            if obs[2] is None:
                measurement_grid = 1
            else:
                measurement_grid = obs[2] * 1.
            if weight_decay is not None:
                # draw X% samples randomly from obs, where X is weight_decay^age
                proportion = np.power(weight_decay, age)
                obs_shuffled = np.random.permutation(obs[1])
                N = int(proportion * len(obs_shuffled))
                measurement_grid *= proportion
                sample_superset.append(obs_shuffled[:N])
                measurement_count_grid += measurement_grid
                continue
            sample_superset.append(obs[1])
            measurement_count_grid += measurement_grid
        sample_superset = np.concatenate(sample_superset, axis=0)
        sample_superset = np.random.permutation(sample_superset)
        # draw N samples
        if len(sample_superset) > 0:
            proportion = np.clip(1. * sample_size / len(sample_superset), 0, 1)
            measurement_count_grid *= proportion
        return sample_superset[:sample_size], measurement_count_grid

    def update_observations(self, observation, time, measured_surface=None):
        """ adds a new observation, and sets the current time to the latest observation time
        if an observation range is provided, it is stored.
        otherwise we assume the observation is omniscient"""
        n, o = observation.shape
        # expect measured_surface to be lidar scan, convert it into a visibility grid in the static map
        if measured_surface is not None:
            robot_in_map, angles, ranges = measured_surface
            map_angles = np.array(angles) + robot_in_map[2]
            robot_in_map_ij = self.static_obstacles_map.xy_to_floatij(robot_in_map[:2][None, :])[0]
            visgrid = self.static_obstacles_map.lidar_visibility_map_ij(robot_in_map_ij,
                                                                        map_angles.astype(np.float32),
                                                                        np.array(ranges).astype(np.float32))
            measured_surface = (visgrid >= 0).astype(int)
        self.observations.append((time, observation, measured_surface))

    def update_static_obstacles_map(self, static_obstacles_map):
        self.static_obstacles_map = static_obstacles_map
        self.static_obstacles_map_cached_sdf = static_obstacles_map.as_sdf()

    def cython_get_discrete_model(self, sample=None):
        if not self.observations:
            return None
        if self.static_obstacles_map is None:
            return None
        if sample is None:
            obs_odom = self.get_latest_observation()
            measurement_grid = 1
        else:
            obs_odom, measurement_grid = sample
        static_obstacles_map = self.static_obstacles_map
        sdf = self.static_obstacles_map_cached_sdf
        xx, yy = static_obstacles_map.as_meshgrid_xy()
        # filter outliers
        outliers = np.linalg.norm(obs_odom[:, 3:5], axis=-1) > 10
        obs_odom[outliers, 3:5] = 0
        # discrete flow model
        gamma = self.gamma
        sigma = self.sigma
        xx = np.ascontiguousarray(xx).astype(np.float32)
        yy = np.ascontiguousarray(yy).astype(np.float32)
        obs_odom = obs_odom.astype(np.float32)
        vxstar, vystar, rhogrid = fast_discrete_model(xx, yy, obs_odom, sdf, gamma, sigma)
        return vxstar, vystar, rhogrid

    def get_discrete_model(self, sample=None):
        if not self.observations:
            return None
        if self.static_obstacles_map is None:
            return None
        if sample is None:
            obs_odom = self.get_latest_observation()
            measurement_grid = 1
        else:
            obs_odom, measurement_grid = sample
        static_obstacles_map = self.static_obstacles_map
        static_obstacles_map_cached_sdf = self.static_obstacles_map_cached_sdf
        xx, yy = static_obstacles_map.as_meshgrid_xy()
        # filter outliers
        outliers = np.linalg.norm(obs_odom[:, 3:5], axis=-1) > 10
        obs_odom[outliers, 3:5] = 0
        # discrete flow model
        gamma = self.gamma
        sigma = self.sigma
        # currently we care about (dvx/dy)^2 and (dvy/dx)^2,
        # not (dvx/dx)^2 and (dvy/dy)^2
        # for simplicity, we replace dx and dy with dr (absolute distance)
        delta2 = ((obs_odom[:, 0][None, None, :] - xx[:, :, None])**2 +
                  (obs_odom[:, 1][None, None, :] - yy[:, :, None])**2) # [x, y, obs]
        # tile measured velocities over all grid
        vxmeas = obs_odom[:, 3][None, None, :] # [x, y, obs]
        vymeas = obs_odom[:, 4][None, None, :] # [x, y, obs]
        # add in static obstacles by finding closest obstacle and treating it like a 0 speed observation (sdf)
        delta2 = np.concatenate((delta2, (static_obstacles_map_cached_sdf**2)[:, :, None]), axis=-1)
        vxmeas = np.concatenate((vxmeas, np.zeros_like(vxmeas[:,:,:1])), axis=-1)
        vymeas = np.concatenate((vymeas, np.zeros_like(vxmeas[:,:,:1])), axis=-1)
        # ---- vx -----
        # tile over [xx, yy, observation] - computing influence of each observation at each point
        alphax = np.exp(-gamma * delta2)
        TINY = 0.000001
        vxstar = np.sum(alphax * vxmeas, axis=-1) / (np.sum(alphax, axis=-1) + TINY)
        # ---- vy ----
        alphay = np.exp(-gamma * delta2)
        vystar = np.sum(alphay * vymeas, axis=-1) / (np.sum(alphay, axis=-1) + TINY)
        # ---- turbulence ---
        alphaabs = alphax
        vabsmeas = np.sqrt(vymeas**2 + vxmeas**2)
        vabsstar = np.sum(alphaabs * vabsmeas, axis=-1) / (np.sum(alphaabs, axis=-1) + TINY)
        turbulence = vabsstar - np.sqrt(vxstar**2 + vystar**2)
        # ---- rho ----
        # gaussian model for density (smoothing filter preserving p/m2)
        # a bivariate normal distribution smoothes the discrete signal, but has the same area
        rhogrid = np.zeros_like(vxstar)
        for person_odom in obs_odom:
            mux = person_odom[0]
            muy = person_odom[1]
            gaussian = 1. / (2. * np.pi * sigma*sigma) * np.exp(
                -1./2. * (((xx - mux) / sigma)**2 + ((yy - muy) / sigma)**2)
            )
            rhogrid += gaussian
        # if a place is observed 10 times, and we observed 10 pedestrians, its average density is 1
        if isinstance(measurement_grid, np.ndarray):
            measurement_grid[measurement_grid == 0] = np.inf
        rhogrid /= measurement_grid
        return vxstar, vystar, rhogrid, turbulence

    def get_interpolated_model(self):
        """ for comparison only, not maintained """
        if not self.observations:
            return None
        obs_odom = self.get_latest_observation()
        xx, yy = self.static_obstacles_map.as_meshgrid_xy()
        # filter outliers
        outliers = np.linalg.norm(obs_odom[:, 3:5], axis=-1) > 10
        obs_odom[outliers, 3:5] = 0
        # get model
        from scipy.interpolate import interp2d
        vx = interp2d(obs_odom[:, 0], obs_odom[:, 1], obs_odom[:, 3], kind="linear", fill_value=0)
        vy = interp2d(obs_odom[:, 0], obs_odom[:, 1], obs_odom[:, 4], kind="linear", fill_value=0)
        vabs = interp2d(obs_odom[:, 0], obs_odom[:, 1], np.sqrt(obs_odom[:, 4]**2 + obs_odom[:, 3]**2),
                        kind="linear", fill_value=0)
        vxgrid = vx(xx[:,0], yy[0,:]).T
        vygrid = vy(xx[:,0], yy[0,:]).T
        vabsgrid = vabs(xx[:,0], yy[0,:]).T
        vxgrid = np.clip(vxgrid, -3, 3)
        vygrid = np.clip(vygrid, -3, 3)
        vabsgrid = np.clip(vabsgrid, -3, 3)
        turbgrid = vabsgrid - np.sqrt(vxgrid**2 + vygrid**2)
        _, _, rhogrid, _ = self.get_discrete_model()
        return vxgrid, vygrid, rhogrid, turbgrid


class FlowBasedPlanner(NavigationPlanner):
    def __init__(self, version=9):
        # variables
        self.sim = None
        self.previous_crowd = None
        self.flow_model = DiscreteFlowModel()
        self.controller = RVONavigationPlanner()
        # constants
        self.version = version
        self.nudge_max_speed = 0.1
        # RVO controller params
        if self.version in [2, 6, 8, 9, 11]:
            self.controller.safety_distance = 0.01
            self.controller.neighbor_dist = 3.
            self.controller.max_neighbors = 10
            self.controller.time_horizon = 1.5
            self.controller.time_horizon_obst = 3.

    def set_static_obstacles(self, static_obstacles, portals, refmap=None):
        self.human_static_obstacles = static_obstacles
        self.robot_static_obstacles = static_obstacles + portals
        if refmap is None: # create new grid and origin from obstacles
            refmap = CMap2D()
            refmap.from_closed_obst_vertices(self.robot_static_obstacles, resolution=0.5, pad_ij=0)
            self.robot_static_obstacles_map = refmap
        else: # keep the refmap grid and origin, add only desired obstacles
            self.robot_static_obstacles_map = refmap.empty_like()
            self.robot_static_obstacles_map.fill_polygon_obstacles(self.robot_static_obstacles)
        self.human_static_obstacles_map = self.robot_static_obstacles_map.empty_like()
        self.human_static_obstacles_map.fill_polygon_obstacles(self.human_static_obstacles)
        self.controller.set_static_obstacles(static_obstacles, portals)
        self.flow_model.update_static_obstacles_map(self.human_static_obstacles_map)

    def infer_crowd_velocity(self, crowd, dt):
        if self.previous_crowd is None:
            self.previous_crowd = crowd
        crowd_odom = calculate_crowd_velocity(crowd, self.previous_crowd, dt)
        self.previous_crowd = crowd
        return crowd_odom

    def compute_cmd_vel(self, crowd, robot_pose, goal, dt,
                        measured_surface=None, crowd_odom=None, measurement_time=None,
                        show_plot=True, debug=False, debug_dict=None, preplanned_traj=None):
        # If there's no crowd, just do rvo to the goal
        if len(crowd) == 0:
            return self.controller.compute_cmd_vel(crowd, robot_pose, goal, dt,
                                                   show_plot=show_plot, debug=debug)
        # stored inputs
        human_static_obstacles_map = self.human_static_obstacles_map
        robot_static_obstacles_map = self.robot_static_obstacles_map
        static_nudge_vel = self.nudge_max_speed
        if self.version in [6, 7, 8, 9, 10]:
            static_nudge_vel = 0
        if crowd_odom is None:
            crowd_odom = self.infer_crowd_velocity(crowd, dt)
        # flow model
        # interpolate velocity field
        latest_time = self.flow_model.get_latest_observation_time()
        if latest_time is None:
            latest_time = 0
        if measurement_time is None:
            measurement_time = latest_time + dt
        self.flow_model.update_observations(crowd_odom, measurement_time, measured_surface=measured_surface)
        if self.version in [1, 2, 3, 4, 5, 6, 7]:
            crowd_sample = crowd_odom
        elif self.version in [8, 9, 10]:
            crowd_sample, measurement_grid = self.flow_model.get_observation_sample()
        elif self.version in [11]:
            crowd_sample, measurement_grid = self.flow_model.get_observation_sample(weight_decay=0.97)
        else:
            raise NotImplementedError
        vxgrid, vygrid, rhogrid, turbgrid = self.flow_model.get_discrete_model(
            sample=(crowd_sample, measurement_grid))
        # RRT trajectory
        ll = locals()
        if debug_dict is None:
            debug_dict = {}
        debug_dict.update({key: ll[key] for key in [
            'crowd',
            'crowd_odom',
            'crowd_sample',
            'measurement_grid',
            'measurement_time',
            'robot_pose',
            'goal',
            'dt',
            'vxgrid',
            'vygrid',
            'rhogrid',
            'turbgrid',
        ]})
        debug_dict['static_obstacles'] = self.robot_static_obstacles
        def dump_debug_dict(debug_dict=debug_dict, filename="filename.pickle"):
            import pickle
            with open('filename.pickle', 'wb') as handle:
                pickle.dump(debug_dict, handle, protocol=0)
        trajectory, info = plan_trajectory_in_flow(robot_pose, goal,
                                                   vxgrid, vygrid, rhogrid, turbgrid,
                                                   self.robot_max_speed,
                                                   robot_static_obstacles_map,
                                                   self.flow_model.mu,
                                                   static_nudge_vel)
        if preplanned_traj is not None:
            trajectory = preplanned_traj
        debug_dict['trajectory'] = trajectory
        debug_dict['vrx'] = info['vrx']
        debug_dict['vry'] = info['vry']
        nudge_case = False
        # get target vel, determine if nudge case
        if self.version in [1, 2, 3, 4, 5]:
            if len(trajectory) == 0:
                print("too close to wall!")
                raise ValueError
            t, tx, ty, tvx, tvy = trajectory[0]
            target_vel = (tvx, tvy)
            nudge_case = np.linalg.norm(target_vel) < self.nudge_max_speed
        elif self.version in [6, 7, 8, 9, 10, 11]:
            nudge_case = len(trajectory) == 0
            if not nudge_case:
                t, tx, ty, tvx, tvy = trajectory[0]
                target_vel = (tvx, tvy)
        else:
            raise NotImplementedError
        # Run controller to get cmd_vel from target_vel
        if nudge_case:
            print("Nudge")
            if self.version in [4, 6, 8, 9, 10, 11]: # no solution - revert to baseline
                cmd_vel = self.controller.compute_cmd_vel([], robot_pose, goal, dt,
                                                          show_plot=show_plot, debug=debug)
            elif self.version in [2, 3]:
                cmd_vel = self.controller.run_rvo_step([], robot_pose, target_vel, dt,
                                                       show_plot=show_plot, debug=debug)
            elif self.version in [5]:
                cmd_vel = target_vel
            else:
                raise NotImplementedError
            nudge_trajectory = []
            nvx, nvy = ((goal[0]-robot_pose[0]), (goal[1]-robot_pose[1]))
            nvx = nvx / np.sqrt(nvx**2 + nvy**2)
            nvy = nvy / np.sqrt(nvx**2 + nvy**2)
            nudge_trajectory.append([0, robot_pose[0], robot_pose[1], nvx, nvy])
            nudge_trajectory.append([10, goal[0], goal[1], 0, 0])
            nudge_trajectory = np.array(nudge_trajectory).reshape((-1, 5))
            debug_dict['trajectory'] = nudge_trajectory
        else:
            if self.version in [5, 9]:
                cmd_vel = self.controller.run_rvo_step([], robot_pose, target_vel, dt,
                                                       show_plot=show_plot, debug=debug)
            elif self.version in [1, 2, 3, 4, 6, 7, 8, 10, 11]:
                cmd_vel = self.controller.run_rvo_step(crowd_odom, robot_pose, target_vel, dt,
                                                       show_plot=show_plot, debug=debug)
            else:
                raise NotImplementedError
        # plot
        if show_plot:
            vrx = info['vrx']
            vry = info['vry']
            mincost = info['mincost']
            xx, yy = robot_static_obstacles_map.as_meshgrid_xy()
            plt.ion()
            plt.figure("flow")
            plt.clf()
            fig, (axvx, axvy, axrho, axturb, axflow, axbest) = plt.subplots(6, 1, num="flow")
            im1 = axvx.contourf(xx, yy, vxgrid, cmap='PiYG')
            axvx.quiver(crowd_sample[:, 0], crowd_sample[:, 1], crowd_sample[:, 3], crowd_sample[:, 4],
                        width=0.001)
            plt.sca(axvx)
            plt.gca().yaxis.set_label_position("right")
            plt.ylabel("vx")
            plt.axvline(0, color='k')
#             plt.plot(vxgrid[250, :], yy[250, :], color='k')
            plt.plot(trajectory[:, 1], trajectory[:, 2], color='yellow')
            plt.colorbar(im1)
            im2 = axvy.contourf(xx, yy, vygrid, cmap='PiYG')
            axvy.quiver(crowd_sample[:, 0], crowd_sample[:, 1], crowd_sample[:, 3], crowd_sample[:, 4],
                        width=0.001)
            plt.sca(axvy)
            plt.gca().yaxis.set_label_position("right")
            plt.ylabel("vy")
            plt.axvline(0, color='k')
            plt.colorbar(im2)
            im3 = axrho.contourf(xx, yy, rhogrid, cmap='Greens')
            plt.sca(axrho)
            plt.gca().yaxis.set_label_position("right")
            plt.ylabel("density")
            plt.axvline(0, color='k')
            plt.colorbar(im3)
            imturb = axturb.contourf(xx, yy, turbgrid, cmap='Greens')
            plt.sca(axturb)
            plt.gca().yaxis.set_label_position("right")
            plt.ylabel("turbulence")
            plt.axvline(0, color='k')
            plt.colorbar(imturb)
            plt.sca(axflow)
            plt.gca().yaxis.set_label_position("right")
            plt.ylabel("model flow")
            mask = (human_static_obstacles_map.occupancy() > 0.5).astype(np.uint8)
            gridshow(mask)
            plt.quiver(vxgrid.T, vygrid.T)
            plt.sca(axbest)
            plt.gca().yaxis.set_label_position("right")
            plt.ylabel("best vel")
            gridshow(mincost)
            plt.quiver(vrx.T, vry.T)
            plt.pause(0.1)
        return cmd_vel

def plan_trajectory_in_flow(robot_pose, goal,
                            vxgrid, vygrid, rhogrid, turbgrid,
                            max_robot_vel, static_obstacles_map, mu, static_nudge_vel):
    rx, ry, th, vx, vy, w = robot_pose
    xx, yy = static_obstacles_map.as_meshgrid_xy()
    # trajectory: t x y vx vy
    # dijkstra solution
    if isinstance(goal, str) and goal == "x=-20":
        goal_boundary_ij = np.ascontiguousarray(np.array(np.where(xx < -20)).T).astype(np.int64)
    else:
        goal_boundary_ij = static_obstacles_map.xy_to_ij(goal[None,:]).astype(np.int64)
    pose_ij = static_obstacles_map.xy_to_ij(np.array([[rx, ry]]))[0]
    crowd_vel_x = vxgrid.astype(np.float32)
    crowd_vel_y = vygrid.astype(np.float32)
    crowd_turbulence = turbgrid.astype(np.float32)
    crowd_density = rhogrid.astype(np.float32)
    mask = (static_obstacles_map.occupancy() > 0.5).astype(np.uint8)
    mask[int(pose_ij[0]), int(pose_ij[1])] = 0
    from timeit import default_timer as timer
    tic = timer()
    result, vrx, vry = crowdflow_dijkstra(goal_boundary_ij,
                                          crowd_vel_x, crowd_vel_y, crowd_density, crowd_turbulence,
                                          mask, max_robot_vel, mu, static_nudge_vel)
    toc = timer()
    print("{:.2f}ms".format((toc - tic)*1000))
    info = {"vrx": vrx, "vry": vry, "mincost": result}
    trajectory = []
    p = pose_ij * 1.
    t = 0
    while True:
        if not static_obstacles_map.is_inside_ij(p[None,:].astype(np.float32))[0]:
            print("trajectory out of map bounds")
            break
        x, y = static_obstacles_map.ij_to_xy(p[None,:])[0]
        vx = vrx[int(p[0]), int(p[1])]
        vy = vry[int(p[0]), int(p[1])]
        trajectory.append([t, x, y, vx, vy])
        # next point
        if result[int(p[0]), int(p[1])] == 0: # goal reached
            break
        vnorm = np.sqrt(vx*vx + vy*vy)
        if vnorm == 0:
            print("no viable direction to goal")
            trajectory = []
            break
        nidx = np.array([np.sign(vx), np.sign(vy)]) # (-1/0/1, -1,0,1)
        dist = np.linalg.norm(nidx)
        next_p = p + nidx
        next_t = t + dist / vnorm
        p = next_p
        t = next_t
    return np.array(trajectory).reshape((-1, 5)), info
