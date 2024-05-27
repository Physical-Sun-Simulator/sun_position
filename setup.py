from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Provides the position of the sun'
LONG_DESCRIPTION = 'Python package that provides TU/e approved sun positioning calculations'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="sun_position", 
        version=VERSION,
        author="Aqiel Oostenbrug",
        author_email="a.oostenbrug@student.tue.nl",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],
)