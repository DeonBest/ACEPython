"""
Abtract class for all readers.
All readers should implement this abstract class forcing
implementation of the functions defined.

Author: Evan Larkin
Date: January 2021
"""
from abc import ABC, abstractmethod

# A custom exception that can be used while reading


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
