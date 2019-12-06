import pathlib
from setuptools import setup

# This call to setup() does all the work
setup(
    name="example_one",
    version="0.1",
    description="Just an example",
    long_description="nothing to see here",
    long_description_content_type="text/markdown",
    url="https://github.com/sema4-EricSchles/",
    author="Eric Schles",
    author_email="ericschles@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["example_one"],
    include_package_data=True
)
