import requests
from bs4 import BeautifulSoup as bs
import sys
import glob
import json
import os
#how to get args
#city = sys.argv[1]
#another way to structure
# if __name__ == '__main__':
#print(calc(argv[1]))

def get_data_files():
    my_list=[]
    for file in glob.glob(os.path.dirname(os.path.realpath(__file__))+'/data/*.csv'):
        my_list.append(file)
    return my_list
print(json.dumps(get_data_files()))
sys.stdout.flush()
