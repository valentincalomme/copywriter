"""These tests are meant to check whether certain imports are valid.

This is a way to ensure that the package namespacing doesn't get messed
with and that every important import remains valid.
"""

import importlib


def test_import_copywriter() -> None:
    """Ensures that the main package is importable."""
    importlib.import_module("copywriter")
