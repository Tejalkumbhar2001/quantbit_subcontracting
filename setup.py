from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in quantbit_subcontracting/__init__.py
from quantbit_subcontracting import __version__ as version

setup(
	name="quantbit_subcontracting",
	version=version,
	description="subcontracting details",
	author="quantbit technologies pvt ltd",
	author_email="contact@erpdata.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
