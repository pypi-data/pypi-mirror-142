# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['chemspectranslator']

package_data = \
{'': ['*'], 'chemspectranslator': ['data/*']}

install_requires = \
['numpy>=1.2']

setup_kwargs = {
    'name': 'chemspectranslator',
    'version': '1.1.0',
    'description': 'Universal translator for chemical species',
    'long_description': '# chemspectranslator\n\n``chemspectranslator`` is a universal translator for chemical mechanism species\n\nBased on the master spreadsheet originally conceived by Bill Carter (UC Riverside),\nand adapted by Christoph Knote (Uni Augsburg) / Louisa Emmons (NCAR).\n\n## Documentation\n\nmaintained at https://mbees.med.uni-augsburg.de\n\n## Changelog\n\n### 1.1.0 (2021-03-14)\n\n- Update build system, remove Google online version\n\n### 1.0.0 (2017-12-19)\n\n- Peer-reviewed version to be published in Knote et al., GMD\n\n### 0.1.0 (2017-08-12)\n\n- Initial release\n',
    'author': 'Christoph Knote',
    'author_email': 'christoph.knote@med.uni-augsburg.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://mbees.med.uni-augsburg.de/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3,<4',
}


setup(**setup_kwargs)
