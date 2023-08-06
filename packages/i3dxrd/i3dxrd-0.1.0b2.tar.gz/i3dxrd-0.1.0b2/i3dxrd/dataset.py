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
__date__ = "02/12/2020"

import os

import fabio

import numpy

from fabio.fabioimage import fabioimage
from ImageD11 import blobcorrector
from ImageD11.correct import correct
from ImageD11.labelimage import labelimage
from ImageD11.peaksearcher import peaksearch
import silx
from silx.io.url import DataUrl
from darfix.core.dataset import Data


class Dataset:
    """Class to define a dataset from a series of data files.

    :param str first_filename: First filename of the series of files to read.
    :param int nframes: Number of frames to read.
    :param list filenames: Ordered list of filenames, defaults to None.
    :type filenames: Union[Generator,Iterator,List], optional
    :param str dark_filename: Filename for dark file.
    :param str flood_filename: Filename for flood file.
    :param str spline_filename: Filename for spline file.
    :param in_memory: If True, data is loaded into memory, else, data is read in
        chunks depending on the algorithm to apply, defaults to False.
    :type in_memory: bool, optional
    """

    def __init__(
        self,
        first_filename=None,
        nframes=None,
        filenames=None,
        dark_filename=None,
        flood_filename=None,
        spline_filename=None,
        isH5=False,
        in_memory=False,
    ):

        assert (
            first_filename is not None or filenames is not None
        ), "\
            Either first filename or filename must be given"
        self._peaks_groups = []
        self._dark_filename = dark_filename
        self._flood_filename = flood_filename
        self._spline_filename = spline_filename
        self._isH5 = isH5
        self._in_memory = in_memory

        metadata = []
        data_urls = []

        if self._isH5:
            url = DataUrl(first_filename)
            with silx.io.open(url.file_path()) as h5:
                rot = h5["entry0000/sample/rotation_angle"][:] % 360
                # rocking = h5['entry0000/sample/rocking'][:]
                # n_steps_rotation = h5['entry0000/sample/n_steps_rotation'][0]
                # n_steps_rocking = h5['entry0000/sample/n_steps_rocking']
                for i in range(h5[url.data_path()].shape[0]):
                    data_urls.append(
                        DataUrl(
                            file_path=url.file_path(),
                            data_path=url.data_path(),
                            data_slice=i,
                            scheme="silx",
                        )
                    )
                    metadata.append({"Omega": rot[i]})
        else:
            with fabio.open_series(
                filenames=filenames, first_filename=first_filename
            ) as series:
                for frame in series.frames():
                    filename = frame.file_container.filename
                    data_urls.append(DataUrl(file_path=filename, scheme="fabio"))
                    metadata.append(frame.header)

        self._data = Data_3DXRD(
            numpy.array(data_urls), metadata=metadata, in_memory=self._in_memory
        )

    @property
    def file_series(self):
        return self._file_series

    @property
    def nframes(self):
        """
        Return number of frames
        """
        if self.data is None:
            return 0
        else:
            return len(self.data.flatten())

    @property
    def peaks_groups(self):
        return self._peaks_groups

    def add_peaks(self, threshold, flt_file=None, spt_file=None):
        peaks = PeaksData(threshold)
        peaks.flt_file = flt_file
        peaks.spt_file = spt_file
        self._peaks_groups.append(peaks)
        return peaks

    @property
    def in_memory(self):
        return self._data.in_memory

    @property
    def data(self):
        return self._data

    def get_frame(self, i):
        return self._data[i]

    def compute_background(self, bg_filename="background.edf", step=1):
        """Function that computes the background from the dataset data by
        applying the median.

        :param str bg_filename: filename to use as output for the background
        :param int step: spacing between values, defaults to 1.
        :returns: ndarray
        :raises: ValueError
        """
        background = numpy.zeros(self._data[0].shape, self._data.dtype)
        if self.in_memory:
            numpy.median(self.data, out=background, axis=0)
        else:
            indices = numpy.arange(0, len(self.data), step)
            numpy.median(
                Data(self.data.urls[indices], self.data.metadata[indices]),
                out=background, axis=0)

        im = fabio.edfimage.edfimage(data=background)
        try:
            im.write(bg_filename, force_type=im.data.dtype)
        except TypeError:
            im.write(bg_filename)

        return background

    def peak_search(
        self, thresholds, out_file, OMEGA=0, OMEGAOVERRIDE=True, OMEGASTEP=1
    ):
        """
        Method to compute peak search as done in ImageD11.
        """

        li_objs = {}  # label image objects, dict of

        s = self._data[0].shape  # data array shape
        # Output files:
        if out_file[-4:] != ".spt":
            out_file = out_file + ".spt"
            print("Your output file must end with .spt, changing to ", out_file)

        if self._spline_filename is not None and os.path.exists(self._spline_filename):
            print("Using spatial from", self._spline_filename)
            corr_func = blobcorrector.correctorclass(self._spline_filename)
        else:
            print("Avoiding spatial correction")
            corr_func = blobcorrector.perfect()

        # Create label images
        for t in thresholds:
            # the last 4 chars are guaranteed to be .spt above
            mergefile = "%s_t%d.flt" % (out_file[:-4], t)
            spotfile = "%s_t%d.spt" % (out_file[:-4], t)
            li_objs[t] = labelimage(
                shape=s, fileout=mergefile, spatial=corr_func, sptfile=spotfile
            )
            print("make labelimage", mergefile, spotfile)

        for i in range(len(self._data)):
            data_object = fabioimage(self._data[i], self._data.metadata[i])
            # t = timer()
            filein = self._data.urls[i]
            if OMEGAOVERRIDE or "Omega" not in data_object.header:
                data_object.header["Omega"] = OMEGA
                OMEGA += OMEGASTEP
                OMEGAOVERRIDE = True  # once you do it once, continue
            # TODO: add median, monitorval and monitorcol
            data_object = correct(
                data_object, self._dark_filename, self._flood_filename
            )
            # t.tick(filein+" io/cor")
            peaksearch(filein, data_object, corr_func, thresholds, li_objs)
        for t in li_objs:
            self.add_peaks(t, li_objs[t].outfile.name, li_objs[t].sptfile.name)


