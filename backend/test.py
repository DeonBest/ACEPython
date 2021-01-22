import sys
from flask import Flask, jsonify
import json
import glob
import json
import os
import random
import numpy as np
import usb.core
import struct
from serial.tools import list_ports
import serial

for com in list_ports.comports():
    print(com)
#Serial(port=None, baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=None, xonxoff=False, rtscts=False, write_timeout=None, dsrdtr=False, inter_byte_timeout=None)
ser = serial.Serial('/dev/tty.usbserial-14200', 125000, 8, serial.PARITY_NONE, serial.STOPBITS_ONE,0.1)


try:
    ser.isOpen()
    print('Port open')
except:
    print('Error')
    exit()

if ser.isOpen():
    print(ser)
    try:
        while True:
            print('read')
            #value = ser.readline()
            #print(struct.unpack('f', value))
            print(ser.read())
    except Exception as e:
        print('Error', e)
        exit()
else:
    print('cannot open serial port')

""" #list of devices
dev=usb.core.find(idVendor=0x0403,idProduct=0x6010)
#buffer
ep=dev[0].interfaces()[0].endpoints()[0]
i=dev[0].interfaces()[0].bInterfaceNumber

dev.reset()

if dev.is_kernel_driver_active(i):
    dev.detach_kernel_driver(i)

dev.set_configuration()

eaddr=ep.bEndpointAddress
r=dev.read(eaddr, 1024)
val = struct.unpack('f', r)
print(len(r))
print(r) """



    