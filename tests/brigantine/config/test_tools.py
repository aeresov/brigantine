from pathlib import Path
from brigantine.config.tools import load
import pytest


@pytest.mark.parametrize("filename", [Path("tests/assets/config_good.yaml")])
def test_load(filename: Path):
    machine = load(filename)
