# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

version = "1.0+crom"

install_requires = [
    'crom',
    'Chameleon >= 2.4',
    'cromlech.browser >= 0.5',
    'setuptools',
    ]

tests_require = [
    'pytest',
    'cromlech.browser [test]',
    'zope.interface',
    ]

setup(
    name='dolmen.tales',
    version=version,
    author='Cromlech team',
    author_email='dolmen@list.dolmen-project.org',
    url='http://gitweb.dolmen-project.org',
    download_url='http://pypi.python.org/pypi/dolmen.tales',
    description='Various TALES support the TAL engine',
    long_description=(open("README.txt").read() + "\n" +
                      open(os.path.join("docs", "HISTORY.txt")).read()),
    license='ZPL',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['dolmen'],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'test': tests_require
        },
    entry_points="""
    # -*- Entry points: -*-
    [chameleon.tales]
    slot = dolmen.tales.slot:SlotExpr
    """,
    )
