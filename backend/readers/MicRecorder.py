"""
    Mic Recorder
    This is a helper class for the Mic Reader.
    It records microphone data and stores it in frames.

    Author: Evan Larkin
    Date: February 2021
"""
# class taken from the SciPy 2015 Vispy talk opening example
# see https://github.com/vispy/vispy/pull/928
import pyaudio
import threading
import atexit
import numpy as np


class MicrophoneRecorder(object):
    """
        Initialize the recorder
        Args:
            framesize: Chunksize - Number of frames in the buffer
                Default => 100
            rate: sampling rate (/sec)
                Default => 4000
    """

    def __init__(self, rate=4000, framesize=100):
        self.rate = rate
        self.chunksize = framesize
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16,
                                  channels=1,
                                  rate=self.rate,
                                  input=True,
                                  frames_per_buffer=self.chunksize,
                                  stream_callback=self.new_frame)
        self.lock = threading.Lock()
        self.stop = False
        self.frames = []
        self.start()
        atexit.register(self.close)

    """
        A new frame is available from the stream, append it to the data collection
    """

    def new_frame(self, data, frame_count, time_info, status):
        data = np.fromstring(data, dtype=np.int16)
        # make output -1 to 1 from -32767 to 32767
        dataConverted = np.array([x / 32767 for x in data])
        print()
        with self.lock:
            self.frames.append(dataConverted)
            if self.stop:
                return None, pyaudio.paComplete
        return None, pyaudio.paContinue

    """
        Get the frames that have been collected
    """

    def get_frames(self):
        with self.lock:
            frames = self.frames
            self.frames = []
            return frames

    """
        Start streaming from microphone
    """

    def start(self):
        self.stream.start_stream()

    """
        Close mic stream
    """

    def close(self):
        with self.lock:
            self.stop = True
        self.stream.close()
        self.p.terminate()
