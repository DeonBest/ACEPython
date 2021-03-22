from readers.Reader import Reader
import numpy as np
from readers.MicRecorder import MicrophoneRecorder


class MicReader(Reader):
    def __init__(self, framesize, channels=8):
        mic = MicrophoneRecorder(framesize=framesize)

        # keeps reference to mic
        self.mic = mic
        self.channels = channels
        self.time_vect = np.arange(
            mic.chunksize, dtype=np.float32) / mic.rate * 1000

    def setInput(self, input):
        print('set input daq' + input)

    def start(self):
        # No start setup required
        try:
            self.mic.start()
            return True
        except Exception as e:
            return False

    def stop(self):
        # No Stop setup required
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
