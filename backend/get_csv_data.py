import requests
from bs4 import BeautifulSoup as bs
import sys
import glob
import json
import os
import numpy as np
#how to get args
#city = sys.argv[1]
#another way to structure
# if __name__ == '__main__':
#print(calc(argv[1]))

file = sys.argv[1]
def get_csv_data():
    print(file)
    data = np.genfromtxt(file, delimiter=",", names=["x"])
    datavalues = data['x']
    print(json.dumps(datavalues.tolist()))
    return datavalues
get_csv_data()
sys.stdout.flush()
