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
__date__ = "30/07/2020"

from Orange.widgets.widget import OWWidget, Input, Output

from silx.gui import qt

from i3dxrd.dataset import Dataset
from i3dxrd.gui.peakSearchWidget import PeakSearchWidget


class PeakSearchWidgetOW(OWWidget):
    """
    Widget to select the data to be used in the dataset.
    """

    name = "peak search"
    # icon = "icons/upload.svg"
    want_main_area = False

    # Inputs
    class Inputs:
        dataset = Input("dataset", Dataset)

    # Outputs
    class Outputs:
        dataset = Output("dataset", Dataset)

    def __init__(self):
        super().__init__()

        self._widget = PeakSearchWidget()
        types = qt.QDialogButtonBox.Ok
        _buttons = qt.QDialogButtonBox(parent=self)
        _buttons.setStandardButtons(types)

        self.controlArea.layout().addWidget(self._widget)
        self.controlArea.layout().addWidget(_buttons)

        _buttons.accepted.connect(self.close)

        self.__updatingData = False

    @Inputs.dataset
    def setDataset(self, dataset):
        self.show()
        if dataset:
            self._widget.setDataset(dataset)
        else:
            # Emit None
            self.Outputs.dataset.send(dataset)

    def closeEvent(self, event):
        self.Outputs.dataset.send(self._widget.dataset)
        event.accept()
