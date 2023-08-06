# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['depythel', 'depythel.repository']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'depythel-api',
    'version': '0.1.0',
    'description': 'Library for Interdependency Visualiser and Dependency Hell scrutiniser',
    'long_description': "About\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n.. image:: https://raw.githubusercontent.com/harens/depythel/main/art/generate-macports-python.png\n  :width: 600\n  :alt: Generate dependencies of gping from MacPorts\n\n**depythel API** is an open-source pure Python API tool to help manage dependencies in a variety of different projects.\n\nUse this tool if you like the standard depythel CLT, but don't want the extra baggage that comes with a command line tool.\n\nBenefits\n-----------------------------------------------------------------------------------------------------------------------\n\n- 🎉 No third party dependencies\n- 🐍 Compatible with all `supported Python versions <https://endoflife.date/python>`_ (3.7+)\n- 👀 `PEP 561 compatible <https://www.python.org/dev/peps/pep-0561>`_, with built in support for type checking\n\nInstall\n-----------------------------------------------------------------------------------------------------------------------\n\n.. code-block:: console\n\n    $ pip install depythel-api\n\nLicense\n-----------------------------------------------------------------------------------------------------------------------\n\nThe depythel API is `free software <https://www.gnu.org/philosophy/free-sw.en.html>`_, and it will always stay free.\n\nWe respect the `essential freedoms <https://www.gnu.org/philosophy/free-sw.en.html#four-freedoms>`_ of our users, and\nso depythel is openly licensed under `GPL-3.0-or-later <https://github.com/harens/depythel/blob/master/LICENSE>`_.\n",
    'author': 'harens',
    'author_email': 'harensdeveloper@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
