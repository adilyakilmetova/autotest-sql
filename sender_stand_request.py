# Адиля Кильметова, 8-я когорта,  Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data

#Функция для Создания заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)
response = post_new_order(data.body)
print(response.text)
print(response.status_code)

#Функция для получения заказа по его номеру
def get_order_by_track():
    response = post_new_order(data.body)
    token = response.json()["track"]
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK,
                        params={"t": token}
                        )
response = get_order_by_track()
print(response.status_code)
print(response.text)