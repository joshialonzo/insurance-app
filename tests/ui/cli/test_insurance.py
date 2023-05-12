# tests/ui/cli/test_insurance.py

from typer.testing import CliRunner

from insurance.ui.cli import __app_name__, __version__, app


runner = CliRunner()


def test_version():
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} version {__version__}" in result.stdout
