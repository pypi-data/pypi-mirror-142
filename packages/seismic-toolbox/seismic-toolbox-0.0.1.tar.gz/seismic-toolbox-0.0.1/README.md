# seismic-toolbox

The purpose of this repository is to be used as 
an open-source library as a base others projects, sometimes
closed source.

A goal is also to have as few requirements as possible, namely numpy (and possibly pandas in the future).

Packages include:
-   reader: a seg reader interface and a seg-y implementation.

## Installation
Here is one way to create an environment using conda.
```
conda create --name seismic python=3.10
conda activate seismic
```

### User mode
`pip install seismic-toolbox`

### Dev mode
Clone the repository, activate your environment, cd to 
the `seismic-toolbox` directory and install using:

`pip install -e .`


## Release
```shell
flake8
rm -fR dist
rm -fR build
python setup.py sdist bdist_wheel
twine upload dist/*
```
