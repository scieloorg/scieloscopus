# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

install_requires = []

tests_require = []

setup(
    name='scieloscopus',
    version='1.0.0',
    description='Library to delivery Scopus and Scimago indicators of SciELO Journals',
    url='https://github.com/scieloorg/scieloscopus',
    license='BSD 2-clause "Simplified" License',
    author='SciELO',
    author_email='scielo-dev@googlegroups.com',
    maintainer='Ednilson Gesseff',
    maintainer_email='ednilson.gesseff@scielo.org',
    keywords='scielo scopus scimago cwts journal bibliometry bibliometric indicators data sciences',
    packages=find_packages(),
    include_package_data=True,
        classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    dependency_links=[],
    tests_require=tests_require,
    test_suite='tests',
    install_requires=install_requires,
)
