"""VBI Quality Metrics."""
from typing import Generator

from dkist_processing_common.parsers.quality import L0QualityFitsAccess
from dkist_processing_common.parsers.quality import L1QualityFitsAccess
from dkist_processing_common.tasks import QualityL0Metrics
from dkist_processing_common.tasks import WorkflowTaskBase
from dkist_processing_common.tasks.mixin.fits import FitsDataMixin
from dkist_processing_common.tasks.mixin.quality import QualityMixin

from dkist_processing_vbi.models.tags import VbiTag


class VbiQualityL0Metrics(QualityL0Metrics):
    """L0 VBI-specific quality metrics."""

    def run(self) -> None:
        """Contains the steps to run this task."""
        frames: Generator[L0QualityFitsAccess, None, None] = self.fits_data_read_fits_access(
            tags=[VbiTag.input()],
            cls=L0QualityFitsAccess,
        )
        self.calculate_l0_metrics(frames=frames)


class VbiQualityL1Metrics(WorkflowTaskBase, QualityMixin, FitsDataMixin):
    """L1 VBI-specific quality metrics."""

    def run(self):
        """Contains the steps to run this task."""
        frames = self.fits_data_read_fits_access(
            tags=[
                VbiTag.output(),
                VbiTag.frame(),
            ],
            cls=L1QualityFitsAccess,
        )
        datetimes = []
        noise_values = []
        for frame in frames:
            datetimes.append(frame.time_obs)
            noise_values.append(self.avg_noise(frame.data))
        self.quality_store_noise(datetimes=datetimes, values=noise_values)
