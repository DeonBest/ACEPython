"""
    Random Reader
    This reader returns random values from -0.5 to 0.5

    Author: Evan Larkin
    Date: February 2021
"""
import numpy as np
import os
import glob
from readers.Reader import Reader
import random


class RandomReader(Reader):
    """
        Initialize the reader
        Args:
            framesize: Number of data points returned per read
                Default => 100
            channels: Number of channels returned during read
                Default => 8
    """

    def __init__(self, framesize=100, channels=8):
        file = os.path.realpath(__file__)+'/../data/emg1KT60.csv'
        file = file.split('backend')[0]
        data = np.genfromtxt(file+'backend/data/emg1KT60.csv',
                             delimiter=",", names=["x"])

        self.currentIndex = 0
        self.channels = 8
        self.framesize = framesize
        self.data = data['x']

    """
        Start the reader
    """

    def start(self):
        # No start setup required
        return True

    """
        Stop the reader
    """

    def stop(self):
        # No Stop setup required
        return True

    """
        Create random data and return it
    """

    def read(self):
        result = []
        for j in range(0, int(self.channels)):
            result.insert(j, [])
            for i in range(0, self.framesize):
                result[j].append(random.uniform(-0.5, 0.5))
        return result
