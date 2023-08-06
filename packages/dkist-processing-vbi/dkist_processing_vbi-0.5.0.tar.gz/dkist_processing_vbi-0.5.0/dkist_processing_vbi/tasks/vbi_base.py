"""VBI base task class."""
from abc import ABC

from dkist_processing_common.tasks import WorkflowTaskBase

from dkist_processing_vbi.models.constants import VbiConstants


class VbiTaskBase(WorkflowTaskBase, ABC):
    """Base task that all VBI tasks should inherit from."""

    @property
    def constants_model_class(self):
        """VBI constants."""
        return VbiConstants
