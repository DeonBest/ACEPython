import sys
from flask import Flask, jsonify, g, session
import json
import glob
import json
import os
import random
import numpy as np
from readers.FileReader import FileReader
from readers.MicReader import MicReader
from readers.RandomReader import RandomReader

app = Flask(__name__)

reader = {}


@app.before_first_request
def init():
    print("INIT")
    reader['filereader'] = {
        'reader': FileReader(framesize=100), 'name': "File"
    }
    reader['micreader'] = {'reader': MicReader(framesize=100), 'name': "Mic"
                           }
    reader['randomreader'] = {'reader': RandomReader(
        framesize=100), 'name': 'Random'
    }
    return jsonify(1)


@ app.route("/getreaders")
def getReaders():
    readerList = []
    for key in reader.keys():
        readerList.append({'key': key, 'name': reader[key]['name']})
    return jsonify(list(readerList))


@ app.route("/read/<readertype>/<channels>")
def read(readertype, channels):
    print(readertype, channels)
    result = reader[readertype]['reader'].read(channels)
    print('THE RESULT')
    return jsonify(result)


@ app.route("/datafiles")
def datafiles():
    try:
        my_list = []
        for file in glob.glob(os.path.dirname(os.path.realpath(__file__))+'/data/*.csv'):
            my_list.append(file)
        return json.dumps(my_list)
    except Exception as e:
        return json.dumps(str(e))


@ app.route("/actions")
def actions():

    my_list = []
    for file in glob.glob(os.path.dirname(os.path.realpath(__file__))+'/../frontend/images/actions/*.jpg'):
        actionname = os.path.basename(file).replace(
            "_", " ").replace(".jpg", "").capitalize()
        actionkey = os.path.basename(file)
        action = {
            'file_location': file,
            'action_name': actionname,
            'action_key': actionkey
        }
        my_list.append(action)
    return json.dumps(my_list)


@ app.route("/readarr")
def readarr():
    return jsonify(random.uniform(-0.5, 0.5))


@ app.route("/readarr2")
def readarr2():
    return jsonify(random.randint(0, 10))


@ app.route('/readcsv/<filename>')
def readcsv(filename, frame=0):
    file = glob.glob(os.path.dirname(
        os.path.realpath(__file__))+'/data/'+filename)
    data = np.genfromtxt(str(file[0]), delimiter=",", names=["x"])
    datax = data['x']

    def getData():
        try:
            return json.dumps(datax.tolist())
        except Exception as e:
            return json.dumps(str(e))
    return getData()


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
