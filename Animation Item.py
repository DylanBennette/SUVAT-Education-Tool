from PyQt4.QtGui import*
import sys
from PyQt4.QtGui import*
from PyQt4 import QtGui
from A2_Physics_Propulsion_redone import *

class AnimationClass(QGraphicsItemAnimation):
    def __init__(self):
        super().__init()
        self.Image = 

class MainWindow(QMainWindow):
    #Constructor
    def __init__(self):
        #Parentconstructor
        super().__init__()
        self.setWindowTitle('VectorItem')
        self.make_menubar()

    def make_menubar(self):
        DisplayEditor = QtGui.QAction(QtGui.QIcon("Main.png"),"&Main", self)
        DisplayEditor.setShortcut("Ctrl+M")
        DisplayEditor.setStatusTip("Main")
        DisplayEditor.triggered.connect(self.mainMenu)

        
        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&Main")
        fileMenu.addAction(DisplayEditor)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("menu bar")
        self.show()

 if __name__ == "__main__":
    TestQGraphics = QApplication(sys.argv)
    QGraphicsmain = MainWindow()
    QGraphicsmain.show()
    QGraphicsmain.raise_()
    TestQGraphics.exec_()
        

