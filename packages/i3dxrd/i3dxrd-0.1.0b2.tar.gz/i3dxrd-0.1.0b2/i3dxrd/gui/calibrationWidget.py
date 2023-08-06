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
import numpy

from silx.gui import qt
from silx.gui.colors import Colormap
from silx.gui.plot import ScatterView
from ImageD11 import transformer

_logger = logging.getLogger(__file__)


class CalibrationWidget(qt.QMainWindow):
    """
    Widget for calibrating the parameters. It shows in a scatterView the tth and eta values of the data,
    to help the user perform the calibration.
    """

    def __init__(self, parent=None):
        qt.QMainWindow.__init__(self, parent)

        self.dataset = None

        widget = qt.QWidget()
        layout = qt.QGridLayout()
        self._transformer = transformer.transformer()

        self._thresholdsCB = qt.QComboBox(parent=self)
        self._thresholdsCB.currentIndexChanged.connect(self._changeThreshold)
        self._editParameters = qt.QPushButton("Edit parameters")
        self._editParameters.pressed.connect(self.showParameters)
        self._loadParameters = qt.QPushButton("Load parameters")
        self._loadParameters.pressed.connect(self.loadParameters)
        self._addCellPeaksB = qt.QPushButton("Add cell peaks")
        self._addCellPeaksB.pressed.connect(self.addCellPeaks)
        self._saveGvB = qt.QPushButton("Save g-vectors")
        self._saveGvB.pressed.connect(self.saveGVectors)
        self._fitB = qt.QPushButton("Fit")
        self._fitB.pressed.connect(self.fit)
        self._shownCellPeaks = False

        self._scatterView = ScatterView(backend="gl")
        # import pdb; pdb.set_trace()
        if not self._scatterView._plot()._backend.isValid():
            self._scatterView = ScatterView(backend="matplotlib")
        self._scatterView.setColormap(Colormap(name="cividis", normalization="log"))
        self._scatterView.getMaskToolsWidget().parent().setFloating(True)
        self._scatterView.getMaskToolsWidget().show()
        self._scatterView.getScatterItem().setSymbolSize(1.0)

        thresh_layout = qt.QHBoxLayout()

        thresh_layout.addWidget(qt.QLabel("Thresholds:"))
        thresh_layout.addWidget(self._thresholdsCB)
        thresh_widget = qt.QWidget()
        thresh_widget.setLayout(thresh_layout)
        thresh_layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(thresh_widget, 0, 0, 1, 1)
        layout.addWidget(self._editParameters, 0, 1)
        layout.addWidget(self._fitB, 0, 2)
        layout.addWidget(self._loadParameters, 1, 0)
        layout.addWidget(self._addCellPeaksB, 1, 1)
        layout.addWidget(self._saveGvB, 1, 2)
        layout.addWidget(self._scatterView, 2, 0, 1, 3)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def setDataset(self, dataset):
        self.dataset = dataset
        oldState = self._thresholdsCB.blockSignals(True)
        self._thresholdsCB.clear()
        self._thresholdsCB.blockSignals(oldState)
        self._thresholdsCB.addItems(
            [str(peaks.threshold) for peaks in self.dataset.peaks_groups]
        )

    def addCellPeaks(self):
        """
        Add cell peaks to the plot.
        """
        self._shownCellPeaks = True
        self._transformer.addcellpeaks()
        theory_tth = self._transformer.theorytth
        self._scatterView.getPlotWidget().remove(kind="curve")
        curve = self._scatterView.getPlotWidget().addCurve(
            theory_tth,
            numpy.zeros(theory_tth.shape[0]),
            symbol="|",
            linestyle=" ",
            color="red",
        )
        self._scatterView.getPlotWidget().getCurve(curve).setSymbolSize(20.0)

    def fit(self):
        """
        Fit parameters with vary to make the computed two-theta positions match
        the observed ones.
        """
        tthmin, tthmax = self._scatterView.getPlotWidget().getXAxis().getLimits()
        self._transformer.fit(tthmin, tthmax)
        tth, eta = self._transformer.compute_tth_eta()
        inds = numpy.array(self._transformer.indices).flatten()
        values = numpy.zeros((len(tth),))
        for inds in self._transformer.indices:
            values[inds] = numpy.ones(len(inds)) * numpy.random.random() + 0.5
        self.plotTthEta(values)

    def saveGVectors(self):
        """
        Save g-vectors, i.e scattering vectors, into file.
        """
        self._transformer.computegv()
        fileDialog = qt.QFileDialog(self, "Save g-vectors")
        fileDialog.setFileMode(qt.QFileDialog.AnyFile)
        fileDialog.setAcceptMode(qt.QFileDialog.AcceptSave)
        fileDialog.setDefaultSuffix(".gve")
        fileDialog.setNameFilter("G-vectors files (*.gve *.gv);;All files (*);;")
        if fileDialog.exec_():
            filename = fileDialog.selectedFiles()[0]
            self._transformer.savegv(filename)
            i = self._thresholdsCB.currentIndex()
            self.dataset.peaks_groups[i].gvectors = filename
        else:
            _logger.warning("Could not open file")

    def _changeThreshold(self, index):
        """
        Pick up new file with different threshold peaks.
        """
        self._thresholdsCB.setEnabled(False)
        peaks = self.dataset.peaks_groups[index]
        try:
            self._transformer.loadfiltered(peaks.flt_file)
        except IndexError:
            _logger.warning("No peaks to plot")
        self._thresholdsCB.setEnabled(True)
        self.plotTthEta()

    def plotTthEta(self, values=None):
        """
        Plot tth and eta values.
        """
        try:
            tth, eta = self._transformer.compute_tth_eta()
            self._thresholdsCB.setEnabled(True)
            self._scatterView.setData(
                tth, eta, values if values is not None else numpy.zeros((len(tth),))
            )
            self._scatterView.resetZoom()
            if self._shownCellPeaks:
                self.addCellPeaks()
        except Exception as e:
            _logger.warning(e)

    def applyParameters(self):
        """
        Update plot with new parameters.
        """
        result = self._paramsDialog.result()
        varys = []
        pars = {}
        for key in result:
            pars[key] = result[key][0]
            if result[key][1]:
                varys.append(key)
        self._transformer.parameterobj.set_parameters(pars)
        self._transformer.parameterobj.set_varylist(varys)
        self.plotTthEta()

    def saveParameters(self, filename):
        """
        Save parameters to file.
        """
        self.applyParameters()
        self._transformer.saveparameters(filename)
        self.dataset.peaks_groups[self._thresholdsCB.currentIndex()].parameters = filename

    def showParameters(self):
        """
        Show parameters dialog.
        """
        possvars = self._transformer.get_variable_list()
        _vars = self._transformer.getvars()
        logic = {}
        for v in possvars:
            if v in _vars:
                logic[v] = 1
            else:
                logic[v] = 0
        self._paramsDialog = ParametersDialog(self, self._transformer.pars, logic)
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
            self._transformer.loadfileparameters(filename)
            if self.dataset is not None:
                peaks = self.dataset.peaks_groups[self._thresholdsCB.currentIndex()]
                peaks.parameters = filename
            self.plotTthEta()
        else:
            _logger.warning("Could not open file")


