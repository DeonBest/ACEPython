#!/usr/bin/env python3

import random



from PyQt5 import QtWidgets, QtGui
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
matplotlib.use('Qt5Agg')
import numpy as np
from Reader.FileReader import FileReader
from PlotWidget.ReaderPlotWidget import ReaderPlotWidget
class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class LiveCSV(QtWidgets.QWidget, ReaderPlotWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)

        # customize the UI
        self.initUI()

    def initUI(self):
        container = QtGui.QVBoxLayout()
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.canvas.axes.set_autoscaley_on(True)

        container.addWidget(self.canvas)
        self.setLayout(container)
        self.show()

        self.reader = FileReader('Data/emg1KT60.csv', self.canvas)

    def handleStart(self):
        self.reader.handleStart()

    def handleStop(self):
        self.reader.handleStop()

    def setInput(self, file):
        self.reader.setInput(file)
