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
__date__ = "30/11/2020"

# import os

import logging

from silx.gui import qt
from silx.gui.colors import Colormap
from silx.gui.plot.StackView import StackViewMainWindow
from ImageD11.peakmerge import peakmerger


_logger = logging.getLogger(__file__)


class StackViewWidget(qt.QWidget):
    """
    Widget that allows the user to pick a ROI in any image of the dataset.
    """

    def __init__(self, parent=None):
        qt.QWidget.__init__(self, parent)

        self.peakMerger = peakmerger()

        self.setLayout(qt.QVBoxLayout())
        self._thresholdsCB = qt.QComboBox(parent=self)
        self._thresholdsCB.currentTextChanged.connect(self._changeThreshold)
        self._loadPeaks = qt.QPushButton("Load peaks")
        self._loadPeaks.pressed.connect(self.loadPeaks)
        widget = qt.QWidget()
        layout = qt.QHBoxLayout()
        layout.addWidget(qt.QLabel("Thresholds:"))
        layout.addWidget(self._thresholdsCB)
        layout.addWidget(self._loadPeaks)
        widget.setLayout(layout)
        self._sv = StackViewMainWindow()
        self._sv.setColormap(Colormap("magma", normalization="log"))
        self.layout().addWidget(widget)
        self.layout().addWidget(self._sv)

    def setDataset(self, dataset):
        """
        Dataset setter. Saves the dataset and updates the stack with the dataset
        data

        :param Dataset dataset: dataset
        """
        self.dataset = dataset
        oldState = self._thresholdsCB.blockSignals(True)
        self._thresholdsCB.clear()
        self._thresholdsCB.blockSignals(oldState)
        self._thresholdsCB.addItems(
            [str(peaks.threshold) for peaks in self.dataset.peaks_groups]
        )
        self.setStack(dataset)

    def _changeThreshold(self, text):
        self._thresholdsCB.setEnabled(False)
        filename = self.dataset.thresholds_spt[float(text)]
        self._reloadPeaks(filename)
        self._thresholdsCB.setEnabled(True)

    def _reloadPeaks(self, filename):
        self.peakMerger.readpeaks(filename)
        self.select_image(0)
        self._sv.sigFrameChanged.connect(self.select_image)

    def loadPeaks(self):
        """
        Load peaks from file
        """
        fileDialog = qt.QFileDialog(self, "Load peaks")
        fileDialog.setFileMode(qt.QFileDialog.ExistingFile)
        fileDialog.setNameFilter(
            "Flt files (*.flt);;Spt files (*.spt);;All files (*);;"
        )
        if fileDialog.exec_():
            filename = fileDialog.selectedFiles()[0]
            filename_spt = filename[:-3] + "spt"
            i = filename.find("_t")
            threshold = filename[i + 2:-4]
            try:
                threshold = float(threshold)
                self.dataset.add_peaks(threshold, filename, filename_spt)
                oldState = self._thresholdsCB.blockSignals(True)
                self._thresholdsCB.clear()
                self._thresholdsCB.blockSignals(oldState)
                self._thresholdsCB.addItems(
                    [str(key) for key in self.dataset.thresholds_spt.keys()]
                )
                self._thresholdsCB.setCurrentText(str(threshold))
            except ValueError:
                print("Could not find threshold in filename")
        else:
            _logger.warning("Could not open file")

    def select_image(self, i):
        if i < 0 or i > len(self.peakMerger.images) - 1:
            return False
        im = self.peakMerger.images[i]
        self.currentnum = i
        j = im.imagenumber
        self.peakMerger.harvestpeaks(numlim=(j - 0.1, j + 0.1))
        self.pkx = [p.x for p in self.peakMerger.allpeaks]
        self.pky = [p.y for p in self.peakMerger.allpeaks]
        self.pkI = [p.avg for p in self.peakMerger.allpeaks]
        self.plotPeaks()
        return True

    def plotPeaks(self):

        plot = self._sv.getPlot()
        self.plotLabel = plot.addScatter(
            self.pky, self.pkx, self.pkI, z=1, symbol="+", colormap=Colormap("viridis")
        )
        plot.getScatter(self.plotLabel).setSymbolSize(10)
        plot.setKeepDataAspectRatio(True)

    def setStack(self, dataset=None):
        """
        Sets new data to the stack.
        Mantains the current frame showed in the view.

        :param Dataset dataset: if not None, data set to the stack will be from the given dataset.
        """
        if dataset is None:
            dataset = self.dataset
        nframe = self._sv.getFrameNumber()
        self._sv.setStack(dataset.data)
        self._sv.setFrameNumber(nframe)
