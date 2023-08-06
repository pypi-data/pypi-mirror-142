# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['boxmox']

package_data = \
{'': ['*']}

install_requires = \
['f90nml>=1.3', 'numpy>=1.2', 'pyparsing>=3']

setup_kwargs = {
    'name': 'boxmox',
    'version': '1.2.5',
    'description': 'BOXMOX python interface',
    'long_description': "# BOXMOX\n\n``boxmox`` is the Python wrapper for the chemical box model BOXMOX (a standalone\nC/Fortran executable).\n\n## Installation\n\n### BOXMOX model needs to be installed\n\nThe BOXMOX chemical box model needs to be installed and the ``KPP_HOME`` environment variable has to be set. Download and instructions are our website at https://mbees.med.uni-augsburg.de/boxmodeling.\n\n### Environment variable needs to be set\n\nAdditionally, ``boxmox`` needs a path to write temporary model results\nto, given through the environment variable ``BOXMOX_WORK_PATH``. This directory needs to be accessible and writeable by the user. Set it in your environment, e.g., through:\n\n```\nexport BOXMOX_WORK_PATH=/where/you/want/boxmox/to/write/stuff/to/\n```\n\nRemember to close the shell and log in again for these changes to take effect.\n\n## Contributing\n\nWe are looking forward to receiving your [new issue report](https://mbees.med.uni-augsburg.de/gitlab/mbees/boxmox_pypackage/-/issues/new).\n\nIf you'd like to contribute source code directly, please [create a fork](https://mbees.med.uni-augsburg.de/gitlab/mbees/boxmox_pypackage),\nmake your changes and then [submit a merge request](https://mbees.med.uni-augsburg.de/gitlab/mbees/boxmox_pypackage/-/merge_requests/new) to the original project.\n\n# Changelog\n\n## 1.2.5 (2022-03-14)\n\n- Release on PyPI\n\n## 1.2.0 (2022-03-08) (not released)\n\n- Updates to be compatible with BOXMOX 1.8\n\n## 1.1.0 (2020-09-16)\n\n- Python 3 compatible \n\n## 1.0.0 (2017-12-19)\n\n- Peer-reviewed version to be published in Knote et al., GMD\n\n## 0.1.0 (2017-08-12)\n\n- Initial release\n",
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
