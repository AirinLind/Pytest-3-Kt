from base_request import BaseRequest
import pprint
import json
import requests
import pytest

user_data = [
    {
        "id": 1,
        "username": "john",
        "firstName": "John",
        "lastName": "Doe",
        "email": "john@me.com",
        "password": "john$123",
        "phone": "+900 928 00 13",
        "userStatus": 1
    },
    {
        "id": 2,
        "username": "anna",
        "firstName": "Anna",
        "lastName": "Smith",
        "email": "anna@me.com",
        "password": "anna$123",
        "phone": "+900 928 00 14",
        "userStatus": 1
    },
    {
        "id": 3,
        "username": "michael",
        "firstName": "Michael",
        "lastName": "Johnson",
        "email": "michael@me.com",
        "password": "michael$123",
        "phone": "+900 928 00 15",
        "userStatus": 1
    },
    {
        "id": 4,
        "username": "sarah",
        "firstName": "Sarah",
        "lastName": "Brown",
        "email": "sarah@me.com",
        "password": "sarah$123",
        "phone": "+900 928 00 16",
        "userStatus": 1
    }
]


BASE_URL_PETSTORE = 'https://petstore.swagger.io/v2'
base_request = BaseRequest(BASE_URL_PETSTORE)


@pytest.mark.parametrize('item', user_data)
def test_api(item):
    data = json.dumps(item)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(BASE_URL_PETSTORE + '/user/', data=data, headers=headers)
    pprint.pprint(response.text)
    get_user = base_request.get('user', item['username'])
    assert item['id'] == get_user['id']
    assert item['username'] == get_user['username']
    assert item['firstName'] == get_user['firstName']
    assert item['lastName'] == get_user['lastName']
    assert item['email'] == get_user['email']
    assert item['password'] == get_user['password']
    assert item['phone'] == get_user['phone']
    assert item['userStatus'] == get_user['userStatus']
