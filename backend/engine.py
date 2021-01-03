import sys
from flask import Flask
import json
import glob
import json
import os
app = Flask(__name__)

@app.route("/")
def hello():
    return json.dumps("Hello World from Flask!")
    
@app.route("/datafiles")
def datafiles():
    my_list=[]
    for file in glob.glob(os.path.dirname(os.path.realpath(__file__))+'/data/*.csv'):
        my_list.append(file)
    return json.dumps(my_list)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)

    