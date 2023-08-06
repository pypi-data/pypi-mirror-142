#!/usr/bin/env python
import os
from distutils.core import setup

from setuptools import find_packages  # type: ignore


def _get_version():
    version_file = os.path.normpath(os.path.join(os.path.dirname(__file__), 'PipeRider', 'VERSION'))
    with open(version_file) as fh:
        version = fh.read().strip()
        return version


setup(name='piperider-python-sdk',
      version=_get_version(),
      description='PipeRider Python SDK',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      url='https://github.com/InfuseAI/piperider-python-sdk',
      python_requires=">=3.6",
      packages=find_packages(),
      install_requires=['requests', 'types-requests'],
      extras_require={
          'dev': [
              'pytest>=4.6',
              'pytest-flake8',
              'flake8==3.9.2',
              'pytest-cov',
              'twine',
              'boto3',
          ],
      },
      project_urls={
          "Bug Tracker": "https://github.com/InfuseAI/piperider-python-sdk/issues",
      },
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: Apache Software License",
          "Operating System :: OS Independent",
          "Development Status :: 4 - Beta"
      ],
      package_data={
          'PipeRider': ['*.json', 'VERSION']
      })
