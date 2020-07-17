from setuptools import setup, find_packages

setup(
    name='dcs',
    author='John McLevey',
    author_email='john.mclevey@uwaterloo.ca',
    url='https://github.com/mclevey/dcs',
    packages=find_packages(),
    package_data={'dcs': ['data/*']},
    include_package_data=True,
    install_requires=[
          'pandas',
      ]
)