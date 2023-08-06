# coding: utf-8
# /*##########################################################################
#
# Copyright (c) 2016-2017 European Synchrotron Radiation Facility
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# ###########################################################################*/


__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "30/03/2021"

import logging
import os

from silx.gui import qt
from i3dxrd.data_selection import load_process_data
from silx.gui.dialog.DataFileDialog import DataFileDialog

_logger = logging.getLogger(__file__)


class DatasetSelectionWidget(qt.QTabWidget):
    """
    Widget that creates a dataset from a list of files or from a single filename.
    It lets the user add the first filename of a directory of files, or to
    upload manually each of the files to be read.
    If both options are filled up, only the files in the list of filenames
    are read.
    """

    sigProgressChanged = qt.Signal(int)

    def __init__(self, parent=None):
        qt.QMainWindow.__init__(self, parent)

        self._isHdf5Checkbox = qt.QCheckBox("Hdf5 file")

        # Raw data
        self._rawFilenameData = FilenameSelectionWidget(
            "Load data first file", parent=self
        )
        self._rawFilesData = FilesSelectionWidget(parent=self)
        self._inDiskCB = qt.QCheckBox("Use data from disk")
        rawData = qt.QWidget(self)
        rawData.setLayout(qt.QVBoxLayout())
        rawData.layout().addWidget(self._isHdf5Checkbox)
        rawData.layout().addWidget(self._rawFilenameData)
        rawData.layout().addWidget(self._rawFilesData)
        rawData.layout().addWidget(self._inDiskCB)
        self._inDiskCB.setChecked(True)
        self.addTab(rawData, "raw data")

        self._darkFilename = FilenameSelectionWidget(
            "Load dark file", parent=self, fileMode=qt.QFileDialog.ExistingFile
        )
        self._floodFilename = FilenameSelectionWidget(
            "Load flood file", parent=self, fileMode=qt.QFileDialog.ExistingFile
        )
        self._splineFilename = FilenameSelectionWidget(
            "Load spline file", parent=self, fileMode=qt.QFileDialog.ExistingFile
        )

        peaksData = qt.QWidget(self)
        peaksData.setLayout(qt.QVBoxLayout())
        peaksData.layout().addWidget(self._darkFilename)
        peaksData.layout().addWidget(self._floodFilename)
        peaksData.layout().addWidget(self._splineFilename)

        self.addTab(peaksData, "peak search data")

        self._inDisk = True
        self._isH5 = False

        self._dataset = None
        self.indices = None

        self.getRawFilenames = self._rawFilesData.getFiles
        self.getRawFilename = self._rawFilenameData.getFilename
        self.getDarkFilename = self._darkFilename.getFilename
        self.getFloodFilename = self._floodFilename.getFilename
        self.getSplineFilename = self._splineFilename.getFilename
        self.setRawFilenames = self._rawFilesData.setFiles
        self.setRawFilename = self._rawFilenameData.setFilename
        self.setDarkFilename = self._darkFilename.setFilename
        self.setFloodFilename = self._floodFilename.setFilename
        self.setSplineFilename = self._splineFilename.setFilename

        self._inDiskCB.stateChanged.connect(self.__inDisk)
        self._isHdf5Checkbox.stateChanged.connect(self._changeDataType)

    def _changeDataType(self, state):

        self._isH5 = bool(state)
        self._rawFilenameData.isHDF5(state)
        if state:
            self._rawFilesData.hide()
        else:
            self._rawFilesData.show()

    def updateProgress(self, progress):
        self.sigProgressChanged.emit(progress)

    def loadDataset(self):
        """
        Loads the dataset from the filenames.
        """

        dark_filename = self.getDarkFilename() if self.getDarkFilename() else None
        flood_filename = self.getFloodFilename() if self.getFloodFilename() else None
        spline_filename = self.getSplineFilename() if self.getSplineFilename() else None
        filenames = self._rawFilesData.getFiles()
        if not filenames:
            filenames = self._rawFilenameData.getFilename()
        self._dataset = load_process_data(
            filenames,
            in_memory=not self._inDisk,
            dark_filename=dark_filename,
            flood_filename=flood_filename,
            spline_filename=spline_filename,
            isH5=self._isH5,
        )
        return self.dataset is not None and self.dataset.nframes != 0

    @property
    def dataset(self):
        return self._dataset

    def __inDisk(self, inDisk):
        self._inDisk = bool(inDisk)


