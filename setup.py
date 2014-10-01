#!/usr/bin/env python
# -*- coding: utf-8 -*-

# django-milcam
# setup.py

from setuptools import setup, find_packages

# metadata
VERSION = (0, 3, 1)
__version__ = '.'.join(map(str, VERSION))

setup(
    name="django-milcam",
    version=__version__,
    packages=find_packages(),
    install_requires=[
        'Django==1.6.7',
        'pytz==2014.4',
        'django-geoposition==0.2.2',
        'PIL==1.1.7',
        'sorl-thumbnail==11.12',
        'django-uuidfield==0.5.0',
        'django-annoying==0.8.0',
        'django-tastypie==0.11.1',
        'django-js-reverse==0.3.3',
    ],
    author="Anonymous Ukrainian Patriot",
    author_email="anonymous.ukrainian.patriot@gmail.com",
    description="Military Camera project",
    license="GPLv3 or later",
    url="https://github.com/anonymous-ukrainian-patriot/django-milcam/",
    download_url="https://github.com/anonymous-ukrainian-patriot/django-milcam/archive/%s.tar.gz" % __version__,
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Environment :: Plugins",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: Unix",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Utilities",
    ]
)
