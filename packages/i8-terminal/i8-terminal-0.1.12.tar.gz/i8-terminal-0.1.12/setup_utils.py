import codecs
import os
from typing import Any, List

PACKAGE_NAME = "i8_terminal"


def read(rel_path: str) -> str:
    """
    Read a file.
    """
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def get_version() -> Any:
    """
    Read version from a file.
    """
    rel_path = f"{PACKAGE_NAME}/__init__.py"
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


def get_long_description() -> str:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
    return long_description


def get_requirements() -> List[str]:
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        requirements = fh.read()
    return requirements.strip().split("\n")


COMMON_ARGS = dict(
    name="i8-terminal",
    version=get_version(),
    author="investoreight",
    author_email="info@investoreight.com",
    license="LICENSE.txt",
    description="Investor8 CLI",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
)
