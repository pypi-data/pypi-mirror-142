import codecs
import os
from setuptools import find_packages, setup
from typing import Any

def read(rel_path: str) -> str:
    """
    Read a file.
    """
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()

# TODO: move get_version and its dependecies to a third module (maybe setup_utils.py)
def get_version(rel_path: str) -> Any:
    """
    Read version from a file.
    """
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

PACKAGE_NAME = "i8_terminal"
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="i8-terminal",
    version=get_version(f"{PACKAGE_NAME}/__init__.py"),
    author="investoreight",
    author_email="info@investoreight.com",
    license="LICENSE.txt",
    description="Investor8 CLI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    package_dir={PACKAGE_NAME: PACKAGE_NAME, "": PACKAGE_NAME},
    entry_points={"console_scripts": [f"i8={PACKAGE_NAME}.main:main"]},
    include_package_data=True,
)
