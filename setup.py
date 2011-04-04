# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(
        os.path.join(
            os.path.join(os.path.dirname(__file__), 'docs'),
            *rnames)).read()

version = 0.1
long_description = read('README.txt') + '\n' + read('CHANGES.txt')

install_requires = [
    'setuptools',
    'Chameleon >= 2.0rc7',
    'cromlech.browser',
    ]

tests_require = [
    'zope.component',
    'zope.interface',
    'dolmen.template',
    ]

setup(
    name='dolmen.tales',
    version=version,
    author='Grok & Dolmen Teams',
    author_email='',
    url='http://gitweb.dolmen-project.org',
    download_url='http://pypi.python.org/pypi/dolmen.tales',
    description='Various TALES support the TAL engine',
    long_description=long_description,
    license='ZPL',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        ],
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    namespace_packages=['dolmen'],
    include_package_data = True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'test': tests_require
        },
)
