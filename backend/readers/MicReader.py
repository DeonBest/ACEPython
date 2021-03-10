from readers.Reader import Reader
import numpy as np
from readers.MicRecorder import MicrophoneRecorder


class MicReader(Reader):
    def __init__(self, framesize):
        mic = MicrophoneRecorder(framesize=framesize)
        mic.start()

        # keeps reference to mic
        self.mic = mic

        self.time_vect = np.arange(
            mic.chunksize, dtype=np.float32) / mic.rate * 1000

    def setInput(self, input):
        print('set input daq' + input)

    def read(self, channels):
        """ handles the asynchroneously collected sound chunks """
        # gets the latest frames
        frames = self.mic.get_frames()
        result = []
        if len(frames) > 0:
            # keeps only the last frame
            current_frame = frames[-1]
            # If given plot, update its data.
            for j in range(0, int(channels)):
                result.insert(j, [])
                result[j] = current_frame.tolist()
            return result

        return []
