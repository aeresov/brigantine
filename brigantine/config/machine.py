"""Machine config assembly."""

from pydantic import BaseModel
from .mcu import MCU


class Machine(BaseModel):
    mcu: list[MCU]
