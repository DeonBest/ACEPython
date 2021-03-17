import numpy as np
import os
import glob
from readers.Reader import Reader
import socket
import sys
import time
import numpy as np
from ast import literal_eval

class DelsysReader(Reader):
    def __init__(self, framesize=100, hostip="localhost", commandport=50048, emgport=50041, imuport=50042):
        self.framesize = framesize
        self.hostip = hostip
        self.commandport = commandport
        self.emgport = emgport
        self.imuport = imuport
        self.maxSensors = 16
        self.EMGSignal = []
        self.IMUSignal = []
        self.pairedSensors = 0
        self.activeSensors = 0
        # EMG parameters.
        self.EMGMaxSamplesPerFrame = 26
        self.EMGNativeSamplesPerFrame = 26
        self.EMGSampleRate = 1925.925
        self.EMGChannelNumber = 16
        self.EMGChannelCount = 1
        self.EMGUnits = "V"
        self.EMGSensorSpecificNativeSampleRate = 1925.925
        self.EMGSensorSpecificNativeSamplesPerFrame = 26
        self.EMGSensorSpecificChannelCount = 1
        self.EMGSensorSpecificGain = 1
        self.EMGSensorSpecificUnits = "V"
        # IMU (a.k.a. AUX) parameters.
        self.IMUMaxSamplesPerFrame = 2
        self.IMUNativeSamplesPerFrame = 2
        self.IMUSampleRate = 148.148
        self.IMUChannelNumber = [2, 3, 4]
        self.IMUChannelCount = 3
        self.IMUUnits = "g"
        self.IMUSensorSpecificNativeSampleRate = 148.148
        self.IMUSensorSpecificNativeSamplesPerFrame = 2
        self.IMUSensorSpecificChannelCount = 3
        self.IMUSensorSpecificGain = 1
        self.IMUSensorSpecificUnits = "g"
        # Properties
        self.BufferSize = 6400
        self.baseStationDelay = 0.1
        self.sensorDelay = 0.1
        self.sensorMaxRetries = 100
        self.recordingEnabled = True

        self.EMGSignalBuffer = []
        self.IMUSignalBuffer = []

        self.bytesToReadEMG = self.EMGNativeSamplesPerFrame * \
            self.maxSensors * self.EMGChannelCount * 4
        self.bytesToReadIMU = self.IMUNativeSamplesPerFrame * \
            self.maxSensors * self.IMUChannelCount * 4
        self.result=[]
        self.connect()
        self.start()
        self.readEMG()
        self.stop()
        self.disconnect()

    def updateEMGSignal(self, data):
        print("Update EMG", data)

    def readEMG(self):
        ind = 0
        while ind<3:
            data = self.EMGSocket.recv(self.maxSensors * self.EMGChannelCount * 8)
            arr = np.frombuffer(data, dtype=np.uint8)
            arr2= arr.astype(np.float64)
            datashaped = arr.reshape(self.maxSensors * self.EMGChannelCount, -1)
            print(datashaped)
            if(ind is not 0):
                self.result= np.concatenate((self.result, datashaped.tolist()), axis=1)
            else:
                self.result = datashaped.tolist()
            ind= ind + 1
    def read(self, channels):
        print("RESULT", self.result)
        return self.result.tolist()

    def connect(self):
        try:
            print("Connect")

            self.commandSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.EMGSocket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.IMUSocket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)


            server_address_cmd = (self.hostip, self.commandport)
            self.commandSocket.connect(server_address_cmd)

            time.sleep(self.baseStationDelay)

            # Disregard first message from base station, always Delsys Trigno System Digital Protocol Version x.y.z
            data = self.commandSocket.recv(60)
            print('received "%s"' % data)
            print(len(data))

            server_address_emg = (self.hostip, self.emgport)
            self.EMGSocket.connect(server_address_emg)

            server_address_imu = (self.hostip, self.imuport)
            self.IMUSocket.connect(server_address_imu)

            self.getHardwareInfo()
        except Exception as e:
            print(e)

    def disconnect(self):
        self.commandSocket.close()
        self.commandSocket = None
        self.EMGSocket.close()
        self.EMGSocket = None
        self.IMUSocket.close()
        self.IMUSocket = None
        print("CLOSED")

    # Setting 1 = record on, 0 = record off
    def record(self, setting):
        self.recordingEnabled = setting

    def start(self):
        if(self.commandSocket == None):
            print('No connection be sure to run connect() first')
        start = "START\r\n\r\n"
        self.commandSocket.send(start.encode())
        
        time.sleep(self.sensorDelay)
        try:
            data = self.commandSocket.recv(6).decode('utf-8')
            print('Start data', data)
            if 'OK' not in data:
                print('Unable to stop data collection')
               
        except Exception as e:
            print(e)

    def stop(self):
        if(self.commandSocket == None):
            print('No connection be sure to run connect() first')
        stop = "STOP\r\n\r\n"
        self.commandSocket.send(stop.encode())
        
        time.sleep(self.sensorDelay)
        try:
            data = self.commandSocket.recv(6).decode('utf-8')
            print('Stop data', data)
            if 'OK' not in data:
                print('Unable to stop data collection')
        except Exception as e:
            print(e)

    def getHardwareInfo(self):
        print('test')
        self.pairedSensors = self.getSensorsPaired()
        print(self.pairedSensors)
        self.activeSensors = self.getSensorsActive()
        print(self.activeSensors)

    def getSensorsPaired(self):
        result = []
        for i in range(1, self.maxSensors):
            msg = "SENSOR %s PAIRED?\r\n\r\n" % str(i)
            self.commandSocket.send(msg.encode())
            time.sleep(self.baseStationDelay)
            
            try:
                data = self.commandSocket.recv(7)
                if 'YES' not in data.decode('utf-8'):
                    print(i, 'NOT CONNECTED')
                else: 
                    print(i, "CONNECTED")
                    result.append(i)
                
            except Exception as e:
                print('error')
                print(e)
        if len(result)==0:
            return 0
        else:
            return result

    def getSensorsActive(self):
        result = []
        for i in range(0, len(self.pairedSensors)):
            sensorId = self.pairedSensors[i]
            msg = "SENSOR %d ACTIVE?\r\n\r\n" % sensorId
            self.commandSocket.send(msg.encode())
            time.sleep(self.sensorDelay)
            try:
                data = self.commandSocket.recv(6).decode('utf-8')
                if 'YES' not in data:
                    print(sensorId, 'NOT ACTIVE')
                else: 
                    print(sensorId, "ACTIVE")
                    result.append(sensorId)
                
            except Exception as e:
                print(e)
        if len(result)==0:
            return 0
        else:
            return result