import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon
import PyQt5.QtGui as QtGui
from MainWidgets.PatternRecDataCollectionWidget import Ui_PatternRecDC
from MainWidgets.QuickCollectDataCollectionWidget import Ui_QuickCollectDC



class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        #Initialize Main UI's
        self.quickCollectUI = Ui_QuickCollectDC()
        self.patternRecUI = Ui_PatternRecDC()

        self.central_widget = QtGui.QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.central_widget.addWidget(self.patternRecUI)
        self.central_widget.addWidget(self.quickCollectUI)
        self.central_widget.setCurrentWidget(self.quickCollectUI)

        #Setup File Menu Items
        patternRecPerspective = QAction("&Pattern Rec", self)
        patternRecPerspective.setStatusTip('Pattern Recognition')
        patternRecPerspective.triggered.connect(lambda: self.handlePerspectiveChange('patternRec'))
        quickCollectPerspective = QAction("&Quick Collect", self)
        quickCollectPerspective.setStatusTip('Quick Collect')
        quickCollectPerspective.triggered.connect(lambda: self.handlePerspectiveChange('quickCollect'))
        exitAct = QAction(QIcon('exit.png'), ' &Quit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        fileMenu = menubar.addMenu('&Perspective')
        fileMenu.addAction(patternRecPerspective)
        fileMenu.addAction(quickCollectPerspective)
        fileMenu.addAction(exitAct)


        self.setGeometry(1000, 1000, 1000, 1000)
        self.setWindowTitle('ACE')

        self.show()
    def handlePerspectiveChange(self, perspective):
        print(perspective)
        if(perspective=='patternRec'):
            self.central_widget.setCurrentWidget(self.patternRecUI)
        elif(perspective=='quickCollect'):
            self.central_widget.setCurrentWidget(self.quickCollectUI)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())
