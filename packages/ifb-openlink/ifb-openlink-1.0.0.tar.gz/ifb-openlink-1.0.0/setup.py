#!/usr/bin/env python

from setuptools import find_packages, setup

from openlink import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ifb-openlink',
    version=__version__,
    description='A dashboard that establish links between the structure of a research project and multiple data sources ',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='FAIR, open-data, data-managment-tools',
    url='https://gitlab.com/igbmc/openlink',
    project_urls={
        'Bug Tracker': 'https://gitlab.com/igbmc/openlink/-/issues',
        'Source Code': 'https://gitlab.com/igbmc/openlink',
    },
    author='Laurent Bouri, Julien Seiler',
    license='GNU General Public License v3 (GPLv3)',
    python_requires='>=3.6',
    packages=find_packages(),
    install_requires=[
        'django==3.0.7',
        'django-crispy-forms==1.9.1',
        'django-filter==2.3.0',
        'django-widget-tweaks==1.4.8',
        'django_extensions==2.2.9',
        'django_json_ld==0.0.4',
        'requests==2.23.0',
        'django-popup-forms==1.0.3',
        'wheel==0.34.2',
        'omero-py==5.6.0',
        'djangorestframework==3.11.1',
        'django-rq==2.4.0',
        'django-guardian==2.3.0',
        'django-ckeditor==6.1.0',
        'django-debug-toolbar==3.2.1',
        'paramiko==2.7.2',
        'django-environ==0.8.1',
    ],
    entry_points={
        'console_scripts': [
            'openlink = openlink:manage',
        ],
    },
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Django :: 3.0',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Topic :: Scientific/Engineering',
        'Topic :: System :: Systems Administration',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ]
)
