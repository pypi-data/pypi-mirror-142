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
    url="https://www.github.com/ethz-asl/FlowBot_CrowdBotChallenge",
    version='0.0.7',
    py_modules=['flowplanner', 'rvo'],
    ext_modules=cythonize(["flowplanningtools.pyx"], annotate=True),
    setup_requires=["cython", "numpy"],
    install_requires=['pyyaml', 'numpy'],
    include_dirs=[numpy.get_include()],
)
