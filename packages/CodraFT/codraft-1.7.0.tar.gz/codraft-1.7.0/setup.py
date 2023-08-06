# -*- coding: utf-8 -*-
#
# Licensed under the terms of the CECILL License
# (see codraft/__init__.py for details)

"""
CodraFT
=======

CodraFT is a generic signal and image processing software based on Python scientific
libraries (such as NumPy, SciPy or OpenCV) and Qt graphical user interfaces (thanks to
guidata and guiqwt libraries).

CodraFT is Copyright © 2018 CEA-CODRA, Pierre Raybaut, and Licensed under the
terms of the CeCILL License v2.1.
"""

from distutils.core import setup

import setuptools  # analysis:ignore
from guidata.configtools import get_module_data_path
from guidata.utils import get_package_data, get_subpackages

from codraft import __version__ as version
from codraft.utils import dephash

LIBNAME = "codraft"

DESCRIPTION = "Signal and image processing software"
LONG_DESCRIPTION = """\
CodraFT: Signal and Image Processing Software
=============================================

.. image:: https://raw.githubusercontent.com/CODRA-Software/CodraFT/master/doc/images/dark_light_modes.png

CodraFT is a generic signal and image processing software based on Python scientific
libraries (such as NumPy, SciPy or OpenCV) and Qt graphical user interfaces (thanks to
guidata and guiqwt libraries).

CodraFT stands for "CODRA Filtering Tool".

Copyright © 2018-2022 CODRA, Pierre Raybaut
Copyright © 2009-2015 CEA, Pierre Raybaut
Licensed under the terms of the `CECILL License`_.

.. _changelog: https://github.com/CODRA-Software/CodraFT/blob/master/CHANGELOG.md
.. _CECILL License: https://github.com/CODRA-Software/CodraFT/blob/master/Licence_CeCILL_V2.1-en.txt
"""

KEYWORDS = ""
CLASSIFIERS = ["Topic :: Scientific/Engineering"]
if "beta" in version or "b" in version:
    CLASSIFIERS += ["Development Status :: 4 - Beta"]
elif "alpha" in version or "a" in version:
    CLASSIFIERS += ["Development Status :: 3 - Alpha"]
else:
    CLASSIFIERS += ["Development Status :: 5 - Production/Stable"]


dephash.create_dependencies_file(
    get_module_data_path("codraft", "data"), ("guidata", "guiqwt")
)

setup(
    name=LIBNAME,
    version=version,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=get_subpackages(LIBNAME),
    package_data={
        LIBNAME: get_package_data(
            LIBNAME, (".png", ".svg", ".mo", ".txt", ".h5", ".sig", ".csv")
        )
    },
    entry_points={"gui_scripts": ["codraft = codraft.app:run"]},
    author="Pierre Raybaut",
    author_email="pierre.raybaut@gmail.com",
    url="https://github.com/PierreRaybaut/%s" % LIBNAME,
    license="CeCILL V2",
    classifiers=CLASSIFIERS
    + [
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: OS Independent",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
