
import pytest
import os
from time import sleep

from dotenv import load_dotenv

from gspread_models.service import SpreadsheetService
from gspread_models.base import BaseModel

from app.db import GOOGLE_CREDENTIALS_FILEPATH

from web_app import create_app

load_dotenv()

# an example sheet that is being used for testing purposes:
GOOGLE_SHEETS_TEST_DOCUMENT_ID= os.getenv("GOOGLE_SHEETS_TEST_DOCUMENT_ID")
TEST_SLEEP = int(os.getenv("TEST_SLEEP", default="3"))

@pytest.fixture()
def service():
    """Spreadsheet service connected to the test document. Sleeps to avoid rate limits."""
    ss = SpreadsheetService(
        credentials_filepath=GOOGLE_CREDENTIALS_FILEPATH,
        document_id=GOOGLE_SHEETS_TEST_DOCUMENT_ID
    )
    assert ss.document_id == GOOGLE_SHEETS_TEST_DOCUMENT_ID

    yield ss

    print("SLEEPING...")
    sleep(TEST_SLEEP)


@pytest.fixture()
def model_context(service):
    """Use this fixture and subsequent model calls will be made against the test database."""
    BaseModel.service = service
    assert BaseModel.service.document_id == GOOGLE_SHEETS_TEST_DOCUMENT_ID

    yield "Using test document!"

@pytest.fixture()
def test_client(model_context):
    """Test client for the flask web application.
        Uses the model context and therefore runs against the test database.
    """
    app = create_app()
    app.config.update({"TESTING": True})
    return app.test_client()
