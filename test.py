# Адиля Кильметова, 8-я когорта,  Финальный проект. Инженер по тестированию плюс
import data
import sender_stand_request

def test_create_order_and_get_order_by_track():
    order_response = sender_stand_request.post_new_order(data.body)
    assert order_response.status_code == 201
    assert order_response.json()["track"] != ""

    get_order_response = sender_stand_request.get_order_by_track()
    assert get_order_response.status_code == 200







