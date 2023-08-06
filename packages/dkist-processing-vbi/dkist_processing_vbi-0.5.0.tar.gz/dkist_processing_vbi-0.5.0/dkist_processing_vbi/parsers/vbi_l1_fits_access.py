"""Access class for L1 VBI FITS data."""
from typing import Optional
from typing import Union

from astropy.io import fits
from dkist_processing_common.parsers.l1_fits_access import L1FitsAccess


class VbiL1FitsAccess(L1FitsAccess):
    """Access class for L0 VBI FITS data."""

    def __init__(
        self,
        hdu: Union[fits.ImageHDU, fits.PrimaryHDU, fits.CompImageHDU],
        name: Optional[str] = None,
        auto_squeeze: bool = True,
    ):
        super().__init__(hdu=hdu, name=name, auto_squeeze=auto_squeeze)

        self.number_of_spatial_steps: int = self.header.get("VBINSTP")
        self.current_spatial_step: int = self.header.get("VBISTP")
