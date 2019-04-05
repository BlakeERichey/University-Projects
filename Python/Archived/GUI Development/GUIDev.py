#Demonstrate some basic GUI Development using PyQt5

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QMenu, QTextEdit
from PyQt5.QtGui import QIcon

class BasicWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        menubar = self.menuBar()
        
        exitAct = QAction(QIcon('exit.png'), '&Exit', self) #variable encapsulating the exit command
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip("Exit application.")
        exitAct.triggered.connect(self.quit)

        self.statusbar = self.statusBar()#.showMessage("Ready")
        self.toolbar = self.addToolBar("Exit")
        self.toolbar.addAction(exitAct)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("With Context Menu")
        self.show()

        impAct = QAction("Import mail", self)
        impMenu = QMenu('Import', self)
        impMenu.addAction(impAct)

        newAct = QAction("New", self)

        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)
        fileMenu.addAction(exitAct)

        viewMenu = menubar.addMenu("&View")
        viewStatsAct = QAction("View statusbar", self, checkable=True)
        viewStatsAct.setStatusTip("View Statusbar")
        viewStatsAct.setChecked(True)
        viewStatsAct.triggered.connect(self.toggleMenu)

        viewMenu.addAction(viewStatsAct)

    def toggleMenu(self, state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)

        newAct = cmenu.addAction("New")
        opnAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            self.quit()
            
    def quit(self):
        sys.exit()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BasicWindow()
    sys.exit(app.exec_())
