"""Setup script for MissingValuesGraph"""

# Standard library imports
import pathlib

# Third party imports
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).resolve().parent

# The text of the README file is used as a description
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="MissingValuesGraph",
    version="4.0.0",
    description="Find the missing values for any dataframe/dataset",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/sthirumoorthi/MissingValuesGraph",
    author="Thirumoorthi S",
    author_email="thirumoorthiksr@gmail.com",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["MissingValuesGraph"],
    include_package_data=True,
)