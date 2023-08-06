# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ascl_net_scraper']

package_data = \
{'': ['*']}

install_requires = \
['bs4>=0.0.1,<0.0.2',
 'charmonium.cache>=1.2.6,<2.0.0',
 'html5lib>=1.1,<2.0',
 'requests>=2.27.1,<3.0.0']

setup_kwargs = {
    'name': 'ascl-net-scraper',
    'version': '0.2.0',
    'description': 'Scrapes the data from https://ascl.net',
    'long_description': "==========================\nascl_net_scraper\n==========================\n\n.. image:: https://img.shields.io/pypi/v/ascl_net_scraper\n   :alt: PyPI Package\n   :target: https://pypi.org/project/ascl_net_scraper\n.. image:: https://img.shields.io/pypi/dm/ascl_net_scraper\n   :alt: PyPI Downloads\n   :target: https://pypi.org/project/ascl_net_scraper\n.. image:: https://img.shields.io/pypi/l/ascl_net_scraper\n   :alt: PyPI License\n.. image:: https://img.shields.io/pypi/pyversions/ascl_net_scraper\n   :alt: Python Versions\n.. image:: https://img.shields.io/github/stars/charmoniumQ/ascl_net_scraper?style=social\n   :alt: GitHub stars\n   :target: https://github.com/charmoniumQ/ascl_net_scraper\n.. image:: https://github.com/charmoniumQ/ascl_net_scraper/actions/workflows/main.yaml/badge.svg\n   :alt: CI status\n   :target: https://github.com/charmoniumQ/ascl_net_scraper/actions/workflows/main.yaml\n.. image:: https://img.shields.io/github/last-commit/charmoniumQ/charmonium.determ_hash\n   :alt: GitHub last commit\n   :target: https://github.com/charmoniumQ/ascl_net_scraper/commits\n.. image:: https://img.shields.io/librariesio/sourcerank/pypi/ascl_net_scraper\n   :alt: libraries.io sourcerank\n   :target: https://libraries.io/pypi/ascl_net_scraper\n.. image:: https://img.shields.io/badge/docs-yes-success\n   :alt: Documentation link\n.. image:: http://www.mypy-lang.org/static/mypy_badge.svg\n   :target: https://mypy.readthedocs.io/en/stable/\n   :alt: Checked with Mypy\n.. image:: https://img.shields.io/badge/code%20style-black-000000.svg\n   :target: https://github.com/psf/black\n   :alt: Code style: black\n\nScrapes the data from https://ascl.net\n\n----------\nQuickstart\n----------\n\nIf you don't have ``pip`` installed, see the `pip install\nguide`_.\n\n.. _`pip install guide`: https://pip.pypa.io/en/latest/installing/\n\n.. code-block:: console\n\n    $ pip install ascl_net_scraper\n\n>>> import ascl_net_scraper\n",
    'author': 'Samuel Grayson',
    'author_email': 'sam+dev@samgrayson.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/charmoniumQ/ascl_net_scraper',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
