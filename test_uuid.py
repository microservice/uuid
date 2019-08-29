from http import HTTPStatus

def test_generate_request(client):
    url = "/generate"
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK



