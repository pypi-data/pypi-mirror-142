from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install
from subprocess import check_call
from pathlib import Path

import sys


class PostDevelopCommand(develop):
    """Post-installation for development mode."""

    def run(self):
        check_call(sys.path[0] + "/postinstall/develop.py")
        develop.run(self)


class PostInstallCommand(install):
    """Post-installation for installation mode."""

    def run(self):
        check_call(sys.path[0] + "/postinstall/install.py")
        install.run(self)

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(name='pynibs',
      version='0.1.4',
      description='A toolbox to prepare and analyse non-invasive brain stimulation experiments (NIBS).',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Konstantin Weise',
      author_email='kweise@cbs.mpg.de',
      keywords=['NIBS', 'non-invasive brain stimulation', 'TMS', 'FEM'],
      project_urls={'Home': 'https://gitlab.gwdg.de/tms-localization/pynibs',
                    'Docs': 'https://pynibs.readthedocs.io/',
                    'Download': 'https://pypi.org/project/pynibs/'},

      license='GPL3',
      packages=['pynibs',
                'pynibs.exp',
                'pynibs.models',
                'pynibs.util',
                'pynibs.pckg'],
      install_requires=['dill',
                        'h5py',
                        'lmfit',
                        'matplotlib',
                        'numpy',
                        'nibabel',
                        'pandas',
                        'pygpc',
                        'pyyaml',
                        'scipy',
                        'scikit-learn',
                        'packaging',
                        'lxml',
                        'tables',
                        'tqdm',
                        'pillow',
                        'fslpy',
                        'mkl',
                        'trimesh',
                        'fmm3dpy',
                        'tvb-gdist',
                        'ortools<=9.1.9490'],
      classifiers=['Development Status :: 3 - Alpha',
                   'Intended Audience :: Science/Research',
                   'Topic :: Scientific/Engineering',
                   'Topic :: Software Development :: Build Tools',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   'Programming Language :: Python :: 3.8',
                   'Programming Language :: Python :: 3.9', ],

      zip_safe=False)
