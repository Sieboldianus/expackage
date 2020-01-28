# -*- coding: utf-8 -*-


"""
expackage command line interface
"""

from __future__ import absolute_import
# delay evaluation of annotations at runtime (PEP 563)
from __future__ import annotations
from multiprocessing import freeze_support


import sys
import time
import logging

from expackage.expackage import ExamplePackage


def main():
    """Main expackage method for direct execution of package.
    """
    log = logging.getLogger("expackage")
    log.info(
        "########## "
        "Running expackage in cli-mode "
        "##########")

    # initialize expackage
    expackage = ExamplePackage()
    # run cluster ExamplePackage
    expackage.cluster_example()
    # exit after any input
    input("Press any key to exit...")
    sys.exit(0)


if __name__ == "__main__":
    # multiprocessing freeze_support
    # see:
    # https://docs.python.org/3/library/multiprocessing.html#multiprocessing.freeze_support
    freeze_support()
    main()
