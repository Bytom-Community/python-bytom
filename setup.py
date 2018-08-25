#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name="python-bytom",
      version="1.0.0",
      description="Bytom Python SDK",
      license="MIT",
      install_requires=["simplejson","requests", "six", "pysha3"],
      author="cnfuyu",
      author_email="cnfuyu@gmail.com",
      url="https://github.com/Bytom-Community/python-bytom",
      packages = find_packages(),
      keywords= "bytom",
      zip_safe = True)
