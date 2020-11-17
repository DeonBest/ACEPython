from abc import ABC, abstractmethod


class Reader(ABC):
    @abstractmethod
    def handleStart(self):
        pass

    @abstractmethod
    def handleStop(self):
        pass
