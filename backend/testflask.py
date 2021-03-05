import requests
import time

print(requests.get('http://127.0.0.1:5000/getreaders').json())
val = requests.get('http://127.0.0.1:5000/read/micreader').json()
print(len(val))
time.sleep(0.1)
