# -*- coding: utf-8 -*-
#
# Licensed under the terms of the CECILL License
# (see codraft/__init__.py for details)

"""
Application launcher test 1

Running application a few times in a row with different entry parameters.
"""

from codraft.app import run
from codraft.utils.tests import get_test_fnames

SHOW = True  # Show test in GUI-based test launcher


def test_app():
    """Testing CodraFT app launcher"""
    run(console=False)
    for fname in get_test_fnames("*.h5"):
        print(f"Opening: {fname}")
        run(console=False, h5file=fname)


if __name__ == "__main__":
    test_app()
