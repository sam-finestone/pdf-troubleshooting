# tests/conftest.py
import pytest
import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app import create_app


@pytest.fixture(scope="module")
def app():
    """Create and configure a new app instance for each test."""
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
            "WTF_CSRF_ENABLED": False,  # Disable CSRF tokens for simplicity.
        }
    )
    yield app


@pytest.fixture(scope="module")
def client(app):
    """A test client for the app."""
    return app.test_client()
