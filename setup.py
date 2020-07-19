from setuptools import setup, find_packages

from glob import glob

setup(
    name='dcs',
    author='John McLevey',
    author_email='john.mclevey@uwaterloo.ca',
    url='https://github.com/mclevey/dcs',
    packages=find_packages(),
    package_dir={'dcs': 'dcs'},
    include_package_data=False,
    install_requires=[
          'pandas',
      ]
)