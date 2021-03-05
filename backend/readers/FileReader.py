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

    def read(self):
        print(self.currentIndex)
        print(self.data[self.currentIndex:self.currentIndex + self.framesize])
        next = self.data[self.currentIndex:self.currentIndex +
                         self.framesize].tolist()
        self.currentIndex = self.currentIndex + self.framesize
        return next
