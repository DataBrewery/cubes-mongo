from setuptools import setup, find_packages

setup(
    name = "cubes-mongo",
    version = '0.1',

    packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_data = {
    },

    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python',
        'Topic :: Database',
        'Topic :: Scientific/Engineering',
        'Topic :: Utilities'
    ],

    entry_points={
    },

    test_suite = "tests",

    # metadata for upload to PyPI
    author = "Robin Thomas",
    author_email = "rthomas@squarespace.com",
    description = "MongoDB Backend for Cubes Python OLAP",
    license = "MIT",
    keywords = "olap multidimensional data analysis",
    url = "http://cubes.databrewery.org"
)

