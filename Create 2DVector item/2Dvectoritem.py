from PyQt4.QtGui import*
from PyQt4.QtGui import*
from PyQt4 import QtGui
from A2_Physics_Propulsion_redone import *

class QGraphicsPixmap(QGraphicsPixmapItem):
    """ this is a Pixmap item!"""
    #contructor
    def __init__(self):
        super(QGraphicsPixmap,self).__init__()
        self.List = ['Rocket.jpg']
        self.graphic = QPixmap(self.List[0])
        self.setPixmap(self.graphic.ScaledToWidth(25,1))

    def UpdateVectorgraphic(self):
        self.VectorList = getSUVAT()
        if self.VerticalAcceleration < 0:
            self.graphic = QPixmap(self.list[0])
            self.setPixmap(self.graphic.scaledToWidth)
        elif self.VerticalAcceleration > 0:
            self.graphic = QPixmap(self.list[1])
            self.setPixmap(self.graphic.scaledToWidth)

class QGraphicsVector(QVector2D):
    """QGraphicsVector"""
    #Constructor
    def __init__(self):
        super(QGraphicsVector,self).__init__()
        self.Vectoritem = QVector2D(0,0)

class QGraphicsPixmapVector(QGraphicsVector,QGraphicsPixmap):
    """vectorable Pixmap"""
    #Constructor
    def __init__(self):
        QGraphicsVector.__init__(self)
        QGraphicsPixmap.__init__(self)

class QGraphicsSimulationScene(QGraphicsScene):
    """this class provides a scene in which to display the graphics item"""
    #Constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle('MainWindow')      


    def VerticalVectoring(self,VerticalAcceleration):
        Propulsion1 = Propulsion()
        Propulsion1.RunTime()
        for each in VerticalAcceleration:
            Xmovement += each
            QGraphicsPixmapVector.setX(Xmovement)

    def mainMenu(self):
        SimulationScene = QGraphicsSimulationScene()
        print(SimulationScene)

        
            



            
if __name__ == "__main__":
    SimulationScene = QGraphicsSimulationScene()
    SimulationScene.mainMenu()

        

