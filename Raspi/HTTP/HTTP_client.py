import requests

def send(MyData):
    r = requests.post('http://192.168.43.201:5906', data={'data':MyData})

