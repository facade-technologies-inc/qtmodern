#!/usr/bin/env python

import qtmodern_facade
from setuptools import setup

_version = qtmodern_facade.__version__

setup(name='qtmodern_facade',
      version=_version,
      packages=['qtmodern_facade'],
      description='Qt Widgets Modern User Interface',
      long_description=open('README.rst').read(),
      author='Facade Technologies',
      author_email='cto@facade-technologies.com',
      url='https://github.com/facade-technologies-inc/qtmodern',
      license='MIT',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: User Interfaces'
      ],
      package_data={
          'qtmodern_facade': ['resources/*']
      },
      install_requires=['PySide2==5.15.0'])
