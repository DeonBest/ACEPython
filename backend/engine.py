"""
The main API Class

Contains the endpoints accessible from localhost:5000
Author: Evan Larkin
Date: Jan 2021
"""
import sys
import csv
from flask import Flask, jsonify, g, session
import json
import glob
import json
import os
import random
import numpy as np
from readers import FileReader
from readers import MicReader
from readers import RandomReader
from readers import DelsysReader
import platform
app = Flask(__name__)

# These global variables hold instances of the readers
# Accessible from all endpoints
DAQreader = {}
filereader = {}

"""
This is called once before any other request is sent. It initializes the
readers in the global variable at their respective key.

DAQReader:{
    <readername>:{
        reader: the reader instatiation
        name: Name of the reader that will be used for selection in frontend
    }
}
FileReader:{
    reader: the reader instatiation
}
"""


@app.before_first_request
def init():
    # Setup DAQ Readers
    DAQreader['micreader'] = {'reader': MicReader.MicReader(), 'name': "Mic"}
    DAQreader['randomreader'] = {
        'reader': RandomReader.RandomReader(), 'name': 'Random'}
    try:
        DAQreader['delsysreader'] = {
            'reader': DelsysReader.DelsysReader(), 'name': 'Delsys'}
    except Exception as e:
        print("ERROR With Delsys")

    # Setup File Reader
    filereader['reader'] = FileReader.FileReader()

    return jsonify(1)


"""
This retrieves the path for the data files. When the application is built they are stored in temp
folder at path stored in env variable _MEIPASS. Otherwise they are found in /data/*
"""


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # If in development, return the real path
        base_path = os.path.abspath(".")
        # If engine.py is run before launching the app, base_path resolves to root (Debugging purposes)
        # If engine.py is launched by the application, it resolves to backend (npm start)
        if 'backend' not in base_path:
            base_path = base_path + '/backend'
    return os.path.join(base_path, relative_path)


"""
/getreaders

This retrieves the list of readers available and instantiated.

"""


@ app.route("/test")
def test():
    path1 = resource_path('data/*.csv')
    path2 = os.path.dirname(os.path.realpath(__file__))
    path3 = os.path.abspath(".")
    return jsonify([path1, path2, path3])


@ app.route("/getreaders")
def getReaders():
    readerList = []
    for key in DAQreader.keys():
        readerList.append({'key': key, 'name': DAQreader[key]['name']})
        print(key)
    return jsonify(list(readerList))


"""
/read/file

This retrieves the next set of data from the file being read.

"""


@ app.route("/read/file")
def readFile():
    result = filereader['reader'].read()
    return jsonify(result)


"""
/start/file

This completes any setup required before reading can occur.

"""


@ app.route("/start/file")
def startFile():
    result = filereader['reader'].start()
    print('THE RESULT', result)
    return jsonify(result)


"""
/stop/file

This stops any processes required once reading has completed.

"""


@ app.route("/stop/file")
def stopFile():
    result = filereader['reader'].stop()
    print('THE RESULT')
    return jsonify(result)


"""
/read/<daq>

This retrieves the next set of data from the selected reader.
Params: daq - the key to the selected reader
"""


@ app.route("/read/<daq>")
def readDAQ(daq):
    print(daq)
    result = DAQreader[daq]['reader'].read()
    print('THE RESULT')
    return jsonify(result)


"""
/start/<daq>

This completes any setup required before reading can occur.
Params: daq - the key to the selected reader
"""


@ app.route("/start/<daq>")
def startDAQ(daq):
    print("START DAQ")

    result = DAQreader[daq]['reader'].start()
    print('THE RESULT DAQ', result)
    return jsonify(result)


"""
/stop/<daq>

This stops any processes required once reading has completed.
Params: daq - the key to the selected reader
"""


@ app.route("/stop/<daq>")
def stopDAQ(daq):
    print("STOP DAQ")
    result = DAQreader[daq]['reader'].stop()
    print('THE RESULT')
    return jsonify(result)


"""
/setfileinput/<file>

This sets the file that will be read from the filereader.
Params: file - the name of the file selected
"""


@ app.route("/setfileinput/<file>")
def setFileInput(file):
    result = filereader['reader'].setInput(file)
    return jsonify(result)


"""
/datafiles

This retrieves the data files that can be read. Files are in /data/.
"""


@ app.route("/datafiles")
def datafiles():
    try:
        my_list = []
        # Mac or Linux
        path = resource_path('data/*.csv')
        if(platform.system() == 'Windows'):
            path = resource_path('data\*.csv')

        for file in glob.glob(path):
            my_list.append(str(file))
        return json.dumps(my_list)
    except Exception as e:
        return json.dumps(str(e))


"""
/actions

This retrieves the actions files that can be completed for data collection.
Actions are in ../frontend/images/actions/
"""


@ app.route("/actions")
def actions():

    actionlist = []
    actionsFormatted = []
    path = resource_path('actions/actions.csv')
    if(platform.system() == 'Windows'):
        path = resource_path('actions\\actions.csv')

    with open(path, newline='') as f:
        reader = csv.reader(f)
        for file in reader:

            actionlist.append(file[0])

    for file in actionlist:

        actionname = file.replace(
            "_", " ").replace(".jpg", "").capitalize()
        action = {
            'action_name': actionname,
            'action_key': file
        }
        actionsFormatted.append(action)
    return json.dumps(actionsFormatted)


def main():
    app.run(host='127.0.0.1', port=5000)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
