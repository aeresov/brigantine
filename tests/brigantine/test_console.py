from typer.testing import CliRunner
from brigantine.console import app

runner = CliRunner()


def test_app():
    result = runner.invoke(app, ["goodbye", "Alex", "--formal"])
    assert result.exit_code == 0
    assert "Have a good day" in result.stdout
