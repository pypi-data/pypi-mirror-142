# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['cgi', 'cgitb']
setup_kwargs = {
    'name': 'legacy-cgi',
    'version': '2.6',
    'description': 'Fork of the standard library cgi and cgitb modules, being deprecated in PEP-594',
    'long_description': "Python CGI\n==========\n\nThis is a fork of the standard library modules ``cgi`` and ``cgitb``.\nThey are slated to be removed from the Python standard libary in\nPython 3.13 by PEP-594_.\n\n.. _PEP-594: https://peps.python.org/pep-0594/\n\nInstallation\n------------\n\nInstall the ``legacy-cgi`` package from PyPI::\n\n  $ pip install legacy-cgi\n\nPurpose\n-------\n\nThe purpose of this fork is to support existing CGI scripts using\nthese modules.  Thus, compatibility is the primary goal.\n\nContributions are accepted, but should be focused on bug fixes instead\nof new features or major refactoring.\n\nNew applications should look at the WSGI_ ecosystem.  There's a number\nof highly-polished web frameworks available, and it's significantly\nfaster in a typical deployment given a new Python process does not\nneed created for each request.\n\n.. _WSGI: https://wsgi.readthedocs.io\n",
    'author': 'Michael McLay',
    'author_email': 'mclay@eeel.nist.gov',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jackrosenthal/python-cgi',
    'py_modules': modules,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
