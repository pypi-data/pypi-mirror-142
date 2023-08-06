# -*- coding: utf-8 -*-
#
# Licensed under the terms of the CECILL License
# (see codraft/__init__.py for details)

"""
CodraFT Qt utilities
"""

import functools
import os
import os.path as osp
import sys
import traceback
from contextlib import contextmanager

import guidata
from guiqwt import tools as gqtools
from guiqwt.builder import make
from guiqwt.plot import ImageDialog
from qtpy.QtCore import Qt
from qtpy.QtGui import QCursor
from qtpy.QtWidgets import QApplication, QMessageBox, QProgressDialog

from codraft.config import APP_NAME, _


@contextmanager
def qt_app_context():
    """Context manager handling Qt application creation and persistance"""
    try:
        app = guidata.qapplication()
        yield app
    finally:
        pass


def create_progress_bar(parent, label, max_):
    """Create modal progress bar"""
    prog = QProgressDialog(label, _("Cancel"), 0, max_, parent, Qt.Popup)
    prog.setWindowModality(Qt.WindowModal)
    prog.show()
    return prog


def qt_handle_error_message(widget, message):
    """Handles application (QWidget) error message"""
    traceback.print_exc()
    txt = str(message)
    msglines = txt.splitlines()
    if len(msglines) > 10:
        txt = os.linesep.join(msglines[:10] + ["..."])
    title = widget.window().objectName()
    QMessageBox.critical(widget, title, _("Error:") + f"\n{txt}")


def qt_try_except(message=None):
    """Try...except Qt widget method decorator"""

    def qt_try_except_decorator(func):
        """Try...except Qt widget method decorator"""

        @functools.wraps(func)
        def method_wrapper(*args, **kwargs):
            """Decorator wrapper function"""
            self = args[0]
            if message is not None:
                self.SIG_STATUS_MESSAGE.emit(message)
                QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
                self.repaint()
            output = None
            try:
                output = func(*args, **kwargs)
            except Exception as msg:  # pylint: disable=broad-except
                qt_handle_error_message(self.parent(), msg)
            finally:
                self.SIG_STATUS_MESSAGE.emit("")
                QApplication.restoreOverrideCursor()
            return output

        return method_wrapper

    return qt_try_except_decorator


@contextmanager
def qt_try_opening_file(widget, filename):
    """Try and open file"""
    try:
        yield filename
    except Exception as msg:  # pylint: disable=broad-except
        traceback.print_exc()
        QMessageBox.critical(
            widget,
            APP_NAME,
            (_("%s could not be opened:") % osp.basename(filename)) + "\n" + str(msg),
        )
    finally:
        pass


def create_image_window(title=None, show_itemlist=True, show_contrast=True, tools=None):
    """Create Image Dialog"""
    if title is None:
        script_name = osp.basename(sys.argv[0])
        title = f'{_("Test dialog")} `{script_name}`'
    win = ImageDialog(
        edit=False,
        toolbar=True,
        wintitle=title,
        options=dict(show_itemlist=show_itemlist, show_contrast=show_contrast),
    )
    if tools is None:
        tools = (
            gqtools.LabelTool,
            gqtools.VCursorTool,
            gqtools.HCursorTool,
            gqtools.XCursorTool,
            gqtools.AnnotatedRectangleTool,
            gqtools.AnnotatedCircleTool,
            gqtools.AnnotatedEllipseTool,
            gqtools.AnnotatedSegmentTool,
            gqtools.AnnotatedPointTool,
        )
    for toolklass in tools:
        win.add_tool(toolklass, switch_to_default_tool=True)
    return win


def view_image_items(
    items, title=None, show_itemlist=True, show_contrast=True, tools=None
):
    """Create an image dialog and show items"""
    win = create_image_window(
        title=title,
        show_itemlist=show_itemlist,
        show_contrast=show_contrast,
        tools=tools,
    )
    plot = win.get_plot()
    for item in items:
        plot.add_item(item)
    win.exec_()


def view_images(
    data_or_datalist, title=None, show_itemlist=True, show_contrast=True, tools=None
):
    """Create an image dialog and show images"""
    if isinstance(data_or_datalist, (tuple, list)):
        datalist = data_or_datalist
    else:
        datalist = [data_or_datalist]
    items = []
    for data in datalist:
        item = make.image(data, interpolation="nearest", eliminate_outliers=0.1)
        items.append(item)
    view_image_items(
        items,
        title=title,
        show_itemlist=show_itemlist,
        show_contrast=show_contrast,
        tools=tools,
    )
