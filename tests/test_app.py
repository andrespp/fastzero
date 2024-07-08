from http import HTTPStatus

from fast_zero.schemas import UserPublic


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert


def test_create_user(client):
    response = client.post(
        '/users/',
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


def test_create_existing_user(client, user):
    response = client.post(
        '/users/',
        json={
            'username': user.username,
            'email': user.email,
            'password': 'password',
        },
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_read_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [user_schema]}


def test_get_user(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get(f'/users/{user.id}')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == user_schema

def test_get_unexisting_user(client):
    response = client.get('/users/0')
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_update_user(client, user):
    response = client.put(
        f'/users/{user.id}',
        json={
            'username': 'user_updated',
            'email': 'test_user@example.com',
            'password': 'password',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': user.id,
        'username': 'user_updated',
        'email': 'test_user@example.com',
    }


def test_update_user_invalid_id(client):
    response = client.put(
        '/users/20',
        json={
            'username': 'user_updated',
            'email': 'test_user@example.com',
            'password': 'password',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client, user):
    response = client.delete(f'/users/{user.id}')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_invalid_id(client):
    response = client.delete('users/0')
    assert response.status_code == HTTPStatus.NOT_FOUND
