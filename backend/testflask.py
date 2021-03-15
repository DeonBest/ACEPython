import requests
import time

print(requests.get('http://127.0.0.1:5000/getreaders').json())
val = requests.get('http://127.0.0.1:5000/setfileinput/emg1KT60').json()
val = requests.get('http://127.0.0.1:5000/read/micreader/2').json()
print(val)
