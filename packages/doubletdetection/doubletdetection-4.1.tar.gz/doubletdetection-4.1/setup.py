# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['doubletdetection']

package_data = \
{'': ['*']}

install_requires = \
['anndata>=0.6',
 'ipywidgets',
 'leidenalg',
 'louvain',
 'matplotlib>=3.1',
 'numpy>=1.14.2',
 'pandas>=0.22.0',
 'phenograph',
 'scanpy>1.4.4',
 'scipy>=1.0.1',
 'tqdm']

extras_require = \
{'dev': ['black>=20.8b1', 'flake8>=3.7.7', 'pre-commit>=2.7.1', 'pytest>=4.4'],
 'docs': ['furo',
          'myst-parser',
          'nbsphinx',
          'nbsphinx-link',
          'sphinx>=4.1,<4.4',
          'sphinx-autodoc-typehints']}

setup_kwargs = {
    'name': 'doubletdetection',
    'version': '4.1',
    'description': 'Method to detect and enable removal of doublets from single-cell RNA-sequencing.',
    'long_description': "# DoubletDetection\n\n[![DOI](https://zenodo.org/badge/86256007.svg)](https://zenodo.org/badge/latestdoi/86256007)\n[![Documentation Status](https://readthedocs.org/projects/doubletdetection/badge/?version=latest)](https://doubletdetection.readthedocs.io/en/latest/?badge=latest)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)\n![Build Status](https://github.com/JonathanShor/DoubletDetection/workflows/doubletdetection/badge.svg)\n\nDoubletDetection is a Python3 package to detect doublets (technical errors) in single-cell RNA-seq count matrices.\n\n## Installing DoubletDetection\n\nInstall from PyPI\n\n```bash\npip install doubletdetection\n```\n\nInstall from source\n\n```bash\ngit clone https://github.com/JonathanShor/DoubletDetection.git\ncd DoubletDetection\npip3 install .\n```\n\nIf you are using `pipenv` as your virtual environment, it may struggle installing from the setup.py due to our custom Phenograph requirement.\nIf so, try the following in the cloned repo:\n\n```bash\npipenv run pip3 install .\n```\n\n## Running DoubletDetection\n\nTo run basic doublet classification:\n\n```Python\nimport doubletdetection\nclf = doubletdetection.BoostClassifier()\n# raw_counts is a cells by genes count matrix\nlabels = clf.fit(raw_counts).predict()\n# higher means more likely to be doublet\nscores = clf.doublet_score()\n```\n\n- `raw_counts` is a scRNA-seq count matrix (cells by genes), and is array-like\n- `labels` is a 1-dimensional numpy ndarray with the value 1 representing a detected doublet, 0 a singlet, and `np.nan` an ambiguous cell.\n- `scores` is a 1-dimensional numpy ndarray representing a score for how likely a cell is to be a doublet. The score is used to create the labels.\n\nThe classifier works best when\n\n- There are several cell types present in the data\n- It is applied individually to each run in an aggregated count matrix\n\nIn `v2.5` we have added a new experimental clustering method (`scanpy`'s Louvain clustering) that is much faster than phenograph. We are still validating results from this new clustering. Please see the notebook below for an example of using this new feature.\n\n## Tutorial\n\nSee our [tutorial](https://doubletdetection.readthedocs.io/en/latest/tutorial.html) for an example on 10k PBMCs from 10x Genomics.\n\n## Obtaining data\n\nData can be downloaded from the [10x website](https://support.10xgenomics.com/single-cell/datasets).\n\n## Credits and citations\n\nGayoso, Adam, Shor, Jonathan, Carr, Ambrose J., Sharma, Roshan, Pe'er, Dana (2020, December 18). DoubletDetection (Version v3.0). Zenodo. http://doi.org/10.5281/zenodo.2678041\n\nWe also thank the participants of the 1st Human Cell Atlas Jamboree, Chun J. Ye for providing data useful in developing this method, and Itsik Pe'er for providing guidance in early development as part of the Computational genomics class at Columbia University.\n\nThis project is licensed under the terms of the MIT license.\n",
    'author': 'Adam Gayoso',
    'author_email': 'adamgayoso@berkeley.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/JonathanShor/DoubletDetection',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6.1,<4.0',
}


setup(**setup_kwargs)
