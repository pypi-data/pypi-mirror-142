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

# TODO: get this from requirments.txt?
requirments = ["click==8.0.3", "pandas==1.4.0", "requests==2.25.1", "arrow==1.0.3", "investor8-sdk==1.1.0", 
               "pyyaml==5.4.1", "rich==10.11.0", "plotly==5.3.1", "dash==2.0.0", "dash-bootstrap-components==1.0.0", 
               "kaleido==0.2.1", "openpyxl==3.0.9", "click-repl==0.2.0", "cx-Freeze==6.10"]
 
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
    install_requires=requirments
)
