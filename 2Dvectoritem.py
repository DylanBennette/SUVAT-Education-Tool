from PyQt4.QtGui import*
import sys
from PyQt4.QtGui import*
from PyQt4 import QtGui
from A2_Physics_Propulsion_redone import *

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
        print(Projectile,'sgrgr')
        Item = []
        MoveItem = 1
        while MoveItem == 1:
            Item.append(Projectile.y())
            Item.append(Projectile.Vector.y())
            Item.append(Projectile.x())
            Item.append(Projectile.Vector.x())
            Y = int(input('Input Y Transformation'))
            X = int(input('Input X Transformation'))
            Projectile.setX(X)
            Projectile.setY(Y)
            Item.append(Projectile.y())
            Item.append(Projectile.Vector.y())
            Item.append(Projectile.x())
            Item.append(Projectile.Vector.x())
            for each in Item:
                print(each)
            MoveItem = int(input('Continue'))
        ProjectileScene = QGraphicsScene()
        ProjectileSceneScale = QGraphicsScale()
        ProjectileSceneScale.setXScale(2)
        Item3 = ProjectileSceneScale.xScale()
        ProjectileScene.addItem(Projectile)
        return ProjectileScene,Projectile

   
    def mainMenu(self):
        self.ProjectileScenes = self.CreateVectorItem()
        print(self.ProjectileScenes)
        # graphics view
        self.ProjectileView = QGraphicsView(self.ProjectileScenes)
        #Image Container
        self.SimulationView = QVBoxLayout()
        self.SimulationView.addWidget(self.ProjectileView)
        self.Simulation = QWidget()
        self.Simulation.setLayout(self.SimulationView)
        self.setCentralWidget(self.Simulation)
        self.Simulation.setMinimumSize(self.Simulation.size())
        Item = []
        MoveItem = 1
        while MoveItem == 1:
            print(self.ProjectileView.CreateVectorItem.y())
        
                    
        
        
            
            


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
        

