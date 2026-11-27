from fastapi.testclient import TestClient

def test_register(client: TestClient):

    response = client.post(
        "/InvestAI/register",
        json = {
            "username":"test_user",
            "email": "test_user@email.com",
            "password": "password123"
        },
    )

    assert response.status_code == 200

    assert response.json() == {
        "message": "User created successfully"
    }