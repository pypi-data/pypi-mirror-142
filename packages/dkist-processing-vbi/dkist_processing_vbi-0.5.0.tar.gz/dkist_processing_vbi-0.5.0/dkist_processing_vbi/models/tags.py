"""VBI specific tags."""
from enum import Enum

from dkist_processing_common.models.tags import Tag


class VbiStemName(str, Enum):
    """Stem names for VBI tags."""

    current_spatial_step = "STEP"


class VbiTag(Tag):
    """Tag names for VBI tags."""

    @classmethod
    def spatial_step(cls, step_num: int) -> str:
        """VBI tag for which spatial step is being observed."""
        return cls.format_tag(VbiStemName.current_spatial_step, step_num)
