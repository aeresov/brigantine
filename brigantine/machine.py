"""Machine (3d printer) entity."""

from dataclasses import dataclass
from typing import Optional

from brigantine.config.common import Rect, Volume


@dataclass(frozen=True)
class Pos:
    """Head position.

    Coordinate is None if not homed (when requested from printer)
    or if corresponding axis movement is not required
    (when sent to printer).
    """

    x: Optional[float] = None
    y: Optional[float] = None
    z: Optional[float] = None


class Machine:
    @property
    def move_area(self) -> Volume:
        pass

    @property
    def print_area(self) -> Rect:
        pass

    @property
    def current_pos(self) -> Pos:
        pass
