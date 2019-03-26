from setuptools import setup, find_packages

with open('README.md', 'r') as f:
  long_description = f.read()

setup(
  name="otrs-rest",
  version="1.0.0",
  author="Laurens van Dijk",
  author_email="lzvdijk@gmail.com",
  description="A python3 library for interacting with an OTRS REST webservice",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/lzvdijk/otrs-libs",
  packages=find_packages(),
  classifiers=(
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: GPLv3.0",
    "Operating System :: OS Independent",
  ),
)

