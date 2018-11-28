#Demonstrate some basic GUI Development using PyQt5

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QMenu
from PyQt5.QtGui import QIcon

class BasicWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        
        exitAct = QAction(QIcon('exit.png'), '&Exit', self) #variable encapsulating the exit command
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip("Exit application.")
        exitAct.triggered.connect(self.quit)

        self.statusBar()#.showMessage("Ready")
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Simple Menu with Submenu")
        self.show()

        impAct = QAction("Import mail", self)
        impMenu = QMenu('Import', self)
        impMenu.addAction(impAct)

        newAct = QAction("New", self)

        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)
        fileMenu.addAction(exitAct)

    def quit(self):
        sys.exit()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BasicWindow()
    sys.exit(app.exec_())
