'''
This File is not currently being used but can graph csv data using pyqtgraph
'''

from PyQt5 import QtGui, QtWidgets
import pyqtgraph as pg
from PlotWidget.ReaderPlotWidget import ReaderPlotWidget
from Reader.FileReader import FileReader

class CSVGraphWidget(QtWidgets.QWidget, ReaderPlotWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)

        # customize the UI
        self.initUI()

    def initUI(self):
        container = QtGui.QVBoxLayout()

        self.graphicsView = pg.PlotWidget()
        self.graphicsView.setYRange(-0.1, 0.1, padding=0)
        ax = self.graphicsView.getAxis('bottom')  # This is the trick
        ax.setTickSpacing(1000, 500)
        self.reader = FileReader('Data/emg1KT60.csv')
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line = self.graphicsView.plot(self.reader.x, self.reader.y, pen=pen)

        container.addWidget(self.graphicsView)
        self.setLayout(container)
        self.show()





    def handleStart(self):
        self.reader.handleStart()

    def handleStop(self):
        self.reader.handleStop()

    def setInput(self, file):
        self.reader.setInput(file)

