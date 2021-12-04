from hypothesis import given, strategies

from brigantine.config.mcu import MCU


@given(strategies.builds(MCU))
def test_mcu(value: MCU):
    pass
