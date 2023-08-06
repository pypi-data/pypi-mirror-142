import setuptools

from loci_snyk import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="loci-snyk",
    author="TheTwitchy",
    version=__version__,
    author_email="thetwitchy@thetwitchy.com",
    description="The official Loci Notes Snyk results output processor.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/loci-notes/loci-snyk",
    packages=setuptools.find_packages(),
    install_requires=[
        "click",
        "requests",
        "rich",
        "pendulum"
    ],
    entry_points={
        "console_scripts": [
            "loci-snyk = loci_snyk.main:loci_snyk",
        ],
    },
)
