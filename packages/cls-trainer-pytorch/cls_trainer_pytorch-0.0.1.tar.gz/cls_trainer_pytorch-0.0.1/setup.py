from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.1'
DESCRIPTION = 'General neural network classification trainer compatibile with PyTorch, grid search regime'

# Setting up
setup(
   packages=find_packages(),  # include all packages under src
   package_dir={},
)
