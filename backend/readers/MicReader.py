"""
    Mic Reader
    This reads data from the Mic Recorder.
    The data returned is adjusted to values between -1 and 1.

    Author: Evan Larkin
    Date: February 2021
"""
from readers.Reader import Reader
import numpy as np
from readers.MicRecorder import MicrophoneRecorder


class MicReader(Reader):
    """
        Initialize the reader
        Args:
            framesize: Number of data points returned per read
                Default => 100
            channels: Number of channels returned during read
                Default => 8
    """

    def __init__(self, framesize=100, channels=8):
        mic = MicrophoneRecorder(framesize=framesize)

        # keeps reference to mic
        self.mic = mic
        self.channels = channels
        self.time_vect = np.arange(
            mic.chunksize, dtype=np.float32) / mic.rate * 1000

    def setInput(self, input):
        print('set input daq' + input)

    """
        Start the reader
    """

    def start(self):
        try:
            self.mic.start()
            return True
        except Exception as e:
            return False

    """
        Stop the reader
    """

    def stop(self):
        return True

    def read(self):
        """ handles the asynchroneously collected sound chunks """
        # gets the latest frames
        frames = self.mic.get_frames()
        result = []
        if len(frames) > 0:
            # keeps only the last frame
            current_frame = frames[-1]
            # If given plot, update its data.
            for j in range(0, int(self.channels)):
                result.insert(j, [])
                result[j] = current_frame.tolist()
            return result

        return []
