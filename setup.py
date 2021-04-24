from setuptools import setup
from setuptools import find_namespace_packages

# Open the README file.
with open(file="README.md", mode="r") as fh:
    long_description = fh.read()

setup(

    name='energy-information-administraion-scraper',
    version='0.1.0',
    install_requires=[
        'requests==2.24.0',
        'beautifulsoup4==4.9.3'
    ],
    packages=find_namespace_packages(
        include=['energy_feed']
    ),
    python_requires='>3.7',

)
