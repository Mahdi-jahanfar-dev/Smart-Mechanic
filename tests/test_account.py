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
    
