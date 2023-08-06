
import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="commitizen-cz-fogoprobr",
    version="1.0.2",
    py_modules=["cz_fogoprobr"],
    license="MIT",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/melattofogo/cz-fogoprobr",
    install_requires=["commitizen>=2.21.2"],
)
