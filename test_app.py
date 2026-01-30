from app import app

def test_home_route():
    # Flask provides a test client
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to Jenkins" in response.data 
    assert b"CI/CD pipeline is running successfully" in response.data

