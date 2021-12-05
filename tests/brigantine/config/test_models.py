from hypothesis import given, strategies

from brigantine.config.kinematics import Kinematics
from brigantine.config.mcu import MCU
from brigantine.config.common import GPIOPin


@given(strategies.builds(Kinematics))
def test_kinematics(value: Kinematics):
    pass


@given(strategies.builds(MCU))
def test_mcu(value: MCU):
    pass


@given(strategies.builds(GPIOPin))
def test_gpioping(value: GPIOPin):
    pass

