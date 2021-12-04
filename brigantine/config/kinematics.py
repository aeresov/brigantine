"""Types of printer kinematics."""

from typing import Any, Dict, List, Literal, Optional, Union

from pydantic import BaseModel, root_validator

from brigantine.config.common import GPIOPin


class Stepper(BaseModel):
    step_pin: GPIOPin
    dir_pin: GPIOPin
    enable_pin: GPIOPin
    rotation_distance: int
    microsteps: int
    full_steps_per_rotation: Literal[200, 400]
    gear_ratio: str


class DeltaStepper(Stepper):
    arm_length: int
    angle: Optional[int] = None


class XYZGeometry(BaseModel):
    X: List[Stepper]
    Y: List[Stepper]
    Z: List[Stepper]


class DeltaGeometry(BaseModel):
    A: DeltaStepper
    B: DeltaStepper
    C: DeltaStepper

    @root_validator
    def inject_defaults(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        # angles are 210-330-90
        if not values["A"]["angle"]:
            values["A"]["angle"] = 210
        if not values["B"]["angle"]:
            values["B"]["angle"] = 330
        if not values["C"]["angle"]:
            values["C"]["angle"] = 90
        return values


class Cartesian(BaseModel):
    cartesian: XYZGeometry


class CoreXY(BaseModel):
    corexy: XYZGeometry


class CoreXZ(BaseModel):
    corexz: XYZGeometry


class HybridCoreXY(BaseModel):
    hybrid_corexy: XYZGeometry


class HybridCoreXZ(BaseModel):
    hybrid_corexz: XYZGeometry


class Delta(DeltaGeometry):
    delta_radius: int
    print_radius: Optional[int] = None
    minimum_z_position: int = 0

    @root_validator
    def inject_defaults(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        if not values["print_radius"]:
            values["print_radius"] = values["delta_radius"]
        return values


class Delta(BaseModel):
    delta: DeltaGeometry


class Kinematics(BaseModel):
    geometry: Union[Cartesian, CoreXY]
    max_velocity: int
    max_accel: int
    max_accel_to_decel: Optional[int] = None
    square_corner_velocity: int = 5
    max_z_velocity: Optional[int] = None
    max_z_accel: Optional[int] = None

    @root_validator
    def inject_defaults(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        if not values["max_z_velocity"]:
            values["max_z_velocity"] = values["max_velocity"]
        if not values["max_z_accel"]:
            values["max_z_velocity"] = values["max_accel"]
        return values
