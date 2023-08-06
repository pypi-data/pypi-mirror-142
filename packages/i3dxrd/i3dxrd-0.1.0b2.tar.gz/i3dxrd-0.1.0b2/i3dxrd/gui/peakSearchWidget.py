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
__date__ = "11/08/2020"

import logging

from silx.gui import qt
from darfix.gui.operationThread import OperationThread
from .dataSelectionWidget import FilenameSelectionWidget
from .showPeaksWidget import ShowPeaksWidget

_logger = logging.getLogger(__file__)


class PeakSearchWidget(qt.QMainWindow):

    sigComputed = qt.Signal()

    def __init__(self, parent=None):
        qt.QMainWindow.__init__(self, parent)

        self.dataset = None

        thresholdLabel = qt.QLabel("Threshold:")
        self._threshold = qt.QLineEdit("", parent=self)
        omegaLabel = qt.QLabel("Omega:")
        self._omega = qt.QLineEdit("0", parent=self)
        omegaStepLabel = qt.QLabel("Omega step:")
        self._omegaStep = qt.QLineEdit("1", parent=self)
        self._omegaOverride = qt.QCheckBox("Omega override", self)
        self._outputFilename = FilenameSelectionWidget(
            "Load output filename", parent=self, acceptMode=qt.QFileDialog.AcceptSave
        )
        self._computeButton = qt.QPushButton("Search peaks")
        self._computeButton.setEnabled(False)
        self._computeButton.pressed.connect(self.computePeakSearch)

        widget = qt.QWidget(self)
        widget.setLayout(qt.QGridLayout())
        widget.layout().addWidget(thresholdLabel, 0, 0)
        widget.layout().addWidget(self._threshold, 0, 1)
        widget.layout().addWidget(omegaLabel, 0, 2)
        widget.layout().addWidget(self._omega, 0, 3)
        widget.layout().addWidget(omegaStepLabel, 1, 0)
        widget.layout().addWidget(self._omegaStep, 1, 1)
        widget.layout().addWidget(self._omegaOverride, 1, 2, 1, 2, qt.Qt.AlignRight)
        widget.layout().addWidget(self._outputFilename, 3, 0, 1, 4)
        widget.layout().addWidget(self._computeButton, 4, 3)

        self._showPeaks = ShowPeaksWidget()
        # Main widget is a Splitter with the top widget and the displayComponentsWidget
        self.splitter = qt.QSplitter(qt.Qt.Vertical)
        self.splitter.addWidget(widget)
        self.splitter.addWidget(self._showPeaks)
        self.setCentralWidget(self.splitter)

    def setDataset(self, dataset):
        self.dataset = dataset
        self._showPeaks.setDataset(dataset)
        self._computeButton.setEnabled(True)
        self._thread = OperationThread(self, self.dataset.peak_search)

    def computePeakSearch(self):

        if not self._threshold.text():
            raise ValueError("Threshold value must be filled")
        outputFilename = self._outputFilename.getFilename()
        thresholds = [float(self._threshold.text())]
        omega = float(self._omega.text())
        omega_step = float(self._omegaStep.text())
        omega_override = self._omegaOverride.isChecked()
        self._computeButton.setEnabled(False)

        if not outputFilename:
            outputFilename = "peak_search"
        self._thread.setArgs(
            thresholds, outputFilename, omega, omega_override, omega_step
        )
        self._thread.start()
        self._thread.finished.connect(self._updateData)

    def _updateData(self):
        self._thread.finished.disconnect(self._updateData)
        self._showPeaks.addPeaks(self.dataset.peaks_groups[-1].threshold)
        self._computeButton.setEnabled(True)

        self.sigComputed.emit()
