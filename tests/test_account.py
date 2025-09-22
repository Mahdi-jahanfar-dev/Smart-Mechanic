from conftest import client_instance
from datetime import datetime


# test for user registration route
def test_register(client_instance):

    response = client_instance.post(
        "/account/register",
        json={
            "username": "test_user",
            "first_name": "mahdi",
            "last_name": "jahanfar",
            "password": "123456",
            "is_mechanic": False,
        },
    )

    assert response.status_code == 201


# test for registred user login route
def test_user_registred_login(client_instance):

    response = client_instance.post(
        "/account/login", json={"username": "test_user", "password": "123456"}
    )

    assert response.status_code == 200


# test for not registred user login route
def test_user_not_registred_login(client_instance):

    response = client_instance.post(
        "/account/login", json={"username": "test_user", "password": "12345566"}
    )

    assert response.status_code == 401
