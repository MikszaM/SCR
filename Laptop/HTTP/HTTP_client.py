import requests

r = requests.get('http://192.168.1.200:5906')
print r.text
