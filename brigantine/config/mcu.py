"""MCU config block."""

from typing import Union
from pydantic import BaseModel
from enum import Enum


class SerialComms(BaseModel):
    serial: str


class CANComms(BaseModel):
    interface: str = "can0"
    uuid: str


class Comms(BaseModel):
    __root__: Union[SerialComms, CANComms]


class RestartMethod(str, Enum):
    arduino = "arduino"
    cheetah = "cheetah"
    rpi_usb = "rpi_usb"
    command = "command"


class MCU(BaseModel):
    name: str
    comms: Comms
    baud: int
    restart_method: RestartMethod = RestartMethod.command
