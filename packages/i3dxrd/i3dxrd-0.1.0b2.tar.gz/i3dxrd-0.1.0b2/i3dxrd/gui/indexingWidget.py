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
__date__ = "28/01/2021"

import logging
import os

import numpy

from silx.gui import qt
from silx.gui.colors import Colormap
from silx.gui.plot3d.SceneWindow import SceneWindow
from silx.gui.plot3d import items
from silx.gui.plot import PlotWindow

from ImageD11 import indexing

from .calibrationWidget import ParametersDialog

_logger = logging.getLogger(__file__)


class _ParametersDock(qt.QDockWidget):
    def __init__(self, parent=None):
        """
        Dock widget containing the input parameters.
        """
        qt.QDockWidget.__init__(self, parent)
        widget = qt.QWidget()
        layout = qt.QGridLayout()

        # Init buttons
        self.thresholdsCB = qt.QComboBox(parent=self)
        thresh_layout = qt.QHBoxLayout()
        thresh_layout.addWidget(qt.QLabel("Thresholds:"))
        thresh_layout.addWidget(self.thresholdsCB)
        thresh_widget = qt.QWidget()
        thresh_widget.setLayout(thresh_layout)
        thresh_layout.setContentsMargins(0, 0, 0, 0)
        self.loadGVectors = qt.QPushButton("Load g-vectors")
        self.assignPeaks = qt.QPushButton("Assign peaks to powder rings")
        self.editParameters = qt.QPushButton("Edit parameters")
        self.loadParameters = qt.QPushButton("Load parameters")
        self.generateOrientations = qt.QPushButton("Generate trial orientations")
        self.generateOrientations.setEnabled(False)
        self.scoreOrientations = qt.QPushButton("Score trial orientations")
        self.scoreOrientations.setEnabled(False)
        layout.addWidget(thresh_widget, 0, 0, 1, 2)
        layout.addWidget(self.loadGVectors, 0, 2, 1, 2)
        layout.addWidget(self.assignPeaks, 0, 4, 1, 2)
        layout.addWidget(self.editParameters, 2, 0, 1, 3)
        layout.addWidget(self.loadParameters, 2, 3, 1, 3)
        layout.addWidget(self.generateOrientations, 3, 0, 1, 3)
        layout.addWidget(self.scoreOrientations, 3, 3, 1, 3)

        widget.setLayout(layout)
        self.setWidget(widget)


