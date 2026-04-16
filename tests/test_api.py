import uuid

from app.routes import students

def test_crud(client):
    unique_id = str(uuid.uuid4())[:8]

    username = f"api_{unique_id}"
    email = f"{unique_id}@mail.com"

    # POST
    res = client.post('/students', json={
        "username": username,
        "email": email,
        "password": "123"
    })
    assert res.status_code == 201

    # GET
    res = client.get('/students')
    assert res.status_code == 200

    # Get latest user ID dynamically
    response_data = res.get_json()
    students = response_data["data"]
    
    student_id = students[-1]["id"]

    # PUT
    res = client.put(f'/students/{student_id}', json={
        "username": f"updated_{unique_id}"
    })
    assert res.status_code == 200

    # DELETE
    res = client.delete(f'/students/{student_id}')
    assert res.status_code == 200