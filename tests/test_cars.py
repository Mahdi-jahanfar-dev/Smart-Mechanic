import pytest


def get_authenticated_user(client):

    response = client.post(
        "/account/login",
        json={
            "username": "fixture_test_user",
            "password": "123456",
        },
    )

    data = response.json()
    return data["access_token"]


def get_mechanic_authenticated_user(client):

    response = client.post(
        "/account/login",
        json={
            "username": "fixture_test_user_mechanic",
            "password": "123456",
        },
    )

    data = response.json()
    return data["access_token"]


@pytest.fixture(scope="module", autouse=True)
def create_users(client_instance):
    response = client_instance.post(
        "/account/register",
        json={
            "username": "fixture_test_user",
            "first_name": "mahdi",
            "last_name": "jahanfar",
            "password": "123456",
            "is_mechanic": False,
        },
    )

    response_2 = client_instance.post(
        "/account/register",
        json={
            "username": "fixture_test_user_mechanic",
            "first_name": "tester",
            "last_name": "jahanfar",
            "password": "123456",
            "is_mechanic": True,
        },
    )


@pytest.fixture(scope="module")
def get_auth_token(client_instance):
    return get_authenticated_user(client_instance)


@pytest.fixture(scope="module")
def get_auth_mechanic_token(client_instance):
    return get_mechanic_authenticated_user(client_instance)


def test_car_register_route(client_instance, get_auth_token):

    response = client_instance.post(
        "/cars/register",
        json={"brand": "mercedes benz", "model": "cls 2012"},
        headers={"Authorization": f"Bearer {get_auth_token}"},
    )

    assert response.status_code == 201


def test_car_register_faild_route(client_instance, get_auth_mechanic_token):

    response = client_instance.post(
        "/cars/register",
        json={"brand": "bmw", "model": "m4"},
        headers={"Authorization": f"Bearer {get_auth_mechanic_token}"},
    )

    assert response.status_code == 403