class Data_3DXRD(Data):
    def __new__(cls, urls, metadata, in_memory=True):
        obj = super(Data_3DXRD, cls).__new__(cls, urls, metadata, in_memory)

        obj._subtract_background = False

        return obj

    def __array_finalize__(self, obj):
        if obj is None:
            return
        self.urls = getattr(obj, "urls", None)
        self.metadata = getattr(obj, "metadata", None)
        self.in_memory = getattr(obj, "in_memory", None)
        self._subtract_background = getattr(obj, "_subtract_background", None)

    @property
    def subtract_background(self):
        return self._subtract_background

    @subtract_background.setter
    def subtract_background(self, subtract_background):
        self._subtract_background = subtract_background

    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, background):
        self._background = background
        self._subtract_background = True

    def __subtract_background(self, data):
        if data.dtype.kind == "i" or data.dtype.kind == "u":
            new_data = numpy.subtract(
                data, self.background.astype(data.dtype), dtype=numpy.int64
            )
        else:
            new_data = numpy.subtract(data, self.background.astype(data.dtype))
        new_data[new_data < 0] = 0

        return new_data.astype(data.dtype)


class PeaksData:
    def __init__(self, threshold):

        self._threshold = threshold
        self._flt_file = None
        self._spt_file = None
        self._parameters = None
        self._ubi_file = None
        self._gvectors = None

    @property
    def parameters(self):
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        self._parameters = parameters

    @property
    def ubi_file(self):
        return self._ubi_file

    @ubi_file.setter
    def ubi_file(self, ubi_file):
        self._ubi_file = ubi_file

    @property
    def gvectors(self):
        return self._gvectors

    @gvectors.setter
    def gvectors(self, gvectors):
        self._gvectors = gvectors

    @property
    def threshold(self):
        return self._threshold

    @property
    def flt_file(self):
        return self._flt_file

    @flt_file.setter
    def flt_file(self, flt_file):
        self._flt_file = flt_file

    @property
    def spt_file(self):
        return self._spt_file

    @spt_file.setter
    def spt_file(self, spt_file):
        self._spt_file = spt_file
