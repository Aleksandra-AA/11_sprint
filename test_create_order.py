import data as data
from requests import post, put, get
import configuration
import data
import json

def test_order_create_and_get():
    response_context = post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=data.body_order_create)
    assert  response_context.status_code == 201
    track_id = json.loads(response_context.content.decode('utf-8'))['track']
    response_conent = get(configuration.URL_SERVICE + f"/api/v1/orders/track?t={track_id}")
    assert response_conent.status_code == 200