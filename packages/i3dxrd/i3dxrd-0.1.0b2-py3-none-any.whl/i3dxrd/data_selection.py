from typing import Iterable, Optional, Union
from i3dxrd.dataset import Dataset


def load_process_data(
    filenames: Union[str, Iterable[str]] = None,
    nframes: Optional[int] = None,
    in_memory: bool = True,
    dark_filename: Optional[str] = None,
    flood_filename: Optional[str] = None,
    spline_filename: Optional[str] = None,
    isH5: bool = False,
):
    """When `filenames` is a string, it will be treated as a file pattern."""

    if isinstance(filenames, str):
        dataset = Dataset(
            first_filename=filenames,
            in_memory=in_memory,
            dark_filename=dark_filename,
            flood_filename=flood_filename,
            spline_filename=spline_filename,
            isH5=isH5,
        )
    else:
        filenames = list(filenames)
        dataset = Dataset(
            filenames=filenames,
            in_memory=in_memory,
            dark_filename=dark_filename,
            flood_filename=flood_filename,
            spline_filename=spline_filename,
            isH5=isH5,
        )

    return dataset
