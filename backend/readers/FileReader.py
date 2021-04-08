"""
    File Reader
    This reads data from a file found in ../data/.
    The data file must be set with setInput().

    Author: Evan Larkin
    Date: February 2021
"""
import numpy as np
import os
import glob
from readers.Reader import Reader


class FileReader(Reader):
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
        self.channels = channels
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
        Read from the selected file
    """

    def read(self):
        result = []
        print(self.data[self.currentIndex:self.currentIndex + self.framesize])
        next = self.data[self.currentIndex:self.currentIndex +
                         self.framesize].tolist()
        self.currentIndex = self.currentIndex + self.framesize
        for j in range(0, int(self.channels)):
            result.insert(j, next)
        return result

    """
        Set the input file
        Args: 
            inputFile: File found in ../data
    """

    def setInput(self, inputFile):
        file = os.path.realpath(__file__)
        file = file.split('backend')[0]
        print(inputFile)
        filepath = 'backend/data/'+inputFile+".csv"
        data = np.genfromtxt(file+filepath,
                             delimiter=",", names=["x"])
        print(file+filepath)
        self.currentIndex = 0
        self.data = data['x']
