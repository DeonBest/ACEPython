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
from readers.DelsysReader import DelsysReader

app = Flask(__name__)

DAQreader = {}
filereader = {}


@app.before_first_request
def init():
    # Setup DAQ Readers
    DAQreader['micreader'] = {'reader': MicReader(framesize=100), 'name': "Mic"
                              }
    DAQreader['randomreader'] = {'reader': RandomReader(
        framesize=100), 'name': 'Random'
    }
    DAQreader['delsysreader'] = {'reader': DelsysReader(
        framesize=100), 'name': 'Delsys'
    }
    # Setup File Readers
    filereader['reader'] = FileReader(framesize=100)
    print(DAQreader)
    return jsonify(1)


@ app.route("/getreaders")
def getReaders():
    readerList = []
    for key in DAQreader.keys():
        readerList.append({'key': key, 'name': DAQreader[key]['name']})
        print(key)
    return jsonify(list(readerList))


@ app.route("/read/file")
def readFile():
    result = filereader['reader'].read()
    return jsonify(result)

@ app.route("/start/file")
def startFile():
    result = filereader['reader'].start()
    print('THE RESULT', result)
    return jsonify(result)

@ app.route("/stop/file")
def stopFile(daq):
    print(daq)
    result = filereader['reader'].stop()
    print('THE RESULT')
    return jsonify(result)

@ app.route("/read/<daq>")
def readDAQ(daq):
    print(daq)
    result = DAQreader[daq]['reader'].read()
    print('THE RESULT')
    return jsonify(result)

@ app.route("/start/<daq>")
def startDAQ(daq):
    print("START DAQ")

    result = DAQreader[daq]['reader'].start()
    print('THE RESULT DAQ', result)
    return jsonify(result)


@ app.route("/stop/<daq>")
def stopDAQ(daq):
    print("STOP DAQ")
    result = DAQreader[daq]['reader'].stop()
    print('THE RESULT')
    return jsonify(result)


@ app.route("/setfileinput/<file>")
def setFileInput(file):
    result = filereader['reader'].setInput(file)
    return jsonify(result)


@ app.route("/datafiles")
def datafiles():
    try:
        my_list = []
        for file in glob.glob(os.path.dirname(os.path.realpath(__file__))+'\data\*.csv'):
            print(file)
            my_list.append(str(file))
        return json.dumps(my_list)
    except Exception as e:
        print('ERRRO')
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
