from setuptools import setup, find_packages

VERSION = "1.0.2"
DESCRIPTION = "Netlist file generation"
LONG_DESCRIPTION = "Functions that will automatically generate ADS netlist files using three differenct topologies"

# Setting up
setup(
      name="generate_netlist_files",
      version=VERSION,
      author="Phillip Hagen",
      author_email="<phillip.hagen@outlook.com>",
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      packages=find_packages(),
      install_requires=[],
      keywords=["python", "netlist", "ADS"],
      classifiers=[]
      )