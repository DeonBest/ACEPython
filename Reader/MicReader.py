from Reader.Reader import Reader
import numpy as np
from PyQt5 import QtCore
from Reader.MicRecorder import MicrophoneRecorder

class MicReader(Reader):
    def __init__(self, canvas=None):
        self.canvas= canvas

        mic = MicrophoneRecorder()
        mic.start()

        # keeps reference to mic
        self.mic = mic

        self.time_vect = np.arange(mic.chunksize, dtype=np.float32) / mic.rate * 1000
        if(self.canvas is not None):
            # Initial Values for plot
            y_vec = np.zeros(mic.chunksize)
            plot_refs = self.canvas.axes.plot(self.time_vect, y_vec, 'r')
            self.plot_ref = plot_refs[0]

    def handleStart(self):
        timer = QtCore.QTimer()
        timer.timeout.connect(self.update_plot_data)
        timer.start(100)

        self.timer = timer

    def handleStop(self):
        self.timer.stop()

    def setInput(self, input):
        print('set input daq' + input)

    def update_plot_data(self):
        """ handles the asynchroneously collected sound chunks """
        # gets the latest frames
        frames = self.mic.get_frames()

        if len(frames) > 0:
            # keeps only the last frame
            current_frame = frames[-1]
            # If given plot, update its data.
            if (self.canvas is not None):
                # plots the signal
                self.plot_ref.set_data(self.time_vect, current_frame)
                # refreshes the plots
                self.canvas.draw()

    def getX(self):
        return self.x

    def getY(self):
        return self.y
