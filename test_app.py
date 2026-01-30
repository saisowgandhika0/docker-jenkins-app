from app import app

def test_home_route():
    # Flask provides a test client
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello from Flask inside Docker!" in response.data

