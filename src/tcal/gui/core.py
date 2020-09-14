import sys
import pandas as pd

from pathlib import Path
from collections import OrderedDict

from PyQt5.QtCore import Qt

from PyQt5 import (QtGui,
                   QtCore,
                   QtWidgets,
                   uic)

from PyQt5.QtWidgets import (QMessageBox,
                             QFileDialog,
                             QHeaderView)

from urllib.error import (URLError,
                          HTTPError)

from tcal.dbm import TCAL

from tcal.gui import DataModel
from tcal.gui import (AbtDialog,
                      HelpDialog,
                      WebDialog,
                      CredDialog)

from tcal.consts import *


main = Path.joinpath(DESIGNPATH, 'mwin.ui')

Ui_MainWin, QtBaseClass = uic.loadUiType(main)


class MainWindow(QtWidgets.QMainWindow,
                 Ui_MainWin):

    def __init__(self,
                 *args,
                 obj=None,
                 **kwargs):
        """
        """

        # Define and initialise the main window.

        super(MainWindow,
              self).__init__(*args,
                             **kwargs)

        self.setupUi(self)

        # Set icon.

        self.setWindowIcon(QtGui.QIcon(str(ICONPATH)))

        # Set logo.

        self.logo = QtGui.QPixmap(str(LOGOPATH))

        self.imglabel.setPixmap(self.logo)
        self.imglabel.setScaledContents(True)
        self.imglabel.resize(self.logo.width(),
                             self.logo.height())


        # Maximize the window.

        self.showMaximized()

        # Setup dialog boxes.

        self.abtdialog  = AbtDialog()
        self.helpdialog = HelpDialog()
        self.webdialog  = WebDialog()
        self.creddialog = CredDialog()

        # Setup the menubars.

        # `File` menubar.

        (self.actionUpdate
             .triggered
             .connect(self.updateTable))

        (self.actionSaveAs
             .triggered
             .connect(self.saveAs))

        # `About` menubar.

        (self.actionIntroTCAL
             .triggered
             .connect(self.abtdialog.exec_))

        (self.actionHelpTCAL
             .triggered
             .connect(self.helpdialog.exec_))

        (self.actionTCALWeb
             .triggered
             .connect(self.webdialog.exec_))

        (self.actionCredits
             .triggered
             .connect(self.creddialog.exec_))

        # Setup the data table.

        self.table = TCAL()

        self.df = self.table.load()
        self.dm = DataModel(self.df)

        self.tableView.setModel(self.dm)

        # Setup how the data table looks.

        (self.tableView
         .horizontalHeader()
         .setStretchLastSection(True))

        (self.tableView
         .horizontalHeader()
         .setSectionResizeMode(QHeaderView.Stretch))

        # Setup the search button.

        self.pushButton.clicked.connect(self.searchForm)

    def updateTable(self):

        """
        """

        try:

            self.table.update()

            DONE = ('You are done!\n'
                    '<b>TCAL</b> is ready to be used!')

            DONE = ''.join([PARASTART.format('center'),
                            DONE,
                            PARAEND])

            msgbox = QMessageBox()
            msgbox.setWindowTitle('Update finished!')
            msgbox.setText(DONE)
            msgbox.setStandardButtons(QMessageBox.Close)
            msgbox.exec_()

        except URLError:

            ERROR = ('Houston we have a problem...')

            ERROR = ''.join([PARASTART.format('center'),
                             ERROR,
                             PARAEND])

            INFO  = ('But do not worry, I got you. '
                     'The database will be loaded '
                     'OFFLINE!')

            INFO = ''.join([PARASTART.format('center'),
                            INFO,
                            PARAEND])

            msgbox = QMessageBox()

            msgbox.setText(ERROR)
            msgbox.setInformativeText(INFO)
            msgbox.setWindowTitle('NO INTERNET!')
            msgbox.setStandardButtons(QMessageBox.Close)
            msgbox.exec_()

        except HTTPError:

            ERROR = ('The uplink to TCAL is dead :(!')

            ERROR = ''.join([PARASTART.format('center'),
                             ERROR,
                             PARAEND])

            INFO  = ('This should not ideally be happening, '
                     'but if you have ended up here, just '
                     'update TCAL to get the latest uplink.')

            INFO = ''.join([PARASTART.format('center'),
                            INFO,
                            PARAEND])

            msgbox = QMessageBox()

            msgbox.setIcon(QMessageBox.Critical)
            msgbox.setText(ERROR)
            msgbox.setInformativeText(INFO)
            msgbox.setWindowTitle('Dead Uplink!')
            msgbox.setStandardButtons(QMessageBox.Close)
            msgbox.exec_()

    def searchForm(self):

        """
        """

        # TODO: Set comboBox from `position` column.
        # Get all possible options from it and make
        # comboBox accordingly.

        name      = self.lineEdit1.text()
        institute = self.lineEdit2.text()
        position  = self.comboBox.currentText()

        [results,
         header] = self.table.search(name,
                                     position,
                                     institute)

        if results:

            rdf = pd.DataFrame(results)
            rdf.columns = header

            rdm = DataModel(rdf)
            self.tableView.setModel(rdm)

        else:

            ERROR = ('Sorry :(! Could not find the '
                     'person you are looking for!')

            ERROR = ''.join([PARASTART.format('center'),
                             ERROR,
                             PARAEND])

            INFO  = ('You have either searched for '
                     'a non-existent person, or the '
                     'person you searched for is not '
                     'part of this list yet. If the '
                     'latter is the case, you can add '
                     'them! Find out how by going to '
                     'clicking on `Help TCAL` in the '
                     '`About` menu!')

            INFO = ''.join([PARASTART.format('center'),
                            INFO,
                            PARAEND])

            msgbox = QMessageBox()
            msgbox.setWindowTitle('Negative, Houston.')
            msgbox.setText(ERROR)
            msgbox.setStandardButtons(QMessageBox.Close)
            msgbox.setDefaultButton(QMessageBox.Close)
            msgbox.setInformativeText(INFO)
            msgbox.exec_()

    def saveAs(self):

        """
        """

        CAPTION  = 'Save TCAL!'
        DEFAULT  = 'tcal.csv'
        FILTER   = ('CSV Files (*.csv);;'
                    'Excel Files (*.xlsx);;'
                    'Markdown Files (*.md)')

        (filename, _) = QFileDialog.getSaveFileName(self,
                                                    CAPTION,
                                                    DEFAULT,
                                                    filter=FILTER)
        filename   = Path(filename)
        fileformat = filename.suffix

        self.table.save(filename,
                        fmt=fileformat)
