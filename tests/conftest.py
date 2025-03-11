import pytest
from app import create_app, db
from dotenv import load_dotenv

from config.config_tests import ConfigTests

@pytest.fixture
def client():
    app = create_app(ConfigTests())

    with app.test_client() as client:
        yield client
