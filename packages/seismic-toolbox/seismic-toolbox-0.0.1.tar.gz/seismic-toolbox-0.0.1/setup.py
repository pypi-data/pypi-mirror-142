import setuptools
from distutils.core import Extension

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    require = [x.strip() for x in f.readlines() if not x.startswith('git+')]

setuptools.setup(
    name="seismic-toolbox",
    version="0.0.1",
    author="Olivier Winter",
    description="Seismic toolbox for numpy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oliche/seismic-toolbox",
    project_urls={
        "Bug Tracker": "https://github.com/oliche/seismic-toolbox/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=require,
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where="src"),
    package_data={'seistools': ['sampleconversion.x86_64.so']},
    python_requires=">=3.7",
    ext_modules=[Extension("seistools.sampleconversion", ["./src/seistools/sampleconversion.c"])]
)
