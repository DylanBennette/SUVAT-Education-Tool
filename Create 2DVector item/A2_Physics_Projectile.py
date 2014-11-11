import math
class Projectile():
    def __init__(self,ProjectileName,ProjectileMass,ProjectileDiameter):
        self._ProjectileName = ''
        self._ProjectileMass = 5
        self._ProjectileDiameter = 0

    def getName(self):
        return self._ProjectileName
    def setName(self):
        self._ProjectileName = input("please enter the name of the self here")
    def getMass(self):
        return self._ProjectileMass    
    def setMass(self):
        self._ProjectileMass = int(input("Please input the mass of the object here : "))
    def getDiameter(self):
        return self._ProjectileDiameter
    def setDiameter(self):
        self._ProjectileDiameter = int(input("please input the Diameter of the object :"))
    def getProjectileDetails(self):
        Response = [self.getName(),self.getMass(),self.getDiameter()]
        print(Response)
        return Response
        print(Response)
    def ProjectileChoice(self):
        Projectile1 = StandardProjectile()

class StandardProjectile(Projectile):
    """ A sub-class to simulate a default Projectile"""
    #constructor
    def __init__(self):
        Projectile.__init__(self,'Rock',5,0.20)
                                                                             
