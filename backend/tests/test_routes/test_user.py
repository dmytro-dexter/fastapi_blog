def test_create_user(client):
    data = {"email": "ping@fastapi.com", "password": "supersecret"}
    response = client.post("/users/", json=data)
    assert response.status_code == 201
    assert response.json()["email"] == "ping@fastapi.com"


def delete_user(client):
    data = {"id": 100}
    response = client.delete("/users/", json=data)
    assert response.status_code == 400