class FilesSelectionWidget(qt.QWidget):
    """
    Widget used to get one or more files from the computer and add them to a list.
    """

    def __init__(self, parent=None):
        qt.QWidget.__init__(self, parent)

        self._files = []

        self.setLayout(qt.QVBoxLayout())
        self._table = self._init_table()
        self._addButton = qt.QPushButton("Add")
        self._rmButton = qt.QPushButton("Remove")
        self.layout().addWidget(self._table)
        self.layout().addWidget(self._addButton)
        self.layout().addWidget(self._rmButton)
        self._addButton.clicked.connect(self._addFiles)
        self._rmButton.clicked.connect(self._removeFiles)

    def _init_table(self):

        table = qt.QTableWidget(0, 1, parent=self)
        table.horizontalHeader().hide()
        # Resize horizontal header to fill all the column size
        if hasattr(table.horizontalHeader(), "setSectionResizeMode"):  # Qt5
            table.horizontalHeader().setSectionResizeMode(0, qt.QHeaderView.Stretch)
        else:  # Qt4
            table.horizontalHeader().setResizeMode(0, qt.QHeaderView.Stretch)

        return table

    def _addFiles(self):
        """
        Opens the file dialog and let's the user choose one or more files.
        """
        dialog = qt.QFileDialog(self)
        dialog.setFileMode(qt.QFileDialog.ExistingFiles)

        if not dialog.exec_():
            dialog.close()
            return

        for file in dialog.selectedFiles():
            self.addFile(file)

    def _removeFiles(self):
        """
        Removes the selected items from the table.
        """
        selectedItems = self._table.selectedItems()
        if selectedItems is not None:
            for item in selectedItems:
                self._files.remove(item.text())
                self._table.removeRow(item.row())

    def addFile(self, file):
        """
        Adds a file to the table.

        :param str file: filepath to add to the table.
        """
        assert os.path.isfile(file)
        item = qt.QTableWidgetItem()
        item.setText(file)
        row = self._table.rowCount()
        self._table.setRowCount(row + 1)
        self._table.setItem(row, 0, item)
        self._files.append(file)

    def getFiles(self):
        return self._files

    def setFiles(self, files):
        """
        Adds a list of files to the table.

        :param array_like files: List to add
        """
        for file in files:
            self.addFile(file)

    def getDir(self):
        if len(self._files):
            return os.path.dirname(self._files[0])
        return None


class FilenameSelectionWidget(qt.QWidget):
    """
    Widget used to obtain a filename (manually or from a file)
    """

    filenameChanged = qt.Signal()

    def __init__(
        self,
        buttonText,
        parent=None,
        fileMode=qt.QFileDialog.AnyFile,
        acceptMode=qt.QFileDialog.AcceptOpen,
    ):
        qt.QWidget.__init__(self, parent)

        self._isH5 = False
        self._filename = None
        self._filenameLE = qt.QLineEdit("", parent=self)
        # self._filenameLE.editingFinished.connect(self.filenameChanged)
        self._addButton = qt.QPushButton(buttonText, parent=self)
        # self._okButton =  qt.QPushButton("Ok", parent=self)
        self._addButton.pressed.connect(self._uploadFilename)
        # self._okButton.pressed.connect(self.close)
        self._fileMode = fileMode
        self._acceptMode = acceptMode
        self.setLayout(qt.QHBoxLayout())

        self.layout().addWidget(self._filenameLE)
        self.layout().addWidget(self._addButton)
        # self.layout().addWidget(self._okButton)

    def isHDF5(self, isH5):
        self._isH5 = isH5

    def _uploadFilename(self):
        """
        Loads the file from a FileDialog.
        """
        if self._isH5:
            fileDialog = DataFileDialog()

            if fileDialog.exec_():
                self._filename = fileDialog.selectedDataUrl().path()
                self._filenameLE.setText(self._filename)
                self.filenameChanged.emit()
            else:
                _logger.warning("Could not open file")
        else:
            fileDialog = qt.QFileDialog()
            fileDialog.setFileMode(self._fileMode)
            fileDialog.setAcceptMode(self._acceptMode)

            if fileDialog.exec_():
                self._filenameLE.setText(fileDialog.selectedFiles()[0])
                self.filenameChanged.emit()
            else:
                _logger.warning("Could not open file")

    def getFilename(self):
        return str(self._filenameLE.text())

    def setFilename(self, filename):
        self._filename = filename
        self._filenameLE.setText(str(filename))
