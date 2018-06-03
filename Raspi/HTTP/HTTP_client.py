import requests

def Send(MyData):
    r = requests.post('http://192.168.0.201:5906', data={'data':MyData})

