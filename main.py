import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon
#from MainWidgets.PatternRecDataCollectionWidget import Ui_PatternRecDC
from MainWidgets.QuickCollectDataCollectionWidget import Ui_QuickCollectDC



class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.ui = Ui_QuickCollectDC()
        self.ui.setupUi(self)
        exitAct = QAction(QIcon('exit.png'), ' &Quit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&Perspective')
        fileMenu.addAction(exitAct)

        self.setGeometry(1000, 1000, 1000, 1000)
        self.setWindowTitle('ACE')

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())
