from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'A simple library to calculate anything and everything about circles and polygons.'
LONG_DESCRIPTION = 'Clygon is a library built to calculate everything from circles to polygons. You can calculate the interior angles of a polygon, or the area of any n-gon, and even the arc length, radius, or central angle of a circle.'


# Setting up
setup(
    name="clygon",
    version=VERSION,
    author="Krishay Rastogi",
    author_email="<krishayras@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['math'],
    keywords=['python', 'math', 'geometry', 'polygons', 'circles', 'angles', 'sides'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

