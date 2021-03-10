import numpy as np
import os
import glob
from readers.Reader import Reader
import random


class RandomReader(Reader):
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
        for j in range(0, int(channels)):
            result.insert(j, [])
            for i in range(0, self.framesize):
                result[j].append(random.uniform(-0.5, 0.5))
        return result
