
import io
import os
import subprocess
import shutil

from setuptools import setup, find_packages, Command

NAME = "pyflowline"
DESCRIPTION = \
    "River network for Earth Science"
AUTHOR = "Chang Liao"
AUTHOR_EMAIL = "chang.liao@pnnl.gov"
URL = "https://github.com/changliao1025/pyflowline"
VERSION = "0.1.16"
REQUIRES_PYTHON = ">=3.8.0"
KEYWORDS = "Earth Science"

REQUIRED = [
    "numpy", 
    "gdal",
    "netCDF4",
    "shapely"
]

CLASSIFY = [
    "Development Status :: 4 - Beta",
    "Operating System :: OS Independent",
    "Intended Audience :: Science/Research",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Topic :: Scientific/Engineering",
    "Topic :: Scientific/Engineering :: Visualization"
]

HERE = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(
            HERE, "README.md"), encoding="utf-8") as f:
        LONG_DESCRIPTION = "\n" + f.read()

except FileNotFoundError:
    LONG_DESCRIPTION = DESCRIPTION


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license="custom",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    python_requires=REQUIRES_PYTHON,
    keywords=KEYWORDS,
    url=URL,
    packages=find_packages(),
    install_requires=REQUIRED,
    classifiers=CLASSIFY
)
