
# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ''

setup(
    long_description=readme,
    name='mobilitydb_sqlalchemy',
    version='0.1.0',
    python_requires='==3.*,>=3.8.0',
    project_urls={"documentation": "https://mobilitydb_sqlalchemy.readthedocs.io/en/latest/", "homepage": "https://github.com/adonmo/mobilitydb_sqlalchemy", "repository": "https://github.com/adonmo/mobilitydb_sqlalchemy"},
    author='B Krishna Chaitanya',
    author_email='bkchaitan94@gmail.com',
    keywords='geo gis postgres mobilitydb sqlalchemy orm',
    classifiers=['Development Status :: 3 - Alpha', 'Environment :: Plugins', 'Operating System :: OS Independent', 'Programming Language :: Python', 'Programming Language :: Python :: 3', 'Programming Language :: Python :: 3.7', 'Programming Language :: Python :: 3.8', 'Intended Audience :: Developers', 'Intended Audience :: Information Technology', 'Intended Audience :: Science/Research', 'License :: OSI Approved :: MIT License', 'Natural Language :: English', 'Topic :: Database :: Database Engines/Servers', 'Topic :: Scientific/Engineering :: GIS'],
    packages=['mobilitydb_sqlalchemy', 'mobilitydb_sqlalchemy.types'],
    package_dir={"": "."},
    package_data={},
    install_requires=['geoalchemy2==0.*,>=0.6.3', 'pandas==0.*,>=0.25.3', 'shapely==1.*,>=1.6.4', 'sqlalchemy==1.*,>=1.3.11'],
    extras_require={"dev": ["black==19.*,>=19.10.0", "dephell==0.*,>=0.7.9", "fissix==19.*,>=19.2.0", "pre-commit==1.*,>=1.20.0", "psycopg2==2.*,>=2.8.4", "pytest==5.*,>=5.3.2", "sphinx==2.*,>=2.3.0", "sphinx-rtd-theme==0.*,>=0.4.3"]},
)