from fastapi.testclient import TestClient


def test_login(client: TestClient):

    client.post(
        "/InvestAI/register",
        json={
            "username": "test_user",
            "email": "test_user@email.com",
            "password": "password123"
        },
    )

    response = client.post(
        "/InvestAI/login",
        json={
            "email": "test_user@email.com",
            "password": "password123"
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["token_type"] == "bearer"
    assert data["access_token"]