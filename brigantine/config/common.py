"""Commonly used models."""

from pydantic import BaseModel, constr


class GPIOPin(BaseModel):
    """Model for GPIO pin name.

    This is expected as controller-defined pin name,
    Prepended with "!" if negation is needed, and
    with "^" or "~" if pullup or pulldown is needed.
    """

    __root__: constr(regex=r"^(\!(?!.*\!)){0,1}(\^|~){0,1}(\w+)$")
