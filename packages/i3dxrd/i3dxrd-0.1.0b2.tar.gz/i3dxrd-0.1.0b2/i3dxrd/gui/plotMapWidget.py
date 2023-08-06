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
__date__ = "14/08/2020"

import logging
import numpy

from silx.gui import qt
from ImageD11.grain import read_grain_file
from silx.gui.plot3d.SceneWindow import SceneWindow
from silx.gui.plot3d import items
from .dataSelectionWidget import FilenameSelectionWidget

_logger = logging.getLogger(__file__)


class PlotMapWidget(qt.QMainWindow):
    """
    Widget for calibrating the parameters. It shows in a scatterView the tth and eta values of the data,
    to help the user perform the calibration.
    """

    def __init__(self, parent=None):
        qt.QMainWindow.__init__(self, parent)

        widget = qt.QWidget()
        layout = qt.QVBoxLayout()
        self._grainFile = FilenameSelectionWidget(
            "Open grain file", parent=self, fileMode=qt.QFileDialog.ExistingFile
        )
        self._compute = qt.QPushButton("Compute", parent=self)
        self._compute.pressed.connect(self._loadGrains)
        layout.addWidget(self._grainFile)
        layout.addWidget(self._compute)

        # Create a SceneWindow
        self._window = SceneWindow(self)

        sceneWidget = self._window.getSceneWidget()
        sceneWidget.setBackgroundColor((0.8, 0.8, 0.8, 1.0))
        sceneWidget.setForegroundColor((1.0, 1.0, 1.0, 1.0))
        sceneWidget.setTextColor((0.1, 0.1, 0.1, 1.0))
        self._scatter3D = items.Scatter3D()
        self._scatter3D.setSymbol("x")
        self._scatter3D.getColormap().setName("temperature")  # Use 'magma' colormap
        SIZE = 1024
        self._scatter3D.setScale(SIZE, SIZE, SIZE)
        self._scatter3D.setSymbolSize(11)  # Set the size of the markers
        sceneWidget.addItem(self._scatter3D)
        self._window.hide()
        layout.addWidget(self._window)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def _loadGrains(self):
        """
        Load grains from file
        """
        grain_file = read_grain_file(self._grainFile.getFilename())

        data = []
        intensity = []

        for g in grain_file:
            o = g.translation
            try:
                sf = pow(numpy.median(g.intensity_info), 0.3333)
            except Exception:
                sf = 1.0
            try:
                k = int(g.npks)
            except Exception:
                k = 1
            for u in g.ubi:
                data.append(o)
                data.append(o + u * sf)
                intensity.append(k)
                intensity.append(k)
            for u in g.ubi:
                data.append(o)
                data.append(o - u * sf)
                intensity.append(k)
                intensity.append(k)

        data = numpy.array(data).T
        self._scatter3D.setData(data[0], data[1], data[2], intensity)
        self._window.show()
