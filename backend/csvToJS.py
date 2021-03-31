import csv
import os
import json
from pathlib import Path
from flask import Flask, render_template

path = 'data\emg1KT60.csv'
pathjs = 'frontend\javascript\csvToArray.js'

p = Path(__file__).parents[0]
p2 = Path(__file__).parents[1]
p2path= os.path.join(p2, pathjs)
data =[]
#print("path is ",os.path.join(p, path))


# with open(os.path.join(p, path), newline='') as f:
#     reader = csv.reader(f)
#     data = list(reader)
# print(data)

def CSVToList():
    with open(os.path.join(p, path)) as f:
        reader = csv.reader(f)
        for row in reader:
            x = float(row[0])
            data.append(x)
    return data
# CSVToList()
#
# print(data)

# js = open(p2path)
#
# javascript_out = "var jsData = JSON.parse('{}');".format(json.dumps(data))
# javascript_out += js.read()
