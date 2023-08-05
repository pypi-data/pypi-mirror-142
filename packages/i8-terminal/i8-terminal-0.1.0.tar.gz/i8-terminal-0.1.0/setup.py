from setuptools import find_packages, setup

from setup_cx import get_version

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
