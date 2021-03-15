import numpy as np
import os
import glob
from readers.Reader import Reader
import socket
import sys
import time


class DelsysReader(Reader):
    def __init__(self, framesize=100, hostip="localhost", commandport=50040, emgport=50041, imuport=50042):
        self.hostip = hostip
        self.commandport = commandport
        self.emgport = emgport
        self.imuport = imuport
        self.maxSensors = 16
        self.EMGSignal = []
        self.IMUSignal = []
        self.sensorsPaired = 0
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

        self.connect()

    def updateEMGSignal(self, data):
        print("Update EMG", data)

    def read(self, channels):
        result = []
        return result

    def connect(self):
        try:
            print("Connect")
            test_addr = ('localhost', 80)
            self.commandSocket = socket.socket()

            server_address_cmd = (self.hostip, self.commandport)
            self.commandSocket.connect(server_address_cmd)

            time.sleep(self.baseStationDelay)
            # Disregard first message from base station, always Delsys Trigno System Digital Protocol Version x.y.z
            amount_received = 0
            while amount_received < 1000:
                data = commandSocket.recv(16)
                amount_received += len(data)
                print('received "%s"' % data)

            server_address_emg = (self.hostip, self.emgport)
            self.EMGSocket.connect(server_address_emg)

            server_address_imu = (self.hostip, self.imuport)
            self.IMUSocket.connect(server_address_imu)
        except Exception as e:
            print(e)

    def disconnect(self):
        self.commandSocket.close()
        self.commandSocket = None
        self.EMGSocket.close()
        self.EMGSocket = None
        self.IMUSocket.close()
        self.IMUSocket = None

    # Setting 1 = record on, 0 = record off
    def record(self, setting):
        self.recordingEnabled = setting

    def start(self):
        if(self.commandSocket == None):
            print('No connection be sure to run connect() first')

        for attempt in range(1, self.sensorMaxRetries):
            time.sleep(sensorDelay)
