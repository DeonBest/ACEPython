from abc import ABC, abstractmethod

# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass
class ReadError(Error):
    """Raised when error reading input"""
    pass
class Reader(ABC):
    @abstractmethod
    def read(self, channels):
        pass
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass