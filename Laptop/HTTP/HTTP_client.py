import requests

def Send(MyData):
    r = requests.post('http://192.168.0.200:5906', data={'data':MyData})

