# -*- coding: utf-8 -*-
#
# Licensed under the terms of the CECILL License
# (see codraft/__init__.py for details)

"""
Application launcher test 1

Create signal objects and open CodraFT to show them.
"""

# pylint: disable=invalid-name  # Allows short reference names like x, y, ...

import numpy as np

from codraft.app import run
from codraft.core.computation import fit
from codraft.core.model import create_signal
from codraft.utils.tests import get_test_fnames

SHOW = True  # Show test in GUI-based test launcher


def create_test_signal1():
    """Create test signal (Paracetamol molecule spectrum)"""
    data = np.loadtxt(get_test_fnames("paracetamol.txt")[0], delimiter=",")
    obj = create_signal("Paracetamol")
    obj.xydata = data.T
    return obj


def create_test_signal2():
    """Create test signal (Gaussian curve)"""
    obj = create_signal("Gaussienne")
    x = np.linspace(-10, 10)
    y = fit.GaussianModel.func(x, 500.0, 2.0, 0.0, 0.0)
    obj.set_xydata(x, y)
    return obj


if __name__ == "__main__":
    run(objects=[create_test_signal1(), create_test_signal2()])
