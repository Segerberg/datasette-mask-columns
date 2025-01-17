from setuptools import setup
import os

VERSION = "0.2.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-mask-columns",
    description="Datasette plugin that masks specified database columns",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-mask-columns",
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_mask_columns"],
    entry_points={"datasette": ["mask_columns = datasette_mask_columns"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest", "pytest-asyncio", "httpx", "sqlite-utils"]},
    tests_require=["datasette-mask-columns[test]"],
)
