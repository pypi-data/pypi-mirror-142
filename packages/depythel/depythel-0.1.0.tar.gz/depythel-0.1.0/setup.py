# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['depythel_clt']

package_data = \
{'': ['*']}

install_requires = \
['beartype>=0.10.3,<0.11.0',
 'click>=8.0.3,<9.0.0',
 'depythel_api>=0.1.0,<0.2.0',
 'networkx>=2.6.3,<3.0.0',
 'pyvis>=0.1.9,<0.2.0',
 'rich-click>=1.2.1,<2.0.0',
 'rich>=11.0.0,<12.0.0']

entry_points = \
{'console_scripts': ['depythel = depythel_clt.main:depythel']}

setup_kwargs = {
    'name': 'depythel',
    'version': '0.1.0',
    'description': 'CLT for Interdependency Visualiser and Dependency Hell scrutiniser',
    'long_description': "About\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n|generate-image| |visualise-image|\n\n**depythel** is a series of open-source pure Python tools to help you manage dependencies in a variety of different projects.\n\nIt aims to provide a visual solution to your dependency woes, helping you to make informed judgements about how to\nmanage your project distribution.\n\n.. |generate-image| image:: https://raw.githubusercontent.com/harens/depythel/main/art/python-terminal-api.png\n   :height: 410\n   :alt: JSON output for Python 3.10 from MacPorts in iTerm2\n\n.. |visualise-image| image:: https://raw.githubusercontent.com/harens/depythel/main/art/visualise-macports-python.png\n   :height: 380\n   :alt: Visualising a dependency graph for Python 3.10 from MacPorts\n\nInstallation\n-----------------------------------------------------------------------------------------------------------------------\n\nPyPi\n***********************************************************************************************************************\n\n.. code-block:: console\n\n    $ pip install depythel\n\nLicense\n-----------------------------------------------------------------------------------------------------------------------\n\nThis project is `free software <https://www.gnu.org/philosophy/free-sw.en.html>`_, and it will always stay free.\n\nWe respect the `essential freedoms <https://www.gnu.org/philosophy/free-sw.en.html#four-freedoms>`_ of our users, and\nso both the API and the CLT are openly licensed under\n`GPL-3.0-or-later <https://github.com/harens/depythel/blob/master/LICENSE>`_.\n\nIn the same sense, the project's extensive documentation is freely licensed under the `GNU Free Documentation License\nv1.3 or later <https://www.gnu.org/licenses/fdl-1.3.html>`_.\n",
    'author': 'harens',
    'author_email': 'harensdeveloper@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
