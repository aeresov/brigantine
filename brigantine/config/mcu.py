"""MCU config block."""

from enum import Enum
from typing import Literal, Union

from pydantic import BaseModel


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
    baud: Literal[
        256000,
        250000,
        230400,
        128000,
        115200,
        76800,
        57600,
        56000,
        38400,
        31250,
        19200,
        14400,
        9600,
        7200,
        4800,
        2400,
        1800,
        1200,
        600,
        300,
        150,
        110,
        75,
    ]
    restart_method: RestartMethod = RestartMethod.command
