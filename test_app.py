from app import app
def test_hello_route():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert response.data.decode('utf-8') == 'Hello World'
