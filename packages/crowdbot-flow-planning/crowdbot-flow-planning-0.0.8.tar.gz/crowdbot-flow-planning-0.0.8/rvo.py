import numpy as np
from matplotlib import pyplot as plt
import rvo2

_O = 6 # constant: number of odometry elements

def angle_difference_rad(target_angle, angle):
    """     / angle
           /
          / d
         /)___________ target
    """
    delta_angle = angle - target_angle
    delta_angle = np.arctan2(np.sin(delta_angle), np.cos(delta_angle))  # now in [-pi, pi]
    return delta_angle

class NavigationPlanner(object):
    robot_radius = 0.3  # [m]
    safety_distance = 0.1  # [m]
    robot_max_speed = 1.  # [m/s]
    robot_max_w = 1. # [rad/s]
    robot_max_accel = 0.5  # [m/s^2]
    robot_max_w_dot = 10.  # [rad/s^2]

    def __init__(self):
        raise NotImplementedError

    def set_static_obstacles(self, static_obstacles, portals):
        self.human_static_obstacles = static_obstacles
        self.robot_static_obstacles = static_obstacles + portals

    def compute_cmd_vel(self, crowd, robot_pose, goal, dt, show_plot=True, debug=False):
        raise NotImplementedError

class RVONavigationPlanner(NavigationPlanner):
    def __init__(self):
        # variables
        self.sim = None
        # RVO parameters
        self.neighbor_dist = 10.
        self.max_neighbors = 10
        self.time_horizon = 5.
        self.time_horizon_obst = 5.
        self.marker_publisher = None

    def compute_cmd_vel(self, crowd, robot_pose, goal, dt, show_plot=True, debug=False):
        if isinstance(goal, str) and goal == "x=-20":
            goal = np.array([-20, 0])
        x, y, th, vx, vy, w = robot_pose
        pref_vel = goal[:2] - np.array([x, y])
        pref_vel = pref_vel / np.linalg.norm(pref_vel) * self.robot_max_speed
        crowd_odom = np.zeros((len(crowd), _O))
        if len(crowd) != 0:
            crowd_odom[:, :2] = crowd[:, 1:3]
        return self.run_rvo_step(crowd_odom, robot_pose, pref_vel, dt, show_plot=show_plot, debug=debug)

    def run_rvo_step(self, crowd_odom, robot_pose, target_vel, dt, show_plot=True, debug=False):
        x, y, th, vx, vy, w = robot_pose
        # these params could be defined in init, or received from simulator
        human_radius = 0.3

        # create sim with static obstacles if they don't exist
        if self.sim is None:
            self.sim = rvo2.PyRVOSimulator(dt,
                                           self.neighbor_dist, self.max_neighbors,
                                           self.time_horizon, self.time_horizon_obst,
                                           human_radius, 0.)
            for obstacle in self.robot_static_obstacles:
                self.sim.addObstacle(obstacle)
            self.sim.processObstacles()

        self.sim.clearAgents()

        # add robot
        self.sim.addAgent((x, y),
                          self.neighbor_dist, self.max_neighbors,
                          self.time_horizon, self.time_horizon_obst,
                          self.robot_radius + self.safety_distance,
                          self.robot_max_speed, (vx, vy))

        self.sim.setAgentPrefVelocity(0, tuple(target_vel))

        # add crowd
        for i, person in enumerate(crowd_odom):
            self.sim.addAgent(tuple(person[:2]),
                              self.neighbor_dist, self.max_neighbors,
                              self.time_horizon, self.time_horizon_obst,
                              human_radius + 0.01 + self.safety_distance,
                              0.5, (0,0))
            vel = (person[3], person[4])
            self.sim.setAgentPrefVelocity(i + 1, vel)

        if show_plot:
            plt.ion()
            plt.figure(2)
            plt.cla()
            n_steps = 10
            for s in range(n_steps):
                for i in range(self.sim.getNumAgents()):
                    x, y = self.sim.getAgentPosition(i)
                    plt.gca().add_artist(plt.Circle((x, y),
                                                    self.robot_radius if i == 0 else human_radius,
                                                    color='b' if i == 0 else 'r',
                                                    fill=s == 0,
                                                    ))
                self.sim.doStep()
                if s == 0:
                    vx, vy = self.sim.getAgentVelocity(0)
            for wall in self.robot_static_obstacles:
                wall = np.array(wall)
                plt.plot(wall[:, 0], wall[:, 1], 'k')
            plt.xlim([-22, 22])
            plt.ylim([-5.5, 5.5])
            plt.pause(0.1)
        else:
            self.sim.doStep()
            vx, vy = self.sim.getAgentVelocity(0)
        if self.marker_publisher is not None:
            from visualization_msgs.msg import Marker, MarkerArray
            import rospy
            def point_as_marker(point_xy, frame, scale, namespace, time=None, color=None, id_=0, z=0):
                marker = Marker()
                time = rospy.Time.now() if time is None else time
                marker.header.stamp.secs = time.secs
                marker.header.stamp.nsecs = time.nsecs
                marker.header.frame_id = frame
                marker.ns = namespace
                marker.id = id_
                marker.type = marker.SPHERE
                marker.action = 0
                s = scale
                marker.scale.x = s
                marker.scale.y = s
                marker.scale.z = s
                if color is None:
                    marker.color.g = 1.
                    marker.color.a = 0.5
                else:
                    marker.color.r = color[0]
                    marker.color.g = color[1]
                    marker.color.b = color[2]
                    marker.color.a = color[3]
                marker.pose.position.x = point_xy[0]
                marker.pose.position.y = point_xy[1]
                marker.pose.orientation.w = 1
                return marker
            frame = "sim_map"
            ma = MarkerArray()
            color = (0., 0., 1., 0.5)
            ma.markers.append(point_as_marker(robot_pose[:2], frame, 0.2, "next", id_=0, color=(0, 0, 0, 1)))
            for n in range(3):
                x, y = self.sim.getAgentPosition(0)
                ma.markers.append(point_as_marker([x, y], frame, 0.2, "next", id_=n+1, color=color))
                self.sim.doStep()
            self.marker_publisher.publish(ma)

        speed = np.linalg.norm([vx, vy])
        robot_angle = th
        heading_x = np.cos(robot_angle)
        heading_y = np.sin(robot_angle)
        desired_angle = np.arctan2(vy, vx)
        # rotate to reduce angle difference to desired angle
        rot = -angle_difference_rad(desired_angle, robot_angle)

        if show_plot:
            if False:
                plt.ion()
                plt.figure(1)
                plt.cla()
                plt.plot([x, x+vx], [y, y+vy])
                plt.plot([x, x+target_vel[0]], [y, y+target_vel[1]])
                plt.plot([x, x+heading_x*self.robot_radius], [y, y+heading_y*self.robot_radius], color='white')
                plt.gca().add_artist(plt.Circle((x, y), self.robot_radius, color='b'))
                for cx, cy, cth, cvx, cvy, cvth in crowd_odom:
                    plt.gca().add_artist(plt.Circle((cx, cy), human_radius, color='r'))
                    plt.plot([cx, cx+cvx], [cy, cy+cvy], color='white')
                plt.xlim([-22, 22])
                plt.ylim([-5.5, 5.5])
                plt.pause(0.1)
        print("SOLUTION ------")
        print(speed, rot)

        return (speed, rot)

