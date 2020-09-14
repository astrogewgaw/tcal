import os
import sys
import contextlib

from PyQt5 import QtWidgets
from tcal.gui import MainWindow


def main():

    """
    Console script entry point for TCAL.
    """

    # Start the Qt Application.

    app  = QtWidgets.QApplication(sys.argv)

    # Initialise the main window.

    mwin = MainWindow()

    # Display the main window and
    # start the execution loop for
    # the application.

    mwin.show()
    app.exec_()

if __name__=='__main__':
    main()
