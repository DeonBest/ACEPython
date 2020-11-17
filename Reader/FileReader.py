# class taken from the SciPy 2015 Vispy talk opening example 
# see https://github.com/vispy/vispy/pull/928
import pyaudio
from Reader.Reader import Reader
import numpy as np
from PyQt5 import QtCore


class FileReader(Reader):
    def __init__(self, file, canvas=None):
        data = np.genfromtxt(file, delimiter=",", names=["x"])
        self.data = data['x']
        self.currentIndex = 1000
        self.x = list(range(1000))  # 100 time points
        self.y = self.data[0:1000]  # 100 data points
        self.canvas=canvas
        if(self.canvas is not None):
            # Initial Values for plot
            plot_refs = self.canvas.axes.plot(self.x, self.y, 'r')
            self.plot_ref = plot_refs[0]



    def handleStart(self):
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def handleStop(self):
        self.timer.stop()

    def update_plot_data(self):
        self.x = self.x[100:]  # Remove the first 100 elements.
        nextx = list(range(self.currentIndex, self.currentIndex+100))
        self.x = np.append(self.x,nextx) # Add a new values.

        self.y = self.y[100:]  # Remove the 100 first
        newArr = np.append(self.y, self.data[self.currentIndex:self.currentIndex + 100])
        self.y = newArr
        self.currentIndex = self.currentIndex + 100
        # If given plot, update its data.
        if self.canvas is not None:
            # We have a reference, we can use it to update the data for that line.
            self.plot_ref.set_ydata(self.y)
            # Trigger the canvas to update and redraw.
            self.canvas.draw()


    def setInput(self, input):
        print(input)
        data = np.genfromtxt(input, delimiter=",", names=["x"])
        self.data = data['x']

    def getX(self):
        return self.x

    def getY(self):
        return self.y
