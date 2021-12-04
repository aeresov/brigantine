from pydantic import BaseModel


class GPIOPin(BaseModel):
    __root__: str
