"""Tools for loading config."""

import yaml
from .machine import Machine
from pathlib import Path


def load(filename: Path) -> Machine:
    with filename.open(mode="r", encoding="UTF-8") as file:
        config_data = yaml.safe_load(file)
        return Machine.parse_obj(config_data)