class IndexingWidget(qt.QMainWindow):
    """
    Widget for indexing the orientations of the sample to the corresponding grains.
    """

    def __init__(self, parent=None):
        qt.QMainWindow.__init__(self, parent)

        self.dataset = None

        self._thresholds = {}

        # Indexer
        self._indexer = indexing.indexer()

        self._parametersDock = _ParametersDock()
        self._parametersDock.setFeatures(qt.QDockWidget.DockWidgetMovable)
        self._parametersDock.scoreOrientations.pressed.connect(
            self.scoreTrialOrientations
        )
        self._parametersDock.loadGVectors.pressed.connect(self.loadGVectors)
        self._parametersDock.assignPeaks.pressed.connect(self.assignPeaks)
        self._parametersDock.editParameters.pressed.connect(self.showParameters)
        self._parametersDock.loadParameters.pressed.connect(self.loadParameters)
        self._parametersDock.generateOrientations.pressed.connect(
            self.generateTrialOrientations
        )
        self._parametersDock.thresholdsCB.currentIndexChanged.connect(
            self._changeThreshold
        )
        self.addDockWidget(qt.Qt.TopDockWidgetArea, self._parametersDock)

        self.bottomDock = qt.QDockWidget(self)
        self._plotHist = qt.QPushButton("Plot histograms of UBI matrices")
        self._saveUBI = qt.QPushButton("Save UBI matrices")
        self._plotHist.pressed.connect(self.plotHist)
        self._saveUBI.pressed.connect(self.saveUBI)
        self._plot = PlotWindow(self)
        self._plot.setMinimumHeight(200)
        self._plot.hide()

        layout = qt.QGridLayout()
        layout.addWidget(self._plotHist, 0, 0)
        layout.addWidget(self._saveUBI, 0, 2)
        layout.addWidget(self._plot, 1, 0, 1, 3)
        widget = qt.QWidget()
        widget.setLayout(layout)

        self.bottomDock.setWidget(widget)
        self.bottomDock.setEnabled(False)
        self.addDockWidget(qt.Qt.BottomDockWidgetArea, self.bottomDock)

        # Create a SceneWindow
        window = SceneWindow(self)

        # First scatter
        self._sceneWidget = window.getSceneWidget()
        self._sceneWidget.setBackgroundColor((0.8, 0.8, 0.8, 1.0))
        self._sceneWidget.setForegroundColor((1.0, 1.0, 1.0, 1.0))
        self._sceneWidget.setTextColor((0.1, 0.1, 0.1, 1.0))
        self._scatter1 = items.Scatter3D()
        self._scatter1.setColormap(Colormap(name="hsv"))
        self._scatter1.setSymbol("d")
        SIZE = 1024
        self._scatter1.setScale(SIZE, SIZE, SIZE)
        self._scatter1.setSymbolSize(11)  # Set the size of the markers
        self._sceneWidget.addItem(self._scatter1)

        # Second scatter
        self._scatter2 = items.Scatter3D()
        self._scatter2.setSymbol("o")
        self._scatter2.getColormap().setName("gray")  # Use 'magma' colormap
        self._scatter2.setScale(SIZE, SIZE, SIZE)
        self._scatter2.setSymbolSize(11)  # Set the size of the markers
        self._scatter2.setLabel(
            "Scatter with non-assigned peaks"
        )  # Set name displayed in parameter tree
        self.setCentralWidget(window)

    def setDataset(self, dataset):
        self.dataset = dataset
        oldState = self._parametersDock.thresholdsCB.blockSignals(True)
        self._parametersDock.thresholdsCB.clear()
        self._parametersDock.thresholdsCB.blockSignals(oldState)
        self._parametersDock.thresholdsCB.addItems(
            [str(peaks.threshold) for peaks in self.dataset.peaks_groups]
        )

    def _changeThreshold(self, index):
        """
        Pick up new file with different threshold peaks.
        """
        self._parametersDock.thresholdsCB.setEnabled(False)
        filename = (
            self.dataset.peaks_groups[index].gvectors
            if self.dataset is not None
            else self._thresholds[self._parametersDock.thresholdsCB.currentText()]
        )

        try:
            self._indexer.readgvfile(filename)
            self._scatter1.setLabel(
                "Scatter with gvectors"
            )  # Set name displayed in parameter tree
            self.plotXYZ(self._indexer.gv.T)
        except (IndexError, TypeError):
            _logger.warning("No gvectors to plot")
        self._parametersDock.thresholdsCB.setEnabled(True)

    def loadGVectors(self):
        """
        Load g-vectors from file
        """
        fileDialog = qt.QFileDialog(self, "Load g-vectors")
        fileDialog.setFileMode(qt.QFileDialog.ExistingFile)
        fileDialog.setNameFilter("Parameters files (*.gv *.gve);;All files (*);;")
        if fileDialog.exec_():
            filename = fileDialog.selectedFiles()[0]
            try:
                i = filename.find("_t")
                threshold = filename[i + 2:-4]
            except ValueError:
                threshold = os.basename(filename)
                _logger.warning("Could not find threshold in filename")
            if self.dataset is not None:
                oldState = self._parametersDock.thresholdsCB.blockSignals(True)
                peaks = self.dataset.add_peaks(threshold)
                peaks.gvectors = filename
                self._parametersDock.thresholdsCB.clear()
                self._parametersDock.thresholdsCB.blockSignals(oldState)
                self._parametersDock.thresholdsCB.addItem(threshold)
                self._parametersDock.thresholdsCB.setCurrentText(str(threshold))
            else:
                self._thresholds[threshold] = filename
                self._parametersDock.thresholdsCB.addItem(threshold)
                self._parametersDock.thresholdsCB.setCurrentText(str(threshold))
            self._indexer.readgvfile(filename)
            self.plotXYZ(self._indexer.gv.T)
        else:
            _logger.warning("Could not open file")

    def generateTrialOrientations(self):
        """
        Find orientations.
        """
        self._indexer.find()
        self._parametersDock.scoreOrientations.setEnabled(True)

    def scoreTrialOrientations(self):
        """
        Score orientations
        """
        self._indexer.scorethem()

    def saveUBI(self):
        """
        Save UBI matrices into file.
        """
        fileDialog = qt.QFileDialog(self, "Save UBI")
        fileDialog.setFileMode(qt.QFileDialog.AnyFile)
        fileDialog.setAcceptMode(qt.QFileDialog.AcceptSave)
        fileDialog.setNameFilter("UBI files (*.ubi);;All files (*);;")
        if fileDialog.exec_():
            filename = fileDialog.selectedFiles()[0]
            self._indexer.saveubis(filename)
            idx = self._parametersDock.thresholdsCB.currentIndex()
            self.dataset.peaks_groups[idx].ubi_file = filename
        else:
            _logger.warning("Could not open file")

    def plotHist(self):
        """
        Plot histogram of the difference between calculated orientations and
        errors in peak position.
        """
        self._indexer.histogram_drlv_fit()
        x = self._indexer.histogram
        y = self._indexer.bins
        self._plot.clear()
        for xline in x:
            self._plot.addHistogram(xline, y[1:], legend=str(xline))
        self._plot.show()

    def plotXYZ(self, peaks1, peaks2=None, values1=None, values2=None):
        """
        Plot scatter with corresponding data.
        """
        self._scatter1.setData(
            peaks1[0],
            peaks1[1],
            peaks1[2],
            numpy.zeros(peaks1.shape[1]) if values1 is None else values1,
        )
        if peaks2 is not None:
            self._scatter2.setData(
                peaks2[0],
                peaks2[1],
                peaks2[2],
                numpy.zeros(peaks2.shape[1]) if values2 is None else values2,
            )
        else:
            if self._scatter2 in self._sceneWidget.getItems():
                self._sceneWidget.removeItem(self._scatter2)
        self._parametersDock.generateOrientations.setEnabled(True)
        self.bottomDock.setEnabled(True)

    def assignPeaks(self):
        """
        Assign peaks to powder rings
        """
        if self._scatter2 not in self._sceneWidget.getItems():
            self._sceneWidget.addItem(self._scatter2)
        self._scatter1.setLabel(
            "Scatter with assigned peaks"
        )  # Set name displayed in parameter tree
        self._indexer.assigntorings()
        N = len(numpy.unique(self._indexer.ra))
        values1 = (self._indexer.ra[self._indexer.ra != -1] * (N + 1) // 2) % N
        values2 = self._indexer.ra[self._indexer.ra == -1]
        peaks1 = self._indexer.gv[self._indexer.ra != -1].T
        peaks2 = self._indexer.gv[self._indexer.ra == -1].T
        self.plotXYZ(peaks1, peaks2, values1, values2)

    def applyParameters(self):
        """
        Update plot with new parameters.
        """
        result = self._paramsDialog.result()
        self._indexer.parameterobj.set_parameters(result)
        self._indexer.loadpars()

    def saveParameters(self, filename):
        """
        Save parameters to file.
        """
        result = self._paramsDialog.result()
        self._indexer.parameterobj.set_parameters(result)
        self._indexer.saveparameters(filename)

    def showParameters(self):
        """
        Show parameters dialog.
        """
        self._indexer.updateparameters()
        self._paramsDialog = ParametersDialog(self, self._indexer.pars)
        self._paramsDialog.applyParametersSignal.connect(self.applyParameters)
        self._paramsDialog.saveParametersSignal.connect(self.saveParameters)
        if self._paramsDialog.exec_() == qt.QDialog.Accepted:
            self.applyParameters()

    def loadParameters(self):
        """
        Load parameters from file
        """
        fileDialog = qt.QFileDialog(self, "Load parameters")
        fileDialog.setFileMode(qt.QFileDialog.ExistingFile)
        fileDialog.setNameFilter(
            "Parameters files (*.par *.prm, *.prms);;All files (*);;"
        )
        if fileDialog.exec_():
            filename = fileDialog.selectedFiles()[0]
            self._indexer.loadpars(filename)
        else:
            _logger.warning("Could not open file")
