from http import HTTPStatus

from fastapi.testclient import TestClient

from app.app import app


def test_root_must_return_hello_world():
    client = TestClient(app)

    response = client.get("/")

    assert response.json() == {"message": "Olá mundo!"}
    assert response.status_code == HTTPStatus.OK
