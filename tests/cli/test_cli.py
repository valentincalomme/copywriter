import semver
from typer.testing import CliRunner

from copywriter.cli.application import app


class TestCliApplication:
    """Collection of CLI tests."""

    runner = CliRunner()

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
