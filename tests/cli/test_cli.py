import subprocess
import sys

import pytest
import semver
from typer.testing import CliRunner

from copywriter.cli.application import app


class TestCliApplication:
    """Collection of CLI tests."""

    runner = CliRunner()

    @pytest.mark.xfail(
        reason="Known bug when testing on Windows, see https://github.com/ValentinCalomme/copywriter/issues/12",
        condition=sys.platform == "win32",
    )
    def test_entrypoint(self) -> None:
        """Check that we can call the commandline directly."""
        subprocess.run(["copywriter", "--help"], capture_output=True, text=True)  # noqa:S603,S607

    def test_help(self) -> None:
        """Check that the application's help command doesn't crash."""
        result = self.runner.invoke(app=app, args="--help")
        assert result.exit_code == 0

    def test_about(self) -> None:
        """Ensures the about command doesn't crash."""
        result = self.runner.invoke(app=app, args="about")
        assert result.exit_code == 0
        assert len(result.output) > 0

    def test_version(self) -> None:
        """Ensures the version command doesn't crash."""
        result = self.runner.invoke(app=app, args="version")
        assert result.exit_code == 0
        assert semver.Version.parse(result.output)
