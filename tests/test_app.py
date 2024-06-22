from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert


def test_create_user_deve_retornar_created_e_usuario_criado():
    client = TestClient(app)  # Arrange

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
            'username': 'user',
            'email': 'test_user@example.com',
        }
