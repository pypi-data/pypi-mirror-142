import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent
# The text of the README file
README = (HERE / "README.rst").read_text()
# This call to setup() does all the work
setup(
    name="target_describe",
    version="0.0.3",
    description="Generate viz for your variables with your target for ML",
    long_description=README,
    url="https://github.com/DanielR59/target_description",
    author="Daniel Rosas",
    author_email="daniel_pumas_59@hotmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=open("requirements.txt").readlines(),
)
