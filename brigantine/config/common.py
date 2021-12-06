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

    def height(self) -> int:
        return self.y_max - self.y_min

    @validator("x_max", "y_max")
    @classmethod
    def rect_makes_sense(cls, v: Any, field: ModelField, values: Dict[str, Any]):
        match field.name:
            case "x_max":
                x_min: Optional[int] = values.get("x_min", None)
                if x_min and (v - x_min) <= 0:
                    raise ValueError("invalid rect width")
            case "y_max":
                y_min: Optional[int] = values.get("y_min", None)
                if y_min and (v - y_min) <= 0:
                    raise ValueError("invalid rect height")
        return values



class GPIOPin(BaseModel):
    """Model for GPIO pin name.

    This is expected as controller-defined pin name,
    Prepended with "!" if negation is needed, and
    with "^" or "~" if pullup or pulldown is needed.
    """

    __root__: constr(regex=r"^(\!(?!.*\!)){0,1}(\^|~){0,1}(\w+)$")
