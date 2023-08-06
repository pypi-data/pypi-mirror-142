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
__date__ = "12/08/2020"

from silx.gui import qt
from silx.gui.colors import Colormap
from silx.gui.plot.StackView import StackViewMainWindow
from .dataSelectionWidget import FilenameSelectionWidget

from darfix.gui.operationThread import OperationThread


class BackgroundSubtractionWidget(qt.QWidget):
    """
    Widget to apply background subtraction to a dataset
    """

    def __init__(self, parent=None):
        qt.QWidget.__init__(self, parent)

        self.setLayout(qt.QVBoxLayout())
        self._compute = qt.QPushButton("Compute background subtraction")
        self._compute.pressed.connect(self.__computeBS)
        widget = qt.QWidget()
        layout = qt.QHBoxLayout()
        layout.addWidget(qt.QLabel("Step:"))
        self._step = qt.QLineEdit("1")
        self._outputFilename = FilenameSelectionWidget(
            "Load output filename", parent=self, acceptMode=qt.QFileDialog.AcceptSave
        )
        self._outputFilename.setFilename("background.edf")
        layout.addWidget(self._step)
        layout.addWidget(self._outputFilename)
        widget.setLayout(layout)
        self._sv = StackViewMainWindow()
        self._sv.setColormap(Colormap("magma", normalization="log"))
        self.layout().addWidget(widget)
        self.layout().addWidget(self._sv)
        self.layout().addWidget(self._compute)

    def __computeBS(self):
        """
        Function that starts the thread to compute the background
        subtraction.
        #"""
        # if not self.dataset.in_memory:
        #     chunks = [int(self._parametersDock.verticalChunkSize.text()),
        #               int(self._parametersDock.horizontalChunkSize.text())]
        self._compute.setEnabled(False)
        outputFilename = self._outputFilename.getFilename()
        self._thread = OperationThread(self, self.dataset.compute_background)
        self._thread.setArgs(outputFilename, step=int(self._step.text()))
        self._thread.finished.connect(self._updateData)
        self._thread.start()

    def _updateData(self):
        """
        Updates the stack with the data computed in the thread
        """
        self._thread.finished.disconnect(self._updateData)
        if self._thread.data is not None:
            self.dataset.data.background = self._thread.data
            self.setStack()
        else:
            print("\nComputation aborted")
        self._compute.setEnabled(True)

    def setDataset(self, dataset):
        """
        Dataset setter. Saves the dataset and updates the stack with the dataset
        data

        :param Dataset dataset: dataset
        """
        self.dataset = dataset
        self.setStack()

    def getDataset(self):
        return self._update_dataset, self.indices, self.bg_indices, self.bg_dataset

    def resetStack(self):
        self.setStack()

    def clearStack(self):
        self._sv.setStack(None)

    def getStack(self):
        return self._sv.getStack(False, True)[0]

    def setStack(self, dataset=None):
        """
        Sets new data to the stack.
        Mantains the current frame showed in the view.

        :param Dataset dataset: if not None, data set to the stack will be from the given dataset.
        """
        if dataset is None:
            dataset = self.dataset
        nframe = self._sv.getFrameNumber()
        self._sv.clear()
        self._sv.setStack(dataset.data, reset=True)
        self._sv.setFrameNumber(nframe + 1)
        self._sv.setFrameNumber(nframe)
