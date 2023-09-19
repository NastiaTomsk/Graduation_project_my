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