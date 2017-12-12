"setup.py"

from setuptools import setup

setup(
    # Application name:
    name="LibCrawler",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Matthijs Hoogendoorn",
    author_email="matthijshoogendoorn@gmail.com",

    # Packages
    packages=["libcrawler"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="https://github.com/MatthijsHoogendoorn/LibCrawler",

    #
    # license="LICENSE.txt",
    description="LibCrawler. A library responsible to serve data extracted from HTML.",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        "bs4", "requests", "lxml"
    ],
)
