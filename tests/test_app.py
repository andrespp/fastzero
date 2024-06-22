from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert


def test_create_user(client):

    response = client.post(
        '/create_user/',
        json={
            'username': 'user',
            'email': 'test_user@example.com',
            'password': 'password',
        },
    )  # Act

    assert response.status_code == HTTPStatus.CREATED  # Assert
    assert response.json() == {
            'id': 1,
            'username': 'user',
            'email': 'test_user@example.com',
        }
