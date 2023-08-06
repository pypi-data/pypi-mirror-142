import pathlib

from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="Prix-Carburant-FR-Gloird-Client",
    version="0.0.2",
    description="StationEssence client by Gloird",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Gloird/essence",
    author="Maxime Wantiez, Yann RITTER, Nicolas <Gloird> DUPUIS",
    author_email="gloird@gmail.com",
    license="MIT",
    packages=["prixCarburantGloirdClient"],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "realpython=reader.__main__:main",
        ]
    },
)
