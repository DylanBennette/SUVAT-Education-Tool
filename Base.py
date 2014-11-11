import math

class Projectile():
    def __init__(self,ProjectileName,ProjectileMass,ProjectileDiameter):
        self._ProjectileName = ''
        self._ProjectileMass = 0
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
        Name = self.getName()
        Mass = self.getMass()
        Diameter = self.getDiameter()
        Response = [Name,Mass,Diameter]
        return Response
        
    def ProjectileChoice(self):
        Projectile1 = StandardProjectile()
        print(Projectile1)
        print(Projectile1.getProjectileDetails())

class StandardProjectile(Projectile):
    """ A sub-class to simulate a default Projectile"""
    #constructor
    def __init__(self):
        Projectile.__init__(self,'Rock',5,0.20)
                                                                             
class Propulsion():
    def __init__(self,PropulsionName,PropulsionHorizontalForce,PropulsionVerticalForce,PropulsionTotalForce,PropulsionAngle,PropulsionInitialVelocity,PropulsionFinalVelocity,PropulsionAcceleration,PropulsionDisplacement,PropulsionTime):
        self._PropulsionName = ""
        self._PropulsionHorizontalForce = 10
        self._PropulsionVerticalForce = 10
        self._PropulsionTotalForce = 20
        self._PropulsionAngle = 25
        self._PropulsionInitialVelocity = 25
        self._PropulsionFinalVelocity = 0
        self._PropulsionAcceleration = 15
        self._PropulsionDisplacement = 20
        self._PropulsionTime = 0

    def getName(self):
        return self._PropulsionName
    def setName(self):
        self._PropulsionName = input("please input the Name of tyhe method of self here :")
    def getHorizontalForce(self):
        return self._PropulsionHorizontalForce
    def setHorizontalForce(self):
        self._PropulsionHorizontalForce = int(input("please input the amount of force making th object travel horizontally :"))
    def getVerticalForce(self):
        return self._PropulsionVerticalForce
    def setVerticalForce(self):
        self._PropulsionVerticalForce = int(input("Please input the amount of force in Newtons making the object travel vertically :"))
    def getTotalForce(self):
        return self._PropulsionTotalForce
    def setTotalForce(self):
        self._PropulsionTotalForce = int(input("Please input the Total Force Exerted on the object in Newtons :"))
    def getAngle(self):
        return self._PropulsionAngle
    def setAngle(self):
        self._PropulsionAngle = int(input("please enter the angle at whcich the self is launched at"))
    def getInitialVelocity(self):
        return self._PropulsionInitialVelocity
    def setInitialVelocity(self):
        self._PropulsionInitalVelocity = int(input("Please input the initial velocity when Time = 0:"))
    def getFinalVelocity(self):
        return self._PropulsionFinalVelocity
    def setFinalVelocity(self):
        self._PropulsionFinalVelocity = int(input("Please input the Final Velocity when Time is at its maximum :"))
    def getAcceleration(self):
        return self._PropulsionAcceleration
    def setAcceleration(self):
        self._PropulsionAcceleration = int(input("please input the value for the acceleration of the object :"))
    def getDisplacement(self):
        return self._PropulsionDisplacement
    def setDisplacement(self):
        self._PropulsionDisplacement = int(input("Please input the displacement of the objcet from it's point of origin :"))
    def getTime(self):
        return self._PropulsionTime
    def setTime(self):
        self._PropulsionTime = int(input("Please input how much time the object has been traveling for :"))

    def PropulsionChoice(self):
        Propulsion1 = Propulsion('Thrown',15,15,30,32,5,5,4,20,0)
        Propulsion2 = Propulsion('Thrown',15,15,30,32,0,5,4,20,0)
##        print(Propulsion1)
##        print(Propulsion1.getPropulsionDetails())
        Propulsion1.CalculateFinalVelocity()
        Propulsion2.CalculateInitialVelocity()
        

    def CalculateFinalVelocity(self):
        #V^2 = U^2 +2as
        """Organises the Attributes properties into locals so they can be calculated"""
        
        LocalInitialVelocity = self.getInitialVelocity()
        LocalDisplacement = self.getDisplacement()
        LocalAcceleration = self.getAcceleration()
        LocalFinalVelocity = 0
        FinalVelocitysquared = LocalFinalVelocity**2
        InitialVelocitysquared = LocalInitialVelocity**2
        FinalVelocitysquared = InitialVelocitysquared +(2*(LocalAcceleration*LocalDisplacement))
        FinalVelocity= math.sqrt(FinalVelocitysquared)
        print(FinalVelocity)
        
    def CalculateInitialVelocity(self):
        #U^2 = V^2 -2as
        """Organises the Attributes properties into locals so they can be calculated"""
        
        LocalFinalVelocity = self.getFinalVelocity()
        LocalDisplacement = self.getDisplacement()
        LocalAcceleration = self.getAcceleration()
        LocalInitialVelocity = 0
        InitialVelocitysquared = LocalInitialVelocity**2
        FinalVelocitysquared = LocalFinalVelocity**2
        CalculatedInitialVelocitysquared = FinalVelocitysquared -(2*(LocalAcceleration*LocalDisplacement))
        FinalInitialVelocity= math.sqrt(CalculatedInitialVelocitysquared)
        print(FinalInitialVelocity)










        
##        LocalFinalVelocity = self.getFinalVelocity()
##        LocalDisplacement = self.getDisplacement()
##        LocalAcceleration = self.getAcceleration()
##        LocalInitialVelocity = 0
##        InitialVelocitysquared = LocalInitialVelocity**2
##        FinalVelocitysquared = LocalFinalVelocity**2
##        FinalVelocitysquared = FinalVelocitysquared -(2*(LocalAcceleration*LocalDisplacement))
##        FinalInitialVelocity = math.sqrt(FinalVelocitysquared)
##        print(FinalVelocity)

        

    def getPropulsionDetails(self):
        Name = self.getName()
        HorizontalForce = self.getHorizontalForce()
        VerticalForce = self.getVerticalForce()
        TotalForce = self.getTotalForce()
        Angle = self.getAngle()
        InitialVelocity = self.getInitialVelocity()
        FinalVelocity = self.getFinalVelocity()
        Acceleration = self.getAcceleration()
        Displacement = self.getDisplacement()
        Time = self.getTime()
        Response = [Name,HorizontalForce,VerticalForce,TotalForce,Angle,InitialVelocity,FinalVelocity,Angle,InitialVelocity,FinalVelocity,Acceleration,Displacement,Time]
        return Response
        
class StandardPropulsion(Propulsion):
    """A sub-class to simulate a defult Propulsion"""
    #constructor
    def __init__(self):
        Propulsion.__init__(self,'Thrown',15,15,30,32,5,5,4,20,0)
    

        
        
        
if __name__ == "__main__":

    Selection1 = Projectile('Rock',5,0.20) 
    Selection1.ProjectileChoice()
    Selection2 = Propulsion('Thrown',15,15,30,32,5,5,4,20,0)
    Selection2.PropulsionChoice()
    

                                               
