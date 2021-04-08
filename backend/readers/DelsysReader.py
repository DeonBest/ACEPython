"""
    Delsys Reader
    This reads data from the Delsys Trigno Base System.
    Only works on windows.
    Requires Delsys Trigno SDK.

    Author: Evan Larkin
    Date: March 2021
"""
import numpy as np
import os
import glob
from readers.Reader import Reader
from readers.Reader import ReadError
import socket
import sys
import time
import numpy as np
from ast import literal_eval


class DelsysReader(Reader):
    """
        Initialize the reader
        Args:
            framesize: Number of data points returned per read
                Default => 100
            channels: Number of channels returned during read
                Default => 8
            hostip: the host ip for the delsys base station
                Default => localhost
            commandport: the command port for the delsys base station
                Default => 50048
            emgport: the emg port for the delsys base station
                Default => 50041
            imuport: the emg port for the delsys base station
                Default => 50042
    """

    def __init__(self, framesize=100, channels=8, hostip="localhost", commandport=50048, emgport=50041, imuport=50042):
        self.framesize = framesize
        self.channels = channels
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
        self.result = []
        self.connect()

    """
        Read from the Delsys Buffer
    """

    def read(self):
        result = np.array([])
        ind = 0
        try:
            while(True):
                data = self.EMGSocket.recv(self.BufferSize)
                arr = np.frombuffer(data, dtype=np.float32)
                arr2 = arr
                extra = len(data) % (self.maxSensors * self.EMGChannelCount)
                arr = arr[:len(arr)-extra]
                result = np.append(result, arr)
                ind = ind + 1

        # When no data left on buffer return
        except Exception as e:
            print("Error", e)
            dataLength = int(len(result)/16)
            # 16xDatalength array of zeros
            val = np.zeros((16, dataLength))
            if(dataLength > 0):
                # For each active sensor, get the data in the appropriate shape (every 16th value)
                for i in range(0, len(self.activeSensors)):
                    #limit to first 8 sensors
                    if(self.activeSensors[i] < 8):
                        val[self.activeSensors[i] -
                            1] = result[self.activeSensors[i]-1:len(result):16]
                        # Array indexed from 0, sensor n data = result[n-1]
                        print(result[self.activeSensors[i]-1:len(result):16])
            return val.tolist()

    """
        Connect to the Delsys base station.
    """

    def connect(self):
        try:
            print("Connect")

            self.commandSocket = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
            self.EMGSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.IMUSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            server_address_cmd = (self.hostip, self.commandport)
            self.commandSocket.connect(server_address_cmd)

            time.sleep(self.baseStationDelay)

            # Disregard first message from base station, always 'Delsys Trigno System Digital Protocol Version x.y.z'
            data = self.commandSocket.recv(60)
            print('received "%s"' % data)
            print(len(data))

            server_address_emg = (self.hostip, self.emgport)
            self.EMGSocket.connect(server_address_emg)
            self.EMGSocket.setblocking(False)

            server_address_imu = (self.hostip, self.imuport)
            self.IMUSocket.connect(server_address_imu)
            self.IMUSocket.setblocking(False)

            self.getHardwareInfo()
        except Exception as e:
            print(e)

    """
        Disconnect from the Delsys base station.
    """

    def disconnect(self):
        self.commandSocket.close()
        self.commandSocket = None
        self.EMGSocket.close()
        self.EMGSocket = None
        self.IMUSocket.close()
        self.IMUSocket = None
        print("CLOSED")

    """
        Start the reader
    """

    def start(self):
        if(self.commandSocket == None):
            print('No connection be sure to run connect() first')
            return False
        start = "START\r\n\r\n"
        self.commandSocket.send(start.encode())

        time.sleep(self.baseStationDelay)

        data = self.commandSocket.recv(20)

        if 'OK' not in data.decode('utf-8'):
            return False

        return True

    """
        Stop the reader
    """

    def stop(self):
        if(self.commandSocket == None):
            print('No connection be sure to run connect() first')
            return False

        stop = "STOP\r\n\r\n"
        self.commandSocket.send(stop.encode())

        time.sleep(self.sensorDelay)
        try:
            data = self.commandSocket.recv(40).decode('utf-8')

            if 'OK' not in data:
                print('Unable to stop data collection')
                return False

            return True
        except Exception as e:
            print(e)
            return False

    """
        Get information from Delsys base station.
        Determine number of paired and active sensors.
    """

    def getHardwareInfo(self):
        self.pairedSensors = self.getSensorsPaired()
        self.activeSensors = self.getSensorsActive()


    """
        Determine which sensors are paired
    """

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
                print('error',e)
        if len(result) == 0:
            return 0
        else:
            return result

    """
        Determine which sensors are active
    """

    def getSensorsActive(self):
        result = []
        for i in range(0, len(self.pairedSensors)):
            sensorId = self.pairedSensors[i]
            msg = "SENSOR %d ACTIVE?\r\n\r\n" % sensorId
            self.commandSocket.send(msg.encode())
            time.sleep(self.sensorDelay)
            try:
                data = self.commandSocket.recv(7).decode('utf-8')
                if 'YES' not in data:
                    print(sensorId, 'NOT ACTIVE')
                else:
                    print(sensorId, "ACTIVE")
                    result.append(sensorId)

            except Exception as e:
                print("error", e)
        if len(result) == 0:
            return 0
        else:
            return result
