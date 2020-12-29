from main import app


client = app.test_client()


def test_first():
    url = "/"
    response = client.get(url)
    assert response.json == {"Key": "Value"}


def test_second():
    url = "/hello"
    response = client.get(url)
    assert response.status_code == 201
