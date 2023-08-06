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
__date__ = "22/07/2020"

import logging

from silx.gui import qt
from silx.gui.colors import Colormap
from silx.gui.plot import ScatterView

from ImageD11.columnfile import columnfile

_logger = logging.getLogger(__file__)


class ShowPeaksWidget(qt.QMainWindow):
    def __init__(self, parent=None):
        qt.QMainWindow.__init__(self, parent)

        colWidget = self._initColPlot()
        self.setCentralWidget(colWidget)

    def _initColPlot(self):

        widget = qt.QWidget()
        layout = qt.QGridLayout()

        self._thresholdsCB = qt.QComboBox(parent=self)
        self._thresholdsCB.currentIndexChanged.connect(self._changeThreshold)
        bxa = qt.QComboBox(None)
        bya = qt.QComboBox(None)
        bza = qt.QComboBox(None)
        self._axisboxes = [bxa, bya, bza]
        self._ignoreselect = True
        for box in self._axisboxes:
            box.currentIndexChanged.connect(self.select)
        self._loadPeaks = qt.QPushButton("Load peaks")
        self._loadPeaks.pressed.connect(self.loadPeaks)

        self._scatterView = ScatterView(backend="gl")
        # import pdb; pdb.set_trace()
        if not self._scatterView._plot()._backend.isValid():
            self._scatterView = ScatterView(backend="matplotlib")
        self._scatterView.setColormap(Colormap(name="cividis", normalization="log"))
        self._scatterView.getMaskToolsWidget().parent().setFloating(True)
        self._scatterView.getMaskToolsWidget().show()

        layout.addWidget(qt.QLabel("Thresholds:"), 0, 0)
        layout.addWidget(self._thresholdsCB, 0, 1)
        layout.addWidget(self._loadPeaks, 0, 2)
        layout.addWidget(self._scatterView, 1, 0, 1, 3)
        layout.addWidget(qt.QLabel("x-plot"), 2, 0)
        layout.addWidget(qt.QLabel("y-plot"), 2, 1)
        layout.addWidget(qt.QLabel("color"), 2, 2)
        layout.addWidget(bxa, 3, 0)
        layout.addWidget(bya, 3, 1)
        layout.addWidget(bza, 3, 2)
        widget.setLayout(layout)

        return widget

    def select(self, col):
        """
        Choose the x,y,z axes for plotting
        """
        if self._ignoreselect:
            return
        self.update()
        self._scatterView.resetZoom()

    def setDataset(self, dataset):
        self.dataset = dataset
        oldState = self._thresholdsCB.blockSignals(True)
        self._thresholdsCB.clear()
        self._thresholdsCB.blockSignals(oldState)
        self._thresholdsCB.addItems(
            [str(peaks.threshold) for peaks in self.dataset.peaks_groups]
        )

    def addPeaks(self, threshold):
        self._thresholdsCB.addItem(str(threshold))

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
                    [str(peaks.threshold) for peaks in self.dataset.peaks_groups]
                )
                self._thresholdsCB.setCurrentText(str(threshold))
            except ValueError:
                _logger.warning("Could not find threshold in filename")
        else:
            _logger.warning("Could not open file")

    def _changeThreshold(self, idx):
        self._thresholdsCB.setEnabled(False)
        filename = self.dataset.peaks_groups[idx].flt_file
        self.openColFile(filename)
        self._thresholdsCB.setEnabled(True)

    def openColFile(self, filename):

        try:
            self._colfile = columnfile(filename)
        except OSError:
            print("problem opening file", filename)
            return
        except IndexError:
            print("Problem reading file (maybe empty?)")
            return

        self.setTitles()
        self.update()
        self._scatterView.resetZoom()

    def setTitles(self):
        """Read the colfile titles into the dropdowns"""
        self._ignoreselect = True
        for i, b in enumerate(self._axisboxes):
            t = b.currentText()
            b.clear()
            b.addItems(self._colfile.titles)
            if t in self._colfile.titles:
                b.setCurrentIndex(self._colfile.titles.index(t))
            else:
                b.setCurrentIndex(i)
        self._ignoreselect = False

    def update(self):
        """Refreshes the plot"""
        self.x = self._colfile.getcolumn(self._axisboxes[0].currentText())
        self.y = self._colfile.getcolumn(self._axisboxes[1].currentText())
        self.z = self._colfile.getcolumn(self._axisboxes[2].currentText())
        self._scatterView.getXAxis().setLabel(self._axisboxes[0].currentText())
        self._scatterView.getYAxis().setLabel(self._axisboxes[1].currentText())
        self._scatterView.setGraphTitle("color: " + self._axisboxes[2].currentText())
        self._scatterView.setData(self.x, self.y, self.z)
