from hypothesis import given, strategies

from brigantine.config.common import GPIOPin, Rect, Volume
from brigantine.config.kinematics import Kinematics
from brigantine.config.mcu import MCU


@given(strategies.builds(Kinematics))
def test_kinematics(value: Kinematics):
    pass


@given(strategies.builds(MCU))
def test_mcu(value: MCU):
    pass


@given(strategies.builds(GPIOPin))
def test_gpioping(value: GPIOPin):
    pass


@given(strategies.builds(Rect))
def test_rect(value: Rect):
    pass


@given(strategies.builds(Volume))
def test_rect(value: Volume):
    pass
