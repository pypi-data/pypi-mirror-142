"""Setup file for Python lib."""
import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="simple_repr",
    version="1.2.1",
    description="SimpleRepr is a class for creating string representations of classes.",
    url="https://github.com/mr-strawberry66/python-repr-generation",
    author="Sam Kenney",
    author_email="sam.kenney@me.com",
    license="MIT",
    long_description_content_type="text/markdown",
    long_description=long_description,
    platforms=[],
    packages=["simple_repr"]
    + ["simple_repr." + pkg for pkg in find_packages("simple_repr", exclude=["tests"])],
)
