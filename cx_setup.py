# -*- coding: utf-8 -*-

"""Setup config for cx_freeze (build)

This cx_freeze setup is configured to build
self executable folder on Windows for Windows
users who cannot use package manager. The resulting
expackage.exe can be directly run.

Has been tested with conda environment (Windows 10)

Prerequisites:
    - install cx_freeze
    - install [mkl-service][1]

Run build with:
    python cx_setup.py build

[1]: e.g. conda install mkl-service -c conda-forge
"""

import glob
import json
import os
import sys
from pathlib import Path

import opcode

from cx_Freeze import Executable, setup

PYTHON_VERSION = f'{sys.version_info.major}.{sys.version_info.minor}'
print(f"Running cx_freeze for Python {PYTHON_VERSION}")

# Derive Package Paths Dynamically
PYTHON_INSTALL_DIR = os.path.dirname(
    os.path.dirname(os.__file__))


# opcode is not a virtualenv module,
# so we can use it to find the stdlib; this is the same
# trick used by distutils itself it installs itself into the virtualenv
DISTUTILS_PATH = os.path.join(os.path.dirname(opcode.__file__), 'distutils')

# Dependencies are automatically detected,
# but it might need fine tuning.
INCLUDES_MOD = [
    'numpy.lib.format',
    'numpy.core._methods',
    'scipy.sparse.csgraph',
    'scipy.sparse.csgraph._validation',
    'numpy',
    'scipy._distributor_init',
]

# include all mkl files
# https://stackoverflow.com/questions/54337644/cannot-load-mkl-intel-thread-dll-on-python-executable
# https://github.com/anthony-tuininga/cx_Freeze/issues/214
# get json file that has mkl files list (exclude the "service" file)
MKL_FILES_JSON_FILE = glob.glob(
    os.path.join(PYTHON_INSTALL_DIR, "conda-meta", "mkl-[!service]*.json"))[0]
with open(MKL_FILES_JSON_FILE) as file:
    MKL_FILES_JSON_DATA = json.load(file)
# get the list of files from the json data file
NUMPY_MKL_DLLS = MKL_FILES_JSON_DATA["files"]
# get the full path of these files
NUMPY_DLLS_FULLPATH = list(map(lambda currPath: os.path.join(
    PYTHON_INSTALL_DIR, currPath), NUMPY_MKL_DLLS))
# add libiomp5md.dll, as it is also needed for Intel MKL
NUMPY_DLLS_FULLPATH.append(
    os.path.join(PYTHON_INSTALL_DIR, 'Library', 'bin', 'libiomp5md.dll')
)

# files that need manual attention
INCLUDE_FOLDERS_FILES = [
    (DISTUTILS_PATH, 'distutils'),
    'README.md',
    'points.pkl',
] + NUMPY_DLLS_FULLPATH

PACKAGES_MOD = ["hdbscan", "multiprocessing"]
EXCLUDES_MOD = [
    'scipy.spatial.cKDTree',
    "distutils",
    'sklearn.externals.joblib']


# GUI applications require a different base on Windows
# (the default is for a console application).
BASE = None

EXECUTABLES = [
    Executable('expackage/__main__.py',
               base=BASE,
               targetName="expackage.exe")
]

VERSION = "0.0.1"

BUILD_NAME = f'expackage-{VERSION}-win-amd64-{PYTHON_VERSION}'

setup(name="expackage",
      version=VERSION,
      description="ExamplePackage: demonstrates "
      "joblib/loky multiprocessing issue in frozen executable",
      options={
          'build_exe': {
              'includes': INCLUDES_MOD,
              'include_files': INCLUDE_FOLDERS_FILES,
              'packages': PACKAGES_MOD,
              'excludes': EXCLUDES_MOD,
              'optimize': 0,
              'build_exe': (
                  Path.cwd() / 'build' / BUILD_NAME)
          }
      },
      executables=EXECUTABLES)


# open issue Windows:
# after build, rename
# \lib\multiprocessing\Pool.pyc
# to pool.pyc
# see:
# https://github.com/anthony-tuininga/cx_Freeze/issues/353
BUILD_PATH_POOL = (
    Path.cwd() / 'build' / BUILD_NAME /
    'lib' / 'multiprocessing')
Path(BUILD_PATH_POOL / 'Pool.pyc').rename(
    BUILD_PATH_POOL / 'pool.pyc')
