from setuptools import setup, find_packages
import pathlib

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.3'
DESCRIPTION = 'Deep learning anti-cheat for CSGO'
LONG_DESCRIPTION = 'Deep learning anti-cheat for CSGO'

# Setting up
setup(
    name="DLAC",
    version=VERSION,
    author="LaihoE",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "numpy==1.21.5",
        "onnxruntime==1.10.0",
        "pandas==1.3.5",
        "scikit-learn==1.0.1"
        ],
    include_package_data=True
)