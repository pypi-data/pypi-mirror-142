from setuptools import setup

with open('README.md','r') as fh:
    long_desc = fh.read()
setup(
    name='heuristicsearch',
    version='0.0.4',
    description='Heuristic Searches',
    py_modules=['a_star_search','ao_star','graph'],
    package_dir={'':'src'},
    classifiers=["Intended Audience :: Education", 
    "Operating System :: OS Independent", 
    "Programming Language :: Python :: 3.0",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8"],
    long_description=long_desc,
    long_description_content_type="text/markdown"
)