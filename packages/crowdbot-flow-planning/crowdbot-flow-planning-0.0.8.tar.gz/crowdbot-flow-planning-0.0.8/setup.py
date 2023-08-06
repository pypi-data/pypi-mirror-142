import numpy
from setuptools import setup
from Cython.Build import cythonize

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name="crowdbot-flow-planning",
    description='',
    author='Daniel Dugas',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/ethz-asl/FlowBot_CrowdBotChallenge/tree/flowbot/Crowdbotsim_python/crowdbotsimcontrol", # noqa
    version='0.0.8',
    py_modules=['flowplanner', 'rvo'],
    ext_modules=cythonize(["flowplanningtools.pyx"], annotate=True),
    setup_requires=["cython", "numpy"],
    install_requires=['pyyaml', 'numpy'],
    include_dirs=[numpy.get_include()],
)
