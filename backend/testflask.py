from datetime import datetime
import numpy as np
import requests
import time
string = 'testing %d val' % 10
print(requests.get('http://127.0.0.1:5000/actions').json())
# print(requests.get('http://127.0.0.1:5000/datafiles').json())


"""
while(True):
    val = requests.get('http://127.0.0.1:5000/read/delsysreader/2').json()
    if(val is not None and len(val)>0):
        print(len(val))
        print(val[2])
        #print(len(val[0]))
        print(datetime.now())
    time.sleep(0.05)

"""
