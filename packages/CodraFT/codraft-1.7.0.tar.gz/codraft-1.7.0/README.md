# CodraFT - [CODRA](https://codra.net/)'s Filtering Tool

![CodraFT - CODRA's Filtering Tool](https://raw.githubusercontent.com/CODRA-Software/CodraFT/master/doc/images/dark_light_modes.png)

## Overview

CodraFT is a generic signal and image processing software based on Python scientific
libraries (such as NumPy, SciPy or OpenCV) and Qt graphical user interfaces (thanks to
[guidata](https://pypi.python.org/pypi/guidata) and [guiqwt](https://pypi.python.org/pypi/guiqwt) libraries).

Copyrights and licensing:

* Copyright © 2018 [CEA](http://www.cea.fr)-[CODRA](https://codra.net/), Pierre Raybaut
* Licensed under the terms of the CECILL License. See ``Licence_CeCILL_V2.1-en.txt``.

## Installation

### From the installer

CodraFT is available as a stand-alone application, which does not require any Python
distribution to be installed. Just run the installer and you're good to go!

The installer package is available in the [Releases](https://github.com/CODRA-Software/CodraFT/releases) section.

### From the source package

```bash
python setup.py install
```

## Dependencies

### Requirements

* Python 3.7+ (reference is Python 3.8)
* [PyQt5](https://pypi.python.org/pypi/PyQt5) 5.15+ (Python Qt bindings)
* [guidata](https://pypi.python.org/pypi/guidata) 2.0+ (set of tools for automatic GUI generation)
* [guiqwt](https://pypi.python.org/pypi/guiqwt) 4.0+ (set of tools for curve and image plotting based on guidata)

### Other optional modules

* [OpenCV](https://pypi.org/project/opencv-python/) for some image processing features
