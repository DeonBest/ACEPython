import sys
from flask import Flask, jsonify, g, session
import json
import glob
import json
import os
import random
import numpy as np
app = Flask(__name__)
@app.route("/")
def hello():
    return json.dumps("Hello World from Flask!")
    
@app.route("/datafiles")
def datafiles():
    try:
        my_list=[]
        for file in glob.glob(os.path.dirname(os.path.realpath(__file__))+'/data/*.csv'):
            my_list.append(file)
        return json.dumps(my_list)
    except Exception as e:
        return json.dumps(str(e))

@app.route("/actions")
def actions():
    
        my_list=[]
        for file in glob.glob(os.path.dirname(os.path.realpath(__file__))+'/../frontend/images/actions/*.jpg'):
            actionname = os.path.basename(file).replace("_", " ").replace(".jpg","").capitalize()
            actionkey=os.path.basename(file)
            action = {
                'file_location': file,
                'action_name': actionname,
                'action_key': actionkey
            }
            my_list.append(action)
        return json.dumps(my_list)


@app.route("/readarr")
def readarr():
    return jsonify(random.randint(0,100))

@app.route("/readarr2")
def readarr2():
    return jsonify(random.randint(0,10))

@app.route('/readcsv/<filename>')
def readcsv(filename, frame=0):
    file = glob.glob(os.path.dirname(os.path.realpath(__file__))+'/data/'+filename)
    data = np.genfromtxt(str(file[0]), delimiter=",", names=["x"])
    datax = data['x']
    def getData():
        try:
            return json.dumps(datax.tolist())
        except Exception as e:
            return json.dumps(str(e))
    return getData()



if __name__ == "__main__":
    print(actions())
    app.run(host='127.0.0.1', port=5000)
    

    