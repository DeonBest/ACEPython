"""
The main API Class

Contains the endpoints accessible from localhost:5000
Author: Evan Larkin 
Date: Jan 2021
"""
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
    DAQreader['micreader'] = {'reader': MicReader(), 'name': "Mic"}
    DAQreader['randomreader'] = {'reader': RandomReader(), 'name': 'Random'}
    DAQreader['delsysreader'] = {'reader': DelsysReader(), 'name': 'Delsys'}
    # Setup File Reader
    filereader['reader'] = FileReader()

    return jsonify(1)


"""
/getreaders

This retrieves the list of readers available and instantiated.

"""


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
        for file in glob.glob(os.path.dirname(os.path.realpath(__file__))+'\data\*.csv'):
            print(file)
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


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
