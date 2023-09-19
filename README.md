# Автор: Анастасия Баженова, 8а кагорта
Стек для выполнения проекта
●	PyCharm
●	GitHub
●	requests
●	pytest

План:
1. Прописать python в консоли 
2. Создать новый проект и принудить туда venv через консоль пайчарма: 
python -m venv venv
pip install pytest
pip install requests

3. Запустить сервер

4. Создать фаил: configuration.py

URL = "Вставить URL"
CREATE_NEW_ORDER = "/api/v1/orders"
ORDER_TRACK_INFO = "/api/v1/orders/track?t="

5. Создать фаил: data.py

order_body = {
    "firstName": "Anastasia",
    "lastName": "Bazhenova",
    "address": "Pushkin 1",
    "metroStation": "Sokol",
    "phone": "+79008001213",
    "rentTime": 1,
    "deliveryDate": "2023-09-25",
    "comment": "Hello world",
    "color": [
             "BLACK"
    ]
}

6. Создать фаил: request_order.py
import configuration
import data
import requests

#Create an order
def ceate_new_order():
    order_track = requests.post(configuration.URL+configuration.CREATE_NEW_ORDER, json=data.order_body)
    return order_track.json()['track']

def order_track_info(order_track):
    order_info = requests.get(configuration.URL+configuration.ORDER_TRACK_INFO+order_track)
    return order_info

7.Создать фаил: order_test.py
import data
import request_order
import pytest

def test_order_info ():
    track = request_order.ceate_new_order()
    requests = request_order.order_track_info(str(track)).status_code
    expect = 200
    assert requests == expect

8. Прогнать тест

9. Добавить .gitignore в папку проекта с файлами

10. Заполнить README.md

11. Закоммитить все это в GitHub






