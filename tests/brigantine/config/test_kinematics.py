from hypothesis import given, strategies

from brigantine.config.kinematics import Kinematics


@given(strategies.builds(Kinematics))
def test_kinematics(value: Kinematics):
    pass
