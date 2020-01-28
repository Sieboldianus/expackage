# -*- coding: utf-8 -*-

"""
Setup for building and installing expackage
"""

from setuptools import setup

with open('README.md') as f:
    LONG_DESCRIPTION = f.read()


setup(name="expackage",
      version="0.0.1",
      description="ExamplePackage: demonstrates "
      "joblib/loky multiprocessing issue in frozen executable",
      long_description=LONG_DESCRIPTION,
      long_description_content_type='text/markdown',
      author='Sieboldianus',
      url='https://github.com/Sieboldianus/expackage',
      license='WTFPL',
      packages=['expackage'],
      include_package_data=True,
      python_requires='>=3.7',
      install_requires=[
          'numpy',
          'cython',
          'hdbscan',
      ],
      entry_points={
          'console_scripts': [
              'expackage = expackage.__main__:main'
          ]
      })
