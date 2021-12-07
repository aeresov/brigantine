"""Commonly used models."""

from typing import Any, Dict, Optional

from pydantic import BaseModel, conint, constr, validator
from pydantic.fields import ModelField


class Rect(BaseModel):
    """Model for common XY rectangle."""

    x_max: conint(strict=True, gt=0)
    y_max: conint(strict=True, gt=0)
    x_min: conint(strict=True, ge=0) = 0
    y_min: conint(strict=True, ge=0) = 0

    def width(self) -> int:
        return self.x_max - self.x_min

    def depth(self) -> int:
        return self.y_max - self.y_min

    @validator("x_max")
    @classmethod
    def rect_makes_sense(cls, v: Any, values: Dict[str, Any]):
        x_min: Optional[int] = values.get("x_min", None)
        if x_min and (v - x_min) <= 0:
            raise ValueError("invalid rect width")
        return values

    @validator("y_max")
    @classmethod
    def rect_makes_sense(cls, v: Any, values: Dict[str, Any]):
        y_min: Optional[int] = values.get("y_min", None)
        if y_min and (v - y_min) <= 0:
            raise ValueError("invalid rect depth")
        return values


class Volume(Rect):
    """Model for XYZ box."""

    z_max: conint(strict=True, gt=0)
    z_min: conint(strict=True, ge=0) = 0

    def height(self) -> int:
        return self.z_max - self.z_min

    @validator("z_max")
    @classmethod
    def rect_makes_sense(cls, v: Any, values: Dict[str, Any]):
        z_min: Optional[int] = values.get("z_min", None)
        if z_min and (v - z_min) <= 0:
            raise ValueError("invalid rect height")
        return values




class GPIOPin(BaseModel):
    """Model for GPIO pin name.

    This is expected as controller-defined pin name,
    Prepended with "!" if negation is needed, and
    with "^" or "~" if pullup or pulldown is needed.
    """

    __root__: constr(regex=r"^(\!(?!.*\!)){0,1}(\^|~){0,1}(\w+)$")
