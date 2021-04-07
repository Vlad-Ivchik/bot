import os
import pytest
from dotenv import load_dotenv, find_dotenv
from starlette import status
from starlette.testclient import TestClient
from asgi import app

client = TestClient(app)

load_dotenv()

bot_token = os.getenv("BOT_TOKEN")
pythonpath = os.getenv("PYTHONPATH")


@pytest.mark.functional
def test_bot():
    response = client.get("/config")
    assert response.status_code == status.HTTP_200_OK
    payload = response.json()
    data = {"bot_token": bot_token, "pythonpath": pythonpath}
    assert payload == data


@pytest.mark.functional
def test_bot_heroku():
    response = client.get("https://bot-vlad-z43.herokuapp.com/config/")
    assert response.status_code == status.HTTP_200_OK
    payload = response.json()
    data = {"bot_token": bot_token, "pythonpath": pythonpath}
    assert payload == data
