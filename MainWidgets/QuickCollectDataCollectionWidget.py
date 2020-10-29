# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QuickCollectDataCollectionWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
from random import randint
import struct
import numpy as np
import glob
from MainWidgets.LiveMicWidget import LiveMicWidget
from MainWidgets.CSVGraphWidget import CSVGraphWidget
import matplotlib.pyplot as plt


import random

class Ui_QuickCollectDC(QtWidgets.QWidget):

    def setupUi(self, Collection):
        Collection.setObjectName("Collection")
        Collection.resize(1280, 711)
        self.layoutWidget = QtWidgets.QWidget(Collection)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 938, 513))
        self.layoutWidget.setObjectName("layoutWidget")
        self.mainGridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.mainGridLayout.setContentsMargins(30, 30, 30, 30)
        self.mainGridLayout.setObjectName("mainGridLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.mainGridLayout.addWidget(self.label_2, 9, 0, 1, 1)
        self.actionLabelContainer = QtWidgets.QHBoxLayout()
        self.actionLabelContainer.setObjectName("actionLabelContainer")
        self.mainGridLayout.addLayout(self.actionLabelContainer, 0, 2, 1, 1)

        #GRAPH
        #Mic
        self.liveView = LiveMicWidget()
        #CSV
        self.fileView = CSVGraphWidget()
        self.fileView.hide()


        self.liveView.setObjectName("liveView")
        self.fileView.setObjectName("fileView")
        self.mainGridLayout.addWidget(self.liveView, 1, 0, 1, 1)
        self.mainGridLayout.addWidget(self.fileView, 1, 0, 1, 1)
        self.streamLabel = QtWidgets.QLabel(self.layoutWidget)
        self.streamLabel.setObjectName("streamLabel")
        self.mainGridLayout.addWidget(self.streamLabel, 7, 0, 1, 1)
        self.streamContainer = QtWidgets.QHBoxLayout()
        self.streamContainer.setObjectName("streamContainer")
        self.recButton = QtWidgets.QPushButton(self.layoutWidget)
        self.recButton.setObjectName("recButton")
        self.streamContainer.addWidget(self.recButton)
        self.startButton = QtWidgets.QPushButton(self.layoutWidget)
        self.startButton.setObjectName("startButton")
        self.streamContainer.addWidget(self.startButton)
        self.stopButton = QtWidgets.QPushButton(self.layoutWidget)
        self.stopButton.setObjectName("stopButton")
        self.streamContainer.addWidget(self.stopButton)
        self.mainGridLayout.addLayout(self.streamContainer, 8, 0, 1, 1)
        self.inputTypeContainer = QtWidgets.QVBoxLayout()
        self.inputTypeContainer.setObjectName("inputTypeContainer")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("inputTypeLabel")
        self.label.setText('Input Type')
        self.inputTypeContainer.addWidget(self.label)
        self.DAQRadio = QtWidgets.QRadioButton(self.layoutWidget)
        self.DAQRadio.setObjectName("DAQRadio")
        self.DAQRadio.setText("DAQ")
        self.DAQRadio.toggled.connect(lambda: self.inputRadioState(self.DAQRadio))
        self.inputTypeContainer.addWidget(self.DAQRadio)
        self.fileRadio = QtWidgets.QRadioButton(self.layoutWidget)
        self.fileRadio.setObjectName("fileRadio")
        self.fileRadio.setText("File")
        self.fileRadio.toggled.connect(lambda: self.inputRadioState(self.fileRadio))
        self.inputTypeContainer.addWidget(self.fileRadio)
        self.inputDropdown = QtWidgets.QComboBox(self.layoutWidget)
        self.inputDropdown.setObjectName("inputDropdown")
        self.inputTypeContainer.addWidget(self.inputDropdown)
        self.mainGridLayout.addLayout(self.inputTypeContainer, 8, 2, 1, 1)
        self.channelSelectContainer = QtWidgets.QHBoxLayout()
        self.channelSelectContainer.setObjectName("channelSelectContainer")
        self.channel1Button = QtWidgets.QPushButton(self.layoutWidget)
        self.channel1Button.setMinimumSize(QtCore.QSize(50, 50))
        self.channel1Button.setMaximumSize(QtCore.QSize(50, 50))
        self.channel1Button.setObjectName("channel1Button")
        self.channelSelectContainer.addWidget(self.channel1Button)
        self.channel2Button = QtWidgets.QPushButton(self.layoutWidget)
        self.channel2Button.setMinimumSize(QtCore.QSize(50, 50))
        self.channel2Button.setMaximumSize(QtCore.QSize(50, 50))
        self.channel2Button.setObjectName("channel2Button")
        self.channelSelectContainer.addWidget(self.channel2Button)
        self.channel3Button = QtWidgets.QPushButton(self.layoutWidget)
        self.channel3Button.setMinimumSize(QtCore.QSize(50, 50))
        self.channel3Button.setMaximumSize(QtCore.QSize(50, 50))
        self.channel3Button.setObjectName("channel3Button")
        self.channelSelectContainer.addWidget(self.channel3Button)
        self.channel4Button = QtWidgets.QPushButton(self.layoutWidget)
        self.channel4Button.setMinimumSize(QtCore.QSize(50, 50))
        self.channel4Button.setMaximumSize(QtCore.QSize(50, 50))
        self.channel4Button.setObjectName("channel4Button")
        self.channelSelectContainer.addWidget(self.channel4Button)
        self.channel5Button = QtWidgets.QPushButton(self.layoutWidget)
        self.channel5Button.setMinimumSize(QtCore.QSize(50, 50))
        self.channel5Button.setMaximumSize(QtCore.QSize(50, 50))
        self.channel5Button.setObjectName("channel5Button")
        self.channelSelectContainer.addWidget(self.channel5Button)
        self.channel6Button = QtWidgets.QPushButton(self.layoutWidget)
        self.channel6Button.setMinimumSize(QtCore.QSize(50, 50))
        self.channel6Button.setMaximumSize(QtCore.QSize(50, 50))
        self.channel6Button.setObjectName("channel6Button")
        self.channelSelectContainer.addWidget(self.channel6Button)
        self.channel7Button = QtWidgets.QPushButton(self.layoutWidget)
        self.channel7Button.setMinimumSize(QtCore.QSize(50, 50))
        self.channel7Button.setMaximumSize(QtCore.QSize(50, 50))
        self.channel7Button.setObjectName("channel7Button")
        self.channelSelectContainer.addWidget(self.channel7Button)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton.setObjectName("pushButton")
        self.channelSelectContainer.addWidget(self.pushButton)
        self.channelAllButton = QtWidgets.QPushButton(self.layoutWidget)
        self.channelAllButton.setMinimumSize(QtCore.QSize(50, 50))
        self.channelAllButton.setMaximumSize(QtCore.QSize(50, 50))
        self.channelAllButton.setObjectName("channelAllButton")
        self.channelSelectContainer.addWidget(self.channelAllButton)
        self.mainGridLayout.addLayout(self.channelSelectContainer, 10, 0, 2, 1)
        self.actionContainer = QtWidgets.QVBoxLayout()
        self.actionContainer.setObjectName("actionContainer")
        self.selectActionContainer = QtWidgets.QHBoxLayout()
        self.selectActionContainer.setContentsMargins(-1, -1, 150, -1)
        self.selectActionContainer.setObjectName("selectActionContainer")
        self.featureLabel = QtWidgets.QLabel(self.layoutWidget)
        self.featureLabel.setMaximumSize(QtCore.QSize(50, 16777215))
        self.featureLabel.setObjectName("featureLabel")
        self.selectActionContainer.addWidget(self.featureLabel)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.selectActionContainer.addWidget(self.comboBox)
        self.timeStepLabel = QtWidgets.QLabel(self.layoutWidget)
        self.timeStepLabel.setObjectName("timeStepLabel")
        self.selectActionContainer.addWidget(self.timeStepLabel)
        self.timeStepInput = QtWidgets.QLineEdit(self.layoutWidget)
        self.timeStepInput.setMaximumSize(QtCore.QSize(50, 400))
        self.timeStepInput.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.timeStepInput.setObjectName("timeStepInput")
        self.selectActionContainer.addWidget(self.timeStepInput)
        self.actionContainer.addLayout(self.selectActionContainer)
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.layoutWidget)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.actionContainer.addWidget(self.graphicsView_2)
        self.mainGridLayout.addLayout(self.actionContainer, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.mainGridLayout.addItem(spacerItem, 2, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.mainGridLayout.addItem(spacerItem1, 1, 1, 1, 1)

        self.retranslateUi(Collection)
        QtCore.QMetaObject.connectSlotsByName(Collection)

        #Button Handling
        self.recButton.clicked.connect(self.handleRecButtonPress)
        self.startButton.clicked.connect(self.handleStartButton)
        self.stopButton.clicked.connect(self.handleStopButton)

    def retranslateUi(self, Collection):
        _translate = QtCore.QCoreApplication.translate
        Collection.setWindowTitle(_translate("Collection", "Form"))
        self.label_2.setText(_translate("Collection", "Channels"))
        self.streamLabel.setText(_translate("Collection", "Stream"))
        self.recButton.setText(_translate("Collection", "Rec"))
        self.startButton.setText(_translate("Collection", "Start"))
        self.stopButton.setText(_translate("Collection", "Stop"))
        self.channel1Button.setText(_translate("Collection", "1"))
        self.channel2Button.setText(_translate("Collection", "2"))
        self.channel3Button.setText(_translate("Collection", "3"))
        self.channel4Button.setText(_translate("Collection", "4"))
        self.channel5Button.setText(_translate("Collection", "5"))
        self.channel6Button.setText(_translate("Collection", "6"))
        self.channel7Button.setText(_translate("Collection", "7"))
        self.pushButton.setText(_translate("Collection", "8"))
        self.channelAllButton.setText(_translate("Collection", "All"))
        self.featureLabel.setText(_translate("Collection", "Feature"))
        self.timeStepLabel.setText(_translate("Collection", "Time Step"))
    def handleRecButtonPress(self):
        print('Rec Button pressed')
    def handleStartButton(self):
        if self.DAQRadio.isChecked() == True:
            self.liveView.handleStart()

        if self.fileRadio.isChecked() == True:
            self.fileView.setInput(self.inputDropdown.currentText())
            self.fileView.handleStart()

    def handleStopButton(self):
        print('Stop Button pressed')
        if self.DAQRadio.isChecked() == True:
            self.liveView.handleStop()

        if self.fileRadio.isChecked() == True:
            self.fileView.handleStop()

    def inputRadioState(self, b):
        if b.text() == "DAQ":
            if b.isChecked() == True:
                self.fileView.hide()
                self.liveView.show()
                self.inputDropdown.clear()
                self.inputDropdown.addItem("Mic")

        if b.text() == "File":
            if b.isChecked() == True:
                self.liveView.hide()
                self.fileView.show()
                self.inputDropdown.clear()
                for file in glob.glob("Data/*.csv"):
                    print(file)
                    self.inputDropdown.addItem(file)

        print('end')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Collection = QtWidgets.QWidget()
    ui = Ui_QuickCollectDC()
    ui.setupUi(Collection)
    Collection.show()
    sys.exit(app.exec_())
