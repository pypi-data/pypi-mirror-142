import setuptools
import os
import re
import sys

with open("README.md", "r") as fh:
    long_description = fh.read()

PACKAGE_NAME = 'fakertype'
current_path = os.path.abspath(os.path.dirname(__file__))
version_line = open(os.path.join(current_path, PACKAGE_NAME, 'version.py'), "rt").read()

m = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_line, re.M)
__version__ = m.group(1)

setuptools.setup(
    name = PACKAGE_NAME,
    version = __version__, # versions '0.0.x' are unstable and subject to refactor
    author = "Muhammad Yasirroni",
    author_email = "muhammadyasirroni@gmail.com",
    description = "Generate fake data in specified type data",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/yasirroni/fakertype",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python",
    ],
    python_requires = ">=3.6",
    install_requires = [
        "Faker", 
    ],
)