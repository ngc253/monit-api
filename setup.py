# Always prefer setuptools over distutils
from codecs import open
from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Monit Cluster API',

    version='1.0.0',

    description='An open source api m/monit',
    long_description=long_description,

    url='https://github.com/sridhav/monit-api',

    author='Sridhar Vemula',
    author_email='sridhar.vemula2@gmail.com',

    license='MIT',

    classifiers=[
        'Programming Language :: Python :: 2.7.5',
    ],
    keywords='monit cluster m/monit ui mmonit',
    zip_safe= False,
    packages=find_packages(exclude=['contrib', 'static', 'docs', 'tests*']),

    install_requires=['flask', 'flask-restful', 'flask-script', 'flask-jwt_extended', 'flask-migrate', 'pytest', 'flask-sqlalchemy'],

    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    }
)
