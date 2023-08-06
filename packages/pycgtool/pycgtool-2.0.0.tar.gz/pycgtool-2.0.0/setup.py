# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pycgtool', 'pycgtool.parsers']

package_data = \
{'': ['*'], 'pycgtool': ['data/*']}

install_requires = \
['astunparse==1.6.2',
 'mdtraj>=1.9.5,<2.0.0,!=1.9.6',
 'rich>=9.2.0,<10.0.0',
 'wheel>=0.35.1,<0.36.0']

extras_require = \
{':python_version < "3.7"': ['numpy>=1.19.1,<2.0.0'],
 ':python_version >= "3.7"': ['numpy>=1.20.0,<2.0.0'],
 'backmapping': ['mdplus>=0.0.5,<0.0.6'],
 'docs': ['Sphinx>=3.4.3,<4.0.0',
          'sphinx-autoapi>=1.5.1,<2.0.0',
          'sphinx-rtd-theme>=0.5.1,<0.6.0',
          'myst-parser>=0.13.5,<0.14.0']}

entry_points = \
{'console_scripts': ['pycgtool = pycgtool.__main__:main']}

setup_kwargs = {
    'name': 'pycgtool',
    'version': '2.0.0',
    'description': 'Generate coarse-grained molecular dynamics models from atomistic trajectories.',
    'long_description': "# PyCGTOOL\n\n[![License](https://img.shields.io/github/license/jag1g13/pycgtool.svg)](LICENSE)\n[![Python package](https://github.com/jag1g13/pycgtool/actions/workflows/python-package.yml/badge.svg?branch=dev)](https://github.com/jag1g13/pycgtool/actions)\n[![Documentation](https://readthedocs.org/projects/pycgtool/badge/?version=dev)](http://pycgtool.readthedocs.io/en/dev)\n[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.598143.svg)](https://doi.org/10.5281/zenodo.598143)\n[![PyPi Version](https://img.shields.io/pypi/v/pycgtool.svg)](https://pypi.python.org/pypi/pycgtool/)\n[![conda-forge Version](https://anaconda.org/conda-forge/pycgtool/badges/version.svg)](https://anaconda.org/conda-forge/pycgtool/badges/version.svg)\n\nGenerate coarse-grained molecular dynamics models from atomistic trajectories.\n\nPyCGTOOL is a tool to aid in parametrising coarse-grained (CG) molecular mechanics models of small molecules, for example for simulations using the popular MARTINI model.\nIt generates coarse-grained model parameters from atomistic simulation trajectories using a user-provided mapping.\nEquilibrium values and force constants of bonded terms are calculated by Boltzmann Inversion of bond distributions collected from the input trajectory.\n\nAlternatively map-only mode (behaving similarly to MARTINIZE) may be used to generate initial coordinates to use with existing CG topologies such as the MARTINI lipid models.\nFor instance, a pre-equilibrated atomistic membrane may be used to create starting coordinates for a CG membrane simulation.\n\nPyCGTOOL makes it quick and easy to test multiple variations in mapping and bond topology by making simple changes to the config files.\n\nIf you find PyCGTOOL useful, please cite our JCIM paper (https://doi.org/10.1021/acs.jcim.7b00096) and the code itself (https://doi.org/10.5281/zenodo.598143).\n\n```bibtex\n@article{Graham2017,\n   author = {James A. Graham and Jonathan W. Essex and Syma Khalid},\n   doi = {10.1021/acs.jcim.7b00096},\n   issn = {1549-9596},\n   issue = {4},\n   journal = {Journal of Chemical Information and Modeling},\n   month = {4},\n   pages = {650-656},\n   title = {PyCGTOOL: Automated Generation of Coarse-Grained Molecular Dynamics Models from Atomistic Trajectories},\n   volume = {57},\n   url = {https://pubs.acs.org/doi/10.1021/acs.jcim.7b00096},\n   year = {2017},\n}\n```\n\n## Install\n\nPyCGTOOL requires Python 3.6 or higher and may be installed using either `pip` or `conda`:\n```\npip install pycgtool\n```\n\n```\nconda install -c conda-forge pycgtool\n```\n\nAlternatively, you may download a pre-packaged version for your operating system from the [releases page](https://github.com/jag1g13/pycgtool/releases) on GitHub.\nThese pre-packaged versions include all dependencies and should be suitable in cases where you cannot install packages using one of the above methods.\n**Warning**: This installation method is not extensively tested - installing via `pip` or `conda` should be prefered in most cases.\n\n### MDTraj on macOS\n\nOn some versions macOS, with some versions of the Clang compiler, MDTraj may fail to load GROMACS XTC simulation trajectories.\nIf you encounter this issue, please make sure you have the latest version of MDTraj installed.\n\nFor more information see [MDTraj/#1572](https://github.com/mdtraj/mdtraj/issues/1572).\n\n## Usage\n\nInput to PyCGTOOL is an atomistic simulation trajectory in the form of a topology (e.g. PDB, GRO, etc.) and a trajectory file (e.g. XTC, DCD, etc.), along with two custom files which describe the CG model to be generated: mapping (`.map`) and bonding (`.bnd`).\nThese files provide the atomistic-to-CG mapping and bonded topology respectively and use a format similar to GROMACS `.itp` files.\nTopology and trajectory files are processed using [MDTraj](https://www.mdtraj.org) so most common formats are accepted.\n\nExample mapping and bond files are present in the [test/data](https://github.com/jag1g13/pycgtool/tree/main/test/data) directory.\nThe format of these files is described fully in the [documentation page on file formats](https://pycgtool.readthedocs.io/en/dev/file-formats.html).\n\nFor more information, see [the tutorial](https://pycgtool.readthedocs.io/en/main/tutorial.html).\nIt is important to perform validation of any new parameter set - a brief example is present at the end of the tutorial.\n\nFor a full list of options, see the [documentation](https://pycgtool.readthedocs.io/en/main/index.html) or use:\n```\npycgtool -h\n```\n\n### Generate a Model\n\nTo generate a CG model from an atomistic simulation:\n```\npycgtool <topology file> <trajectory file> -m <MAP file> -b <BND file>\n```\n\n### Map Only\n\nTo use PyCGTOOL to convert a set of atomistic simulation coordinates to CG coordinates:\n```\npycgtool <topology file> -m <MAP file>\n```\n\nOr to convert a complete simulation trajectory:\n```\npycgtool <topology file> <trajectory file> -m <MAP file>\n```\n\n## Maintainers\n\nJames Graham ([@jag1g13](https://github.com/jag1g13))\n\n## Contributing\n\nIf you experience problems using PyCGTOOL or wish to see a new feature added please [open an issue](https://github.com/jag1g13/pycgtool/issues/new).\n\nTo help develop PyCGTOOL, you can create a fork of this repository, clone your fork and install PyCGTOOL in development mode using [Poetry](https://python-poetry.org/):\n```\npoetry install\n```\n\nThis will result in an editable mode install (similar to `pip install -e .`) along with all the necessary runtime and development dependencies.\nTesting and linting is handled by [Tox](https://tox.readthedocs.io/en/latest/) - use `tox` to run the full test suite and linter as they are configured in the Continuous Integration pipeline.\n\nWhen you're ready for your work to be merged, please submit a Pull Request.\n\n## License\n\n[GPL-3.0](LICENSE) © James Graham, University of Southampton\n",
    'author': 'James Graham',
    'author_email': 'j.graham@soton.ac.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jag1g13/pycgtool',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
