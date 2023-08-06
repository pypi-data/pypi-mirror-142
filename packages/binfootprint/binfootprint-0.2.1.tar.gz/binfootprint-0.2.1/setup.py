# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['binfootprint']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.22.0,<2.0.0', 'pytest>=7.0.0,<8.0.0', 'scipy>=1.8.0,<2.0.0']

setup_kwargs = {
    'name': 'binfootprint',
    'version': '0.2.1',
    'description': 'serielize python objetcs in a deterministic way',
    'long_description': "# binfootprint\n\n[![PyPI version](https://badge.fury.io/py/binfootprint.svg)](https://badge.fury.io/py/binfootprint)\n[![Build Status](https://travis-ci.org/cimatosa/binfootprint.svg?branch=master)](https://travis-ci.org/cimatosa/binfootprint)\n[![codecov](https://codecov.io/gh/cimatosa/binfootprint/branch/master/graph/badge.svg)](https://codecov.io/gh/cimatosa/binfootprint)\n\n## Description\n\nThis module intents to generate a binary representation of a python object\nwhere it is guaranteed that the same objects will result in the same binary\nrepresentation.\n    \nBy far not all python objects are supported. Here is the list of supported types\n        \n* special build-in constants: True, False, None\n* integer \n* float (64bit)\n* complex (128bit)\n\nas well as\n\n- tuples\n- lists\n- dictionaries\n- namedtuple\n\nof the above.\n\nAlso\n\n- np.ndarray\n\nare supported, however, as of changing details in the numpy implementation future\nversion may of numpy may break backwards compatibility.\n\nIn the current version (0.2.x) of binfootprint, a numpy array is serialized using\nthe (npy file format)[https://numpy.org/doc/stable/reference/generated/numpy.lib.format.html#module-numpy.lib.format].\n\n\nFor any nested combination of these objects it is also guaranteed that the\noriginal objects can be restored without any extra information.\n\nAdditionally\n\n- 'getstate' (objects that implement `__getstate__ and return a state that can be dumped as well)\n\ncan be dumped. To Restore these objects the load function needs a lookup given by the argument 'classes'\nwhich maps the objects class name (`obj.__class__.__name__`) to the actual class definition (the class object).\nOf course for these objects the `__setstate__` method needs to be implemented. \n\nNote: dumping older version is not supported anymore. If backwards compatibility is needed check out older\ncode from git. If needed converters should/will be written.\n\n## Installation\n\n### pip\ninstall the latest version using pip\n\n    pip install binfootprint\n\n### poetry\nUsing poetry allows you to include this package in your project as a dependency.\n\n### git\ncheck out the code from github\n\n    git clone https://github.com/cimatosa/binfootprint.git\n\n\n## Examples\n\nGenerating the binary footprint and reconstruction is done as follows:\n\n```python\nimport binfootprint as bf\n\ndata = ['hallo', 42]\nbin_key = bf.dump(data)\n\ndata_prime = bf.load(bin_key)\nprint(data_prime)\n```\n\nFurther any class that implements `__getstate__` may be used as a container as well. When reconstructing, the class needs to have the `__setstate__` method implemented.\nAdditionally the `bf.load` function required a mapping from the class name to the class object, like this:\n```python\n\nimport binfootprint as bf\n\nclass T(object):\n    def __init__(self, a):\n        self.a = a\n    def __getstate__(self):\n        return [self.a]\n    def __setstate__(self, state):\n        self.a = state[0]\n\nob = T(4)\nbin_ob = bf.dump(ob)\n\n# reconstruction\nclasses = {}\nclasses['T'] = T\nob_prime = bf.load(bin_ob, classes)\n\n```\n\n### Note on numpy ndarrays\n\nAs it has not been clarified/tested yet whether the buffer of the numpy ndarray is really unique also on different machines and architectures\nis it not assured that the binary footprint serves as a valid key.\n",
    'author': 'Richard Hartmann',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/cimatosa/binfootprint',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.10',
}


setup(**setup_kwargs)
