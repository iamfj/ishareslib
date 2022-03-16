"""Python setup.py for project_name package"""
import io
import os

from setuptools import find_packages, setup


def read(*paths, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        return open_file.read().strip()


def read_requirements(*paths):
    return [
        line.strip()
        for path in paths
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="ishareslib",
    version="0.1.0",
    author="Fabian Jocks (iamfj) <dev@jocks.io>",
    url="https://github.com/iamfj/ishareslib/",
    description="A library for reading data from the ishares product family.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    extras_require={
        "dev": read_requirements("requirements-dev.txt"),
        "test": read_requirements("requirements-dev.txt", "requirements-test.txt"),
    },
)