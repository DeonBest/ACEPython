import numpy as np
from PyQt5 import QtGui, QtCore, QtWidgets
import pyqtgraph as pg


class CSVGraphWidget(QtWidgets.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)

        # customize the UI
        self.initUI()

    def initUI(self):
        container = QtGui.QVBoxLayout()

        self.graphicsView = pg.PlotWidget()
        self.graphicsView.setYRange(-0.1, 0.1, padding=0)
        data = np.genfromtxt("Data/emg1KT60.csv", delimiter=",", names=["x"])
        self.data = data['x']
        self.currentIndex = 1000
        self.x = list(range(1000))  # 100 time points
        self.y = self.data[0:1000]  # 100 data points
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line = self.graphicsView.plot(self.x, self.y, pen=pen)

        container.addWidget(self.graphicsView)
        self.setLayout(container)
        self.show()


    def handleStart(self):
        print('start')
        self.timer = QtCore.QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.update_plot_data_csv)
        self.timer.start()

    def update_plot_data_csv(self):
        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.

        self.y = self.y[10:]  # Remove the 10 first
        newArr = np.append(self.y, self.data[self.currentIndex:self.currentIndex + 10])
        self.y = newArr
        self.currentIndex = self.currentIndex + 10
        self.data_line.setData(self.x, self.y)  # Update the data.

    def handleStop(self):
        self.timer.stop()

    def setInput(self, input):
        print(input)
        data = np.genfromtxt(input, delimiter=",", names=["x"])
        self.data = data['x']
