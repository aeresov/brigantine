"""Machine config assembly."""

from pydantic import BaseModel

from brigantine.config.kinematics import Kinematics

from .mcu import MCU


class Machine(BaseModel):
    mcu: list[MCU]
    kinematics: Kinematics
