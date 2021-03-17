import requests
import time
string = 'testing %d val' % 10
import numpy as np

print(requests.get('http://127.0.0.1:5000/getreaders').json())
val = requests.get('http://127.0.0.1:5000/read/delsysreader/2').json()
print(val)
