from fabio.fabioimage import fabioimage
import numpy as np
import h5py


def fso(filename, dataset):
    with h5py.File(filename, "r") as h:
        omega = h["/1.1/measurement/diffrz"][:] % 360  # forwards scan
        nframes = len(omega)
        data = h[dataset]
        assert data.shape[0] == nframes
        header = {"Omega": omega[0]}
        filename = "%s::%s" % (filename, dataset)
        order = np.argsort(omega)

        def frm(i):
            header["Omega"] = omega[i]
            f = fabioimage(data[i], header)
            f.filename = filename
            f.currentframe = i
            return f

        yield (frm(order[0]))  # first
        for i in order:
            yield frm(i)
