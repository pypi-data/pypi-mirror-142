# -*- coding: utf-8 -*-
#
# Licensed under the terms of the CECILL License
# (see codraft/__init__.py for details)

"""
Application launcher test 3

Create signal and image objects (with circles, rectangles, segments and markers),
then open CodraFT to show them.
"""

# pylint: disable=invalid-name  # Allows short reference names like x, y, ...

import numpy as np

from codraft.app import run
from codraft.core.model import create_image
from codraft.tests.app2_test import create_test_signal1
from codraft.tests.data import create_noisy_2d_gaussian, create_test_2d_data

SHOW = True  # Show test in GUI-based test launcher


# FIXME: Cross section tool works only on first image
def test():
    """Simple test"""
    shape = (2000, 2000)
    sig1 = create_test_signal1()
    ima1 = create_image("sin(x)+cos(y)", create_test_2d_data(shape, dtype=np.uint16))
    ima2 = create_image(
        "2D Gaussian",
        create_noisy_2d_gaussian(shape, dtype=np.uint16, x0=2.0, y0=3.0),
        circles=(
            ("Circle1", (100, 100, 400, 400)),
            ("Circle2", (150, 150, 350, 350)),
        ),
        rectangles=(("Rect1", (300, 200, 700, 700)),),
        segments=(("Segment", (100, 100, 400, 400)),),
        markers=(("Marker1", (500, 500)),),
    )
    objects = [sig1, ima1, ima2]
    run(objects=objects, size=(1200, 550))


if __name__ == "__main__":
    test()
