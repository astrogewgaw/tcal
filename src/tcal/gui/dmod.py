from PyQt5.QtCore import Qt

from PyQt5 import QtGui, QtCore


class DataModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        """"""

        super(DataModel, self).__init__()
        self._data = data

    def data(self, index, role):

        if role == Qt.DisplayRole:

            value = self._data.iloc[index.row(), index.column()]
            return str(value)

        if role == Qt.BackgroundRole:

            value = self._data.iloc[index.row(), index.column()]

            if not value:
                return QtGui.QColor("#d63447")

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):

        if role == Qt.DisplayRole:

            if orientation == Qt.Horizontal:

                return str(self._data.columns[section])

            if orientation == Qt.Vertical:

                return str(self._data.index[section] + 1)
