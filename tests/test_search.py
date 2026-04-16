def test_search(client):
    client.post('/register', json={
        "username": "Aparna",
        "email": "aparna@gmail.com",
        "password": "Aparna123"
    })

    res = client.get('/search?q=Aparna')
    assert "Aparna" in res.get_data(as_text=True)