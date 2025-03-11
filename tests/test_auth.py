def test_register(client):
    response = client.post('/api/register', json={
        'username': 'testuser',
        'password': 'testpassword'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert 'access_token' in data

def test_login(client):
    response = client.post('/api/login', json={
        'username': 'testuser',
        'password': 'testpassword'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert 'access_token' in data
