import uuid

def test_register(client):
    unique_id = str(uuid.uuid4())[:8]

    res = client.post('/register', json={
        "username": f"user_{unique_id}",
        "email": f"{unique_id}@mail.com",
        "password": "123"
    })

    assert res.status_code == 201


def test_login(client):
    unique_id = str(uuid.uuid4())[:8]

    username = f"user_{unique_id}"

    client.post('/register', json={
        "username": username,
        "email": f"{unique_id}@mail.com",
        "password": "123"
    })

    res = client.post('/login', json={
        "username": username,
        "password": "123"
    })

    assert res.status_code == 200