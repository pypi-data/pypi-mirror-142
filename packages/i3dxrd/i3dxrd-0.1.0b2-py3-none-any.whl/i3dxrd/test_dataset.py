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
__date__ = "17/07/2020"

import fabio
import unittest
import numpy
import os
import tempfile

from i3dxrd.dataset import Dataset


class TestDataset(unittest.TestCase):

    """Tests for class Dataset in `dataset.py`"""

    def setUp(self):
        _dir = tempfile.mkdtemp()
        for index in range(10):
            data_file = os.path.join(_dir, "data_file%04i.edf" % index)
            data = numpy.ones((100, 100))
            data[25:50, 25:50] = numpy.random.random((25, 25))
            image = fabio.edfimage.EdfImage(data=data)
            image.write(data_file)

        self.dataset = Dataset(first_filename=_dir + "/data_file0000.edf", in_memory=True)
        self.dataset2 = Dataset(
            first_filename=_dir + "/data_file0000.edf", in_memory=False
        )

    def test_nframes(self):
        """Tests the nframes method"""
        self.assertEqual(self.dataset.nframes, 10)

    def test_bs(self):
        background1 = self.dataset.compute_background()
        background2 = self.dataset2.compute_background()

        numpy.testing.assert_array_equal(background1, background2)
