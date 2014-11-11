from PyQt4.QtGui import*
import sys
from PyQt4.QtGui import*
from PyQt4 import QtGui
from A2_Physics_Propulsion_redone import *
import sys
from PyQt4 import QtGui, QtCore

class QVectorPixmap(QGraphicsPixmapItem):
    """ this is a Pixmap item!"""
    #contructor
    def __init__(self):
        super().__init__()
        self.Image = QPixmap('rocket.jpg')
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setPixmap(self.Image)
        self.Vector = QVector2D()

        
##class AnimationClass(QGraphicsItemAnimation):
##    def __init__(self):
##        self.setItem(QGraphicsItem)
##        print(self)

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

    def CreateVectorItem(self):
        Projectile = QVectorPixmap()
        Item2 =  Projectile.Image.size()
        print(Projectile,Item2)
        return Projectile

   
    def mainMenu(self):
        QGraphicsmain = MyView()
        self.setCentralWidget(QGraphicsmain)
        QGraphicsmain.show()
        QGraphicsmain.raise_()
        TestQGraphics.exec_()
        

class MyView(QtGui.QGraphicsView):
    def __init__(self):
         QtGui.QGraphicsView.__init__(self)
         self.Image = QPixmap('rocket.jpg')
         self.scene = QtGui.QGraphicsScene(self)
         self.item = QtGui.QGraphicsPixmapItem(self.Image)
         #first item is 
         self.scene.addItem(self.item)
         self.setScene(self.scene)

         # Remember to hold the references to QTimeLine and QGraphicsItemAnimation instances.
         # They are not kept anywhere, even if you invoke QTimeLine.start().
         self.tl = QtCore.QTimeLine(14000)
         self.tl.setFrameRange(0, 100)
         self.a = QtGui.QGraphicsItemAnimation()
         self.a.setItem(self.item)
         self.a.setTimeLine(self.tl)

         # Each method determining an animation state (e.g. setPosAt, setRotationAt etc.)
         # takes as a first argument a step which is a value between 0 (the beginning of the
         # animation) and 1 (the end of the animation)
         self.a.setPosAt(0, QtCore.QPointF(0, -10))
         self.a.setRotationAt(0.5, 180)
         self.a.setPosAt(0.9, QtCore.QPointF(-10,100))
         self.a.setPosAt(1, QtCore.QPointF(1000,100))
         

         self.tl.start()


##***********************************************************
##
##  self.Balh < Class you are in).Clicked.Connect(lambda:Blah< Passing to)Passing parameters))
##
##********************************************************

         
if __name__ == "__main__":
    TestQGraphics = QApplication(sys.argv)
    QGraphicsmain = MainWindow()
    QGraphicsmain.show()
    QGraphicsmain.raise_()
    TestQGraphics.exec_()
        

