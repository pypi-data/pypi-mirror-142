from numato_cli import __version__
from typer.testing import CliRunner
from .__main__ import app

runner = CliRunner()


def test_version():
    assert __version__ == "0.1.0"


def test_discover():
    result = runner.invoke(app)
    assert result.exit_code == 0
    assert "Discovered devices: " in result.stdout
