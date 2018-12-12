#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name="python-bytom",
      version="1.0.3",
      description="Bytom Python SDK",
      license="MIT",
      install_requires=["simplejson","requests", "six", "pysha3"],
      author="cnfuyu",
      author_email="cnfuyu@gmail.com",
      url="https://github.com/Bytom-Community/python-bytom",
      packages = find_packages(),
      keywords= "bytom python sdk api wallet",
      zip_safe = True,
      classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