class ParametersDialog(qt.QDialog):
    """
    Dialog for showing and editing the parameters.
    """

    saveParametersSignal = qt.Signal(str)
    applyParametersSignal = qt.Signal()

    def __init__(self, parent=None, parameters=None, variable_list=None):
        super(ParametersDialog, self).__init__(parent=parent)

        self._transformer = transformer
        self._slider = None
        self._focusedPar = None

        self.setWindowTitle("Detector parameters")

        QBtn = (
            qt.QDialogButtonBox.Ok
            | qt.QDialogButtonBox.Cancel
            | qt.QDialogButtonBox.Save
            | qt.QDialogButtonBox.Apply
        )

        self.buttonBox = qt.QDialogButtonBox(QBtn)
        self.buttonBox.button(qt.QDialogButtonBox.Save).clicked.connect(
            self.saveParameters
        )
        self.buttonBox.button(qt.QDialogButtonBox.Apply).clicked.connect(
            self.applyParameters
        )
        self.buttonBox.button(qt.QDialogButtonBox.Ok).clicked.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = qt.QVBoxLayout()

        class MyLineEdit(qt.QLineEdit):

            focusInSignal = qt.Signal()

            def focusInEvent(self, event):
                self.focusInSignal.emit()
                super(MyLineEdit, self).focusInEvent(event)

        if parameters is not None:
            self._keys = list(parameters.keys())
            self._keys.sort()
            self.pars_layout = qt.QGridLayout()
            self._parametersW = {}
            num_param = int(len(parameters) / 2)

            for i, key in enumerate(self._keys):
                if variable_list is not None:
                    par = MyLineEdit(str(parameters[key]))
                    par.focusInSignal.connect(self.parameterFocused)
                    vary = qt.QCheckBox("Vary?")
                    if i <= num_param:
                        self.pars_layout.addWidget(qt.QLabel(key), i * 2, 0)
                        self.pars_layout.addWidget(par, i * 2, 1)
                        if key in variable_list:
                            vary.setChecked(variable_list[key])
                            self.pars_layout.addWidget(vary, i * 2, 2)
                    else:
                        self.pars_layout.addWidget(
                            qt.QLabel(key), (i - num_param - 1) * 2, 3
                        )
                        self.pars_layout.addWidget(par, (i - num_param - 1) * 2, 4)
                        if key in variable_list:
                            vary.setChecked(variable_list[key])
                            self.pars_layout.addWidget(vary, (i - num_param - 1) * 2, 5)
                    self._parametersW[key] = (par, vary)
                else:
                    par = MyLineEdit(str(parameters[key]))
                    par.focusInSignal.connect(self.parameterFocused)
                    if i <= num_param:
                        self.pars_layout.addWidget(qt.QLabel(key), i * 2, 0)
                        self.pars_layout.addWidget(par, i * 2, 1)
                    else:
                        self.pars_layout.addWidget(
                            qt.QLabel(key), (i - num_param - 1) * 2, 3
                        )
                        self.pars_layout.addWidget(par, (i - num_param - 1) * 2, 4)
                    self._parametersW[key] = par

            paramWidget = qt.QWidget(parent=self)
            paramWidget.setLayout(self.pars_layout)
            self.layout.addWidget(paramWidget)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

    def parameterFocused(self):
        if self._slider is not None:
            self.pars_layout.removeWidget(self._slider)
        pos = self.pars_layout.getItemPosition(
            self.pars_layout.indexOf(self.focusWidget())
        )
        self._focusedPar = self.focusWidget()
        self._slider = qt.QSlider(qt.Qt.Horizontal)
        self._focusedPar.textEdited.connect(self._updateSlider)
        value = self._focusedPar.text()
        try:
            self._updateSlider(value)
            self._slider.valueChanged.connect(self._updateLineEdit)
            self.pars_layout.addWidget(self._slider, pos[0] + 1, pos[1])
        except ValueError:
            pass

    def _updateLineEdit(self, new_value):
        value = self._focusedPar.text()
        decimal_number = value[::-1].find(".")
        if decimal_number == -1:
            if "e" in value and value.split("e")[1][0] == "-":
                decimal_number = int(value.split("e")[1][1:])
            else:
                decimal_number = 0
        self._focusedPar.setText(
            "{0:.{precision}f}".format(
                float(new_value) / (10**decimal_number), precision=decimal_number
            )
        )

    def _updateSlider(self, value):

        oldState = self._slider.blockSignals(True)
        try:
            decimal_number = value[::-1].find(".")
            if decimal_number == -1 and "e" in value and value.split("e")[1][0] == "-":
                decimal_number = int(value.split("e")[1][1:])
                min_r = float(value) - 100 * 10 ** (-decimal_number)
                max_r = float(value) + 100 * 10 ** (-decimal_number)
                self._slider.setRange(
                    int(min_r * 10**decimal_number), int(max_r * 10**decimal_number)
                )
                self._slider.setValue(int(float(value) * 10**decimal_number))
        except ValueError:
            _logger.warning("Slider value can't be string")

        self._slider.blockSignals(oldState)

    def saveParameters(self):
        """
        Open dialog to choose file for saving the parameters and emit signal.
        """
        fileDialog = qt.QFileDialog(self, "Save parameters")
        fileDialog.setFileMode(qt.QFileDialog.AnyFile)
        fileDialog.setAcceptMode(qt.QFileDialog.AcceptSave)
        fileDialog.setDefaultSuffix(".par")
        fileDialog.setNameFilter(
            "Parameters files (*.par *.prm, *.prms);;All files (*);;"
        )
        if fileDialog.exec_():
            filename = fileDialog.selectedFiles()[0]
            self.saveParametersSignal.emit(filename)
        else:
            _logger.warning("Could not open file")

    def applyParameters(self):
        """
        Emit signal for applying parameters.
        """
        self.applyParametersSignal.emit()

    def result(self):
        """
        Returns list with dictionary containing the modified parameters.
        """
        result = {}
        for key in self._parametersW.keys():
            result[key] = (
                (
                    self._parametersW[key][0].text(),
                    self._parametersW[key][1].isChecked(),
                )
                if isinstance(self._parametersW[key], tuple)
                else self._parametersW[key].text()
            )
        return result
