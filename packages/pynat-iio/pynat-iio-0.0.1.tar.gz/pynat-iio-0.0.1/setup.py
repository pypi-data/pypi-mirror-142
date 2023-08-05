import re

import setuptools


# From: https://github.com/smartcar/python-sdk/blob/master/setup.py
def _get_version():
    """Extract version from package."""
    with open("nat/__init__.py") as reader:
        match = re.search(
            r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', reader.read(), re.MULTILINE
        )
        if match:
            return match.group(1)
        else:
            raise RuntimeError("Unable to extract version.")


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pynat-iio",
    version=_get_version(),
    author="Thomas Florkowski",
    author_email="thomas.florkowski@nateurope.com",
    description="Interfaces to stream data from N.A.T. hardware",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NAT-GmbH/pynat-iio",
    packages=setuptools.find_packages(exclude=["test*"]),
    python_requires=">=3.6",
    install_requires=["pyadi-iio[jesd]"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)
