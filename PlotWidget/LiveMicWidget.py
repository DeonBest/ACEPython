import numpy as np

from PyQt5 import QtGui, QtCore
from Reader.MicRecorder import MicrophoneRecorder
from Reader.MicReader import MicReader
from PlotWidget.ReaderPlotWidget import ReaderPlotWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        super(MplCanvas, self).__init__(fig)
        self.axes.set_ylim(-1500, 1500)

        self.axes.set_xlabel(u'time (ms)', fontsize=6)

class LiveMicWidget(QtGui.QWidget, ReaderPlotWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)

        # customize the UI
        self.initUI()

    def initUI(self):

        hbox_gain = QtGui.QHBoxLayout()
        autoGain = QtGui.QLabel('Auto gain for frequency spectrum')
        autoGainCheckBox = QtGui.QCheckBox(checked=True)
        hbox_gain.addWidget(autoGain)
        hbox_gain.addWidget(autoGainCheckBox)

        # reference to checkbox
        self.autoGainCheckBox = autoGainCheckBox

        hbox_fixedGain = QtGui.QHBoxLayout()
        fixedGain = QtGui.QLabel('Manual gain level for frequency spectrum')
        fixedGainSlider = QtGui.QSlider(QtCore.Qt.Horizontal)
        hbox_fixedGain.addWidget(fixedGain)
        hbox_fixedGain.addWidget(fixedGainSlider)

        self.fixedGainSlider = fixedGainSlider

        vbox = QtGui.QVBoxLayout()

        #vbox.addLayout(hbox_gain)
        #vbox.addLayout(hbox_fixedGain)

        # mpl figure
        self.canvas = MplCanvas(self)
        #vbox.addWidget(self.main_figure.toolbar)
        vbox.addWidget(self.canvas)

        self.setLayout(vbox)

        self.show()

        self.reader = MicReader(self.canvas)

    def handleStart(self):
        self.reader.handleStart()
    def handleStop(self):
        self.reader.handleStop()
    def setInput(self, input):
        self.reader.input(input)

    def initMplWidget(self):
        """creates initial matplotlib plots in the main window and keeps
        references for further use"""
        # top plot
        self.ax_top = self.main_figure.figure.add_subplot(211)
        self.ax_top.set_ylim(-1500, 1500)
        self.ax_top.set_xlim(0, self.time_vect.max())
        self.ax_top.set_xlabel(u'time (ms)', fontsize=6)

        # bottom plot

        # line objects
        self.line_top, = self.ax_top.plot(self.time_vect,
                                          np.ones_like(self.time_vect))
