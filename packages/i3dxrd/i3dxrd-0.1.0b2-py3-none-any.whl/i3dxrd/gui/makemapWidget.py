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
import numpy

from silx.gui import qt
from silx.gui.plot import PlotWindow
from silx.utils.enum import Enum as _Enum
from ImageD11.refinegrains import refinegrains
from .dataSelectionWidget import FilenameSelectionWidget

_logger = logging.getLogger(__file__)


class Lattice(_Enum):
    triclinic = "triclinic"
    monoclinic_a = "monoclinic_a"
    monoclinic_b = "monoclinic_b"
    monoclinic_c = "monoclinic_c"
    orthorhombic = "orthorhombic"
    tetragonal = "tetragonal"
    trigonalP = "trigonalP"
    trigonalH = "trigonalH"
    cubic = "cubic"


class MakemapWidget(qt.QWidget):
    """
    Widget for calibrating the parameters. It shows in a scatterView the tth and eta values of the data,
    to help the user perform the calibration.
    """

    def __init__(self, parent=None):
        qt.QMainWindow.__init__(self, parent)

        self.dataset = None
        self._thresholds = {}

        layout = qt.QGridLayout()
        self._parametersFilename = FilenameSelectionWidget(
            "Load parameters file", parent=self, fileMode=qt.QFileDialog.ExistingFile
        )
        self._ubiFilename = FilenameSelectionWidget(
            "Load UBI file", parent=self, fileMode=qt.QFileDialog.ExistingFile
        )
        self._newUbiFilename = FilenameSelectionWidget(
            "Load new ubi filename", parent=self, acceptMode=qt.QFileDialog.AcceptSave
        )
        self._fltFilename = FilenameSelectionWidget(
            "Load new flt filename", parent=self, acceptMode=qt.QFileDialog.AcceptSave
        )
        self._computeB = qt.QPushButton("Compute map", self)
        self._computeB.pressed.connect(self.compute)
        self._computeB.setEnabled(False)
        self._thresholdsCB = qt.QComboBox(parent=self)
        self._thresholdsCB.currentIndexChanged.connect(self._changeThreshold)
        self._loadPeaks = qt.QPushButton("Load peaks")
        self._loadPeaks.pressed.connect(self.loadPeaks)
        validator = qt.QDoubleValidator(self)
        validator.setLocale(qt.QLocale(qt.QLocale.English, qt.QLocale.UnitedStates))
        validator.setBottom(0)
        self._tolerance = qt.QLineEdit("0.05")
        self._tolerance.setValidator(validator)
        self._tth_range = qt.QLineEdit("(0, 180)")
        self._no_sort = qt.QCheckBox("No sort")
        self._omega_no_float = qt.QCheckBox("Omega no float")
        self._omega_slop = qt.QLineEdit("")
        self._omega_slop.setValidator(validator)
        self._latticeCB = qt.QComboBox(parent=self)
        self._latticeCB.addItems(Lattice.values())
        self._plot1 = PlotWindow(self)
        self._plot1.hide()
        self._plot2 = PlotWindow(self)
        self._plot2.hide()
        thresh_widget = qt.QWidget()
        thresh_layout = qt.QHBoxLayout()
        thresh_layout.addWidget(qt.QLabel("Thresholds:"))
        thresh_layout.addWidget(self._thresholdsCB)
        thresh_layout.addWidget(self._loadPeaks)
        thresh_layout.addWidget(self._tolerance)
        thresh_widget.setLayout(thresh_layout)
        layout.addWidget(thresh_widget, 0, 0, 1, 2)
        layout.addWidget(qt.QLabel("Tolerance:"), 0, 2)
        layout.addWidget(self._tolerance, 0, 3)
        layout.addWidget(qt.QLabel("Lattice:"), 0, 4)
        layout.addWidget(self._latticeCB, 0, 5)
        omega_layout = qt.QHBoxLayout()
        omega_widget = qt.QWidget()
        omega_layout.addWidget(qt.QLabel("Omega slop:"))
        omega_layout.addWidget(self._omega_slop)
        omega_widget.setLayout(omega_layout)
        layout.addWidget(omega_widget, 1, 0, 1, 2)
        layout.addWidget(self._omega_no_float, 1, 3)
        layout.addWidget(qt.QLabel("Tth range:"), 1, 2)
        layout.addWidget(self._tth_range, 1, 3)
        layout.addWidget(self._parametersFilename, 2, 0, 1, 3)
        layout.addWidget(self._ubiFilename, 2, 3, 1, 3)
        layout.addWidget(self._newUbiFilename, 3, 0, 1, 3)
        layout.addWidget(self._fltFilename, 3, 3, 1, 3)
        layout.addWidget(self._computeB, 7, 1, 1, 4)
        self._plot1.setMinimumHeight(200)
        layout.addWidget(self._plot1, 4, 0, 3, 3)
        layout.addWidget(self._plot2, 4, 3, 3, 3)
        layout.addWidget(self._no_sort, 1, 4)
        self.setLayout(layout)

    def setDataset(self, dataset):
        """
        Set dataset and fill thresholdsCB with dataset's peaks files.
        """
        self.dataset = dataset
        oldState = self._thresholdsCB.blockSignals(True)
        self._thresholdsCB.clear()
        self._thresholdsCB.blockSignals(oldState)
        self._thresholdsCB.addItems(
            [str(peaks.threshold) for peaks in self.dataset.peaks_groups]
        )
        self._loadPeaks.setEnabled(True)
        self._computeB.setEnabled(True)

        if self.dataset.peaks_groups[0].parameters is not None:
            self._parametersFilename.setFilename(
                self.dataset.peaks_groups[0].parameters
            )
        if self.dataset.peaks_groups[0].ubi_file is not None:
            self._parametersFilename.setFilename(
                self.dataset.peaks_groups[0].ubi_file
            )

    def _changeThreshold(self, index):
        """
        Peak new file with different threshold peaks.
        """
        if self.dataset is None:
            threshold = self._thresholdsCB.currentText()
            self.peaksFile = self._thresholds[threshold]
        else:
            peaks = self.dataset.peaks_groups[index]
            self.peaksFile = peaks.flt_file
            if peaks is not None:
                self._parametersFilename.setFilename(
                    peaks.parameters if peaks.parameters is not None else ""
                )
                self._ubiFilename.setFilename(
                    peaks.ubi_file if peaks.ubi_file is not None else ""
                )

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
                if self.dataset is None:
                    self._thresholds[threshold] = filename
                    self._thresholdsCB.addItem(threshold)
                    self._thresholdsCB.setCurrentText(threshold)
                else:
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
                print("Could not find threshold in filename")
        else:
            _logger.warning("Could not open file")

    def compute(self):
        """
        Compute refinement of grains positions and plot histograms of the before
        and the after.
        """
        assert (
            self._ubiFilename.getFilename() and self._ubiFilename.getFilename()
        ), "Parameters file and UBI file must be given"
        omega_float = self._omega_no_float.isChecked()
        omega_slop = self._omega_slop.text()
        omega_slop = float(omega_slop) if omega_slop else None
        tthr = str(self._tth_range.text())
        tth_range = (float(tthr[1]), float(tthr[-2]))

        try:
            # func = getattr(ImageD11.refinegrains, self.latticesymmetry)
            refiner = refinegrains(
                intensity_tth_range=tth_range, OmFloat=omega_float, OmSlop=omega_slop
            )
        except Exception:
            raise
            refiner = refinegrains()

        refiner.loadparameters(self._parametersFilename.getFilename())
        refiner.loadfiltered(self.peaksFile)
        refiner.readubis(self._ubiFilename.getFilename())
        symmetry = self._latticeCB.currentText()
        if symmetry != "triclinic":
            # Grainspotter will have already done this
            refiner.makeuniq(symmetry)
        refiner.tolerance = float(self._tolerance.text())
        refiner.generate_grains()
        refiner.refinepositions()
        # o.refineubis(quiet = False , scoreonly = True)
        newubi = (
            self._newUbiFilename.getFilename()
            if self._newUbiFilename.getFilename()
            else self._ubiFilename.getFilename()[:-4] + ".map"
        )
        newflt = (
            self._fltFilename.getFilename()
            if self._fltFilename.getFilename()
            else self.peaksFile[:-4] + ".new"
        )
        sort = not self._no_sort.isChecked()
        refiner.savegrains(newubi, sort_npks=sort)
        refiner.scandata[self.peaksFile].writefile(newflt)

        self.plot_grain_hist(
            self._plot1, self.peaksFile, self._ubiFilename.getFilename()
        )
        self.plot_grain_hist(self._plot2, self.peaksFile, newubi)

        self._plot1.show()
        self._plot2.show()

    def plot_grain_hist(self, plot, peaks_file, ubis_file):
        """
        Plot histogram of data corresponding to the fitted grains.

        :param plot: widget where to plot the different data.
        :param peaks_file: filename with the peaks.
        :param ubis_file: filename with the UBI matrices.
        """
        refinement = refinegrains(OmFloat=False)
        refinement.loadparameters(self._parametersFilename.getFilename())
        refinement.readubis(ubis_file)
        refinement.loadfiltered(peaks_file)
        refinement.tolerance = float(self._tolerance.text())
        refinement.generate_grains()
        refinement.assignlabels()
        data = refinement.scandata[peaks_file]
        data.filter(data.labels >= 0)
        drlv_bins = numpy.linspace(0, float(self._tolerance.text()), 15)
        ng = int(data.labels.max()) + 1
        drlv = numpy.sqrt(data.drlv2)
        dp5 = [drlv[data.labels == i] for i in range(ng)]
        hl = [numpy.histogram(dpi, drlv_bins)[0] for dpi in dp5]
        if drlv_bins.shape[0] != hl[0].shape[0]:
            plotbins = (drlv_bins[1:] + drlv_bins[:-1]) / 2
        for i in range(ng):
            plot.addCurve(plotbins, hl[i], legend=str(i))
