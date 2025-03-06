from app import app

def test_home_route():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Flask GitHub Actions Demo!" in response.data

    #adding new comment for practice