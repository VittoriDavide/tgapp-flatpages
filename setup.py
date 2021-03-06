# -*- coding: utf-8 -*-
import sys, os

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

install_requires=[
    "TurboGears2 >= 2.3.0",
    "tgext.pluggable",
    "docutils",
    "tgext.admin >= 0.7.1",
    "tgext.crud >= 0.8.1",
    "filedepot",
    "rst2pdf",
    "kajiki",
]

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
except IOError:
    README = ''

setup(
    name='tgapp-flatpages',
    version='0.3.1',
    description='Pluggable application to manage static pages (/about) on DB (sqlalchemy or ming) with RST or html',
    long_description=README,
    author='Alessandro Molina',
    author_email='alessandro.molina@axant.it',
    url='https://github.com/axant/tgapp-flatpages',
    keywords='turbogears2.application',
    packages=find_packages(exclude=['ez_setup']),
    install_requires=install_requires,
    include_package_data=True,
    package_data={'tgapp.flatpages': ['i18n/*/LC_MESSAGES/*.mo',
                                 'templates/*/*',
                                 'public/*/*']},
    entry_points="""
    """,
    zip_safe=False
)
