# -*- coding: utf-8 -*-
#
# Licensed under the terms of the CECILL License
# (see codraft/__init__.py for details)

"""
CodraFT
=======

CodraFT is a generic signal and image processing software based on Python scientific
libraries (such as NumPy, SciPy or OpenCV) and Qt graphical user interfaces (thanks to
`guidata`_ and `guiqwt`_ libraries).

.. _guidata: https://pypi.python.org/pypi/guidata
.. _guiqwt: https://pypi.python.org/pypi/guiqwt

.. image:: images/panorama.png

External resources:

    * Python Package Index: `PyPI`_
    * Bug reports and feature requests: `GitHub`_

.. _PyPI: https://pypi.python.org/pypi/codraft
.. _GitHub: https://github.com/CODRA-Software/CodraFT

Copyrights and licensing:

* Copyright © 2018 `CEA`_ - `CODRA`_, Pierre Raybaut ;
* Licensed under the terms of the `CECILL License`_.

.. _CEA: http://www.cea.fr
.. _CODRA: https://codra.net/
.. _CECILL License: http://www.cecill.info/licences/Licence_CeCILL_V2.1-en.html
"""

__version__ = "1.7.1"

import codraft.patch  # analysis:ignore

# Dear (Debian, RPM, ...) package makers, please feel free to customize the
# following path to module's data (images) and translations:
DATAPATH = LOCALEPATH = ""

#    Copyright © 2009-2010 CEA
#    Pierre Raybaut
#    Licensed under the terms of the CECILL License
#    (see included file `Licence_CeCILL_V2.1-en.txt`)
