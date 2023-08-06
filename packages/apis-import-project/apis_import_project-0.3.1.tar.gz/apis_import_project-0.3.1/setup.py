# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['apis_import_project', 'apis_import_project.migrations']

package_data = \
{'': ['*'],
 'apis_import_project': ['static/apis_import_project/css/*',
                         'static/apis_import_project/js/*',
                         'templates/element_templates/*',
                         'templates/pages/*',
                         'templates/section_templates/*']}

install_requires = \
['apis-bibsonomy>=0.3,<0.4',
 'apis-core>=0.17,<0.18',
 'apis-highlighter>=0.9,<0.10']

setup_kwargs = {
    'name': 'apis-import-project',
    'version': '0.3.1',
    'description': 'Generic Django-App for APIS-instances to support importing new data manually with a streamlined workflow and some automation.',
    'long_description': None,
    'author': 'Gregor Pirgie',
    'author_email': 'gregor.pirgie@oeaw.ac.at',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.9',
}


setup(**setup_kwargs)
