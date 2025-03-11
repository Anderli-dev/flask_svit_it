import json
import io

def get_token(client):
    response = client.post('/api/login', json={
        'username': 'testuser',
        'password': 'testpassword'
    })
    assert response.status_code == 200
    return response.get_json()['access_token']

def test_upload_log(client):
    token = get_token(client)
    data = {'file': (io.BytesIO(b"Test log content"), "log.txt")}
    response = client.post('/api/log',
                        headers={'Authorization': f'Bearer {token}'},
                        content_type='multipart/form-data',
                        data=data)
    assert response.status_code == 200
    assert response.get_json()['message'] == 'File uploaded successfully'

def test_get_logs(client):
    token = get_token(client)
    
    client.get('/api/log',
                headers={'Authorization': f'Bearer {token}'},
                content_type='multipart/form-data',
                data={'file': (io.BytesIO(b"Log entry"), "log.txt")})

    response = client.get('/api/log',
                        headers={'Authorization': f'Bearer {token}'})
    
    assert response.status_code == 200
    logs = response.get_json()
    assert isinstance(logs, list)
    assert len(logs) > 0
