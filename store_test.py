from base_request import BaseRequest
import pprint
import json
import requests
import pytest

order_data = [
    {
        "id": 1,
        "petId": 1,
        "quantity": 6,
        "shipDate": "2023-05-13T23:54:30.827Z",
        "status": "placed",
        "complete": True
    },
    {
        "id": 2,
        "petId": 2,
        "quantity": 4,
        "shipDate": "2023-07-26T16:27:43.827Z",
        "status": "placed",
        "complete": True
    },
    {
        "id": 3,
        "petId": 3,
        "quantity": 8,
        "shipDate": "2023-11-20T19:45:15.827Z",
        "status": "placed",
        "complete": False
    },
    {
        "id": 8,
        "petId": 29,
        "quantity": 1,
        "shipDate": "2023-09-16T13:28:36.827Z",
        "status": "cancelled",
        "complete": False
    }
]

BASE_URL_PETSTORE = 'https://petstore.swagger.io/v2'
base_request = BaseRequest(BASE_URL_PETSTORE)


@pytest.mark.parametrize('item', order_data)
def test_api(item):
    data = json.dumps(item)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(BASE_URL_PETSTORE + '/store/order', data=data, headers=headers)
    pprint.pprint(response.text)
    get_order = base_request.get('store/order', str(item['id']))
    assert item['id'] == get_order['id']
    assert item['petId'] == get_order['petId']
    assert item['quantity'] == get_order['quantity']
    assert item['shipDate'] == get_order['shipDate']
    assert item['status'] == get_order['status']
    assert item['complete'] == get_order['complete']
