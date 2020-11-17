import numpy as np
from PyQt5 import QtGui, QtCore, QtWidgets
import pyqtgraph as pg
from abc import ABC, ABCMeta, abstractmethod

class QABCMeta(ABCMeta, type(QtWidgets.QWidget)):
    """Create a meta class that combines ABC and the Qt meta class"""
    pass

class ReaderPlotWidget(ABC, metaclass=QABCMeta):
    @abstractmethod
    def initUI(self):
        pass

    @abstractmethod
    def handleStart(self):
        pass

    @abstractmethod
    def handleStop(self):
        pass
