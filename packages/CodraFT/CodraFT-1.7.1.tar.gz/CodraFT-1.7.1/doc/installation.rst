Installation
============

Dependencies
------------

CodraFT requirements are the following *(note that the installer package already
include all those required libraries as well as Python itself)*:

+--------------------+-------------------+----------------------------------------+
| Name               | Version (minimal) | Comment                                |
+====================+===================+========================================+
| Python language    | 3.7               | Python 3.8 is the reference            |
+--------------------+-------------------+----------------------------------------+
| PyQt               | 5.15              | Should work with PySide6/PyQt6 as well |
+--------------------+-------------------+----------------------------------------+
| QtPy               | 1.9               |                                        |
+--------------------+-------------------+----------------------------------------+
| guidata            | 2.0.4             |                                        |
+--------------------+-------------------+----------------------------------------+
| guiqwt             | 4.0.2             |                                        |
+--------------------+-------------------+----------------------------------------+
| NumPy              | 1.21              |                                        |
+--------------------+-------------------+----------------------------------------+
| SciPy              | 1.7               |                                        |
+--------------------+-------------------+----------------------------------------+

Installation
------------

From the installer:
^^^^^^^^^^^^^^^^^^^

CodraFT is available as a stand-alone application, which does not require any Python
distribution to be installed. Just run the installer and you're good to go!

The installer package is available in the `Releases`_ section.

.. _Releases: https://github.com/CODRA-Software/CodraFT/releases


From the source package::
^^^^^^^^^^^^^^^^^^^^^^^^^

    $ python setup.py install

From the wheel package::
^^^^^^^^^^^^^^^^^^^^^^^^

    $ pip install --upgrade --no-deps codraft-1.7.0-py2.py3-none-any.whl
