# run python setup.py install to install
# run python setup.py sdist to generate a tarball

from distutils.core import setup

setup(
    name = 'libpgm3',
    version = '1.3.5',
    author = 'CyberPoint International, LLC',
    author_email = 'mraugas@cyberpointllc.com',
    url = 'http://www.cyberpointllc.com',
    description = 'A library for creating and using probabilistic graphical models. *Unofficial update to support python 3*',
    long_description = 'This library provides tools for modeling large systems with Bayesian networks. Using these tools allows for efficient statistical analysis on large data sets.',
    packages = ['libpgm3', 'libpgm3.CPDtypes', 'utils'],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Topic :: Scientific/Engineering :: Mathematics'
    ]
)
