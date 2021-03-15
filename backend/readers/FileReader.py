import numpy as np
import os
import glob
from readers.Reader import Reader


class FileReader(Reader):
    def __init__(self, framesize):
        file = os.path.realpath(__file__)+'/../data/emg1KT60.csv'
        file = file.split('backend')[0]
        data = np.genfromtxt(file+'backend/data/emg1KT60.csv',
                             delimiter=",", names=["x"])

        self.currentIndex = 0
        self.framesize = framesize
        self.data = data['x']

    def read(self, channels):
        result = []
        print(self.data[self.currentIndex:self.currentIndex + self.framesize])
        next = self.data[self.currentIndex:self.currentIndex +
                         self.framesize].tolist()
        self.currentIndex = self.currentIndex + self.framesize
        for j in range(0, int(channels)):
            result.insert(j, next)
        return result

    def setInput(self, inputFile):
        file = os.path.realpath(__file__)
        file = file.split('backend')[0]
        filepath = 'backend/data/'+inputFile+".csv"
        data = np.genfromtxt(file+filepath,
                             delimiter=",", names=["x"])
        print(file+filepath)
        self.currentIndex = 0
        self.data = data['x']
