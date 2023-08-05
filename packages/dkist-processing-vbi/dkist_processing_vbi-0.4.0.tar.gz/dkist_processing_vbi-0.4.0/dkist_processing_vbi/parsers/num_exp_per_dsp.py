"""Bud to find number of exposures in a DSP."""
from dkist_processing_common.models.flower_pot import SpilledDirt
from dkist_processing_common.parsers.unique_bud import UniqueBud

from dkist_processing_vbi.models.constants import VbiBudName
from dkist_processing_vbi.parsers.vbi_l0_fits_access import VbiL0FitsAccess


class NumExpPerDspBud(UniqueBud):
    """Bud to find number of exposures in a DSP."""

    def __init__(self):
        super().__init__(
            constant_name=VbiBudName.num_exp_per_dsp.value, metadata_key="number_of_exp_per_dsp"
        )

    def setter(self, fits_obj: VbiL0FitsAccess):
        """Only set the bud value when an observe frame is used."""
        if fits_obj.ip_task_type.lower() != "observe":
            return SpilledDirt
        return super().setter(fits_obj)
