import sys
from pathlib import Path

from PyQt5.QtCore import Qt

from PyQt5 import QtGui, QtCore, QtWidgets, uic

from tcal.consts import *


abtdialog = Path.joinpath(DESIGNPATH, "abtdialog.ui")
helpdialog = Path.joinpath(DESIGNPATH, "helpdialog.ui")
webdialog = Path.joinpath(DESIGNPATH, "webdialog.ui")
creddialog = Path.joinpath(DESIGNPATH, "creddialog.ui")

Ui_AbtDialog, QtBaseClass = uic.loadUiType(abtdialog)
Ui_HelpDialog, QtBaseClass = uic.loadUiType(helpdialog)
Ui_WebDialog, QtBaseClass = uic.loadUiType(webdialog)
Ui_CredDialog, QtBaseClass = uic.loadUiType(creddialog)


class AbtDialog(QtWidgets.QDialog, Ui_AbtDialog):
    def __init__(self, *args, obj=None, **kwargs):
        """"""

        super(AbtDialog, self).__init__(*args, **kwargs)

        self.setupUi(self)

        # Set logo.

        self.logo = QtGui.QPixmap(str(LOGOPATH))

        self.imglabel.setPixmap(self.logo)
        self.imglabel.setScaledContents(True)
        self.imglabel.resize(self.logo.width(), self.logo.height())


class HelpDialog(QtWidgets.QDialog, Ui_HelpDialog):
    def __init__(self, *args, obj=None, **kwargs):
        """"""

        super(HelpDialog, self).__init__(*args, **kwargs)

        self.setupUi(self)


class WebDialog(QtWidgets.QDialog, Ui_WebDialog):
    def __init__(self, *args, obj=None, **kwargs):
        """"""

        super(WebDialog, self).__init__(*args, **kwargs)

        self.setupUi(self)


class CredDialog(QtWidgets.QDialog, Ui_CredDialog):
    def __init__(self, *args, obj=None, **kwargs):
        """"""

        super(CredDialog, self).__init__(*args, **kwargs)

        self.setupUi(self)

        # Set logo.

        self.logo = QtGui.QPixmap(str(LOGOPATH))

        self.imglabel.setPixmap(self.logo)
        self.imglabel.setScaledContents(True)
        self.imglabel.resize(self.logo.width(), self.logo.height())
