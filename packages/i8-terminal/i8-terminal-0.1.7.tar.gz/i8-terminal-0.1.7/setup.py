from setuptools import find_packages, setup

from setup_utils import COMMON_ARGS, PACKAGE_NAME, get_requirements

setup(
    **COMMON_ARGS,
    packages=find_packages(),
    package_dir={PACKAGE_NAME: PACKAGE_NAME, "": PACKAGE_NAME},
    install_requires=get_requirements(),
    entry_points={"console_scripts": [f"i8={PACKAGE_NAME}.main:main"]},
    include_package_data=True,
)
