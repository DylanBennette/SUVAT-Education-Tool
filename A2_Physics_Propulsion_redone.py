from decimal import *
import math
import time
from A2_Physics_Projectile import *

class Propulsion():
    def __init__(self,PropulsionName,PropulsionHorizontalForce,PropulsionVerticalForce,PropulsionTotalForce,PropulsionAngle,PropulsionInitialVelocity,PropulsionFinalVelocity,PropulsionAcceleration,PropulsionDisplacement,PropulsionTime,PropulsionGravity):
        self._PropulsionName = ""
        self._PropulsionHorizontalDisplacement = 10
        self._PropulsionVerticalDisplacement = 10
        self._PropulsionHorizontalForce = 0
        self._PropulsionVerticalForce = 0
        self._PropulsionAngle = 45
        self._PropulsionInitialVelocity = 0 
        self._PropulsionFinalVelocity = 0 
        self._PropulsionAcceleration = 0
        self._PropulsionDisplacement = 0 
        self._PropulsionTime = 0
        self._PropulsionGravity = -9.81

    def getName(self):
        return self._PropulsionName
    def setName(self):
        self._PropulsionName = input("please input the Name of tyhe method of self here :")
    def getGravity(self):
        return self._PropulsionGravity
    def setGravity(self):
        self._PropulsionGravity = input("Would you like to change gravity default is -9.81 ms^-2 :")
    def getHorizontalDisplacement(self):
        return self._PropulsionHorizontalDisplacement
    def setHorizontalDisplacement(self,H):
        self._PropulsionHorizontalDisplacement = H
    def getVerticalDisplacement(self):
        return self._PropulsionVerticalDisplacement
    def setVerticalDisplacement(self,V):
        self._PropulsionVerticalDisplacement = V
    def getHorizontalForce(self):
        return self._PropulsionHorizontalForce
    def setHorizontalForce(self):
        self._PropulsionHorizontalForce = int(input("please input the amount of force making th object travel horizontally :"))
    def getVerticalForce(self):
        return self._PropulsionVerticalForce
    def setVerticalForce(self):
        self._PropulsionVerticalForce = int(input("Please input the amount of force in Newtons making the object travel vertically:"))                                   
    def getAngle(self):
        return self._PropulsionAngle
    def setAngle(self):
        self._PropulsionAngle = int(input("please enter the angle at whcich the self is launched at"))
    def getInitialVelocity(self):
        return self._PropulsionInitialVelocity
    def setInitialVelocity(self):
        self._PropulsionInitialVelocity = int(input("Please input the initial velocity"))
        print(self._PropulsionInitialVelocity,'This is it')
    def setInitialVelocitySUVAT(self,U):
        self._PropulsionInitalVelocity = U
    def getFinalVelocity(self):
        return self._PropulsionFinalVelocity
    def setFinalVelocity(self):
        self._PropulsionFinalVelocity = int(input("Please input the Final Velocity when Time"))
        print(self._PropulsionFinalVelocity,'This is it')
    def setFinalVelocitySUVAT(self,V):
        self._PropulsionFinalVelocity = V
    def getAcceleration(self):
        return self._PropulsionAcceleration
    def setAcceleration(self):
        self._PropulsionAcceleration = int(input("please input the value for the acceleration of the object :"))
        print(self._PropulsionAcceleration,'This is it')
    def setAccelerationSUVAT(self,A):
        self._PropulsionAcceleration = A
    def getDisplacement(self):
        return self._PropulsionDisplacement
    def setDisplacement(self):
        self._PropulsionDisplacement = int(input("Please input the displacement of the objcet from it's point of origin :"))
        print(self._PropulsionDisplacement,'This is it')
    def setDisplacementSUVAT(self,S):
        self._PropulsionDisplacement = S 
    def getTime(self):
        return self._PropulsionTime
    def setTime(self):
        self._PropulsionTime = input("Please input how much time the object has been traveling for :")
        print(self._PropulsionTime,'This is it')
    def setTimeSUVAT(self,T):
        self._PropulsionTime = T
    def RunTime(self):
        Start = (time.clock())
        return Start
        

    def getSuvat(self):
        SUVATlist = []
        S = self.getDisplacement()
        U = self.getInitialVelocity()
        V = self.getFinalVelocity()
        A = self.getAcceleration()
        T = self.getTime()
        SUVATlist.append(S)
        SUVATlist.append(U)
        SUVATlist.append(V)
        SUVATlist.append(A)
        SUVATlist.append(T)
        return SUVATlist


##################################
## equations to calculate S
    
    def CalculateDisplacement1(self):
        try:
            # AUT Calc S then Calc V    APPROVED
            SUVATList = self.getSuvat()
            ULocal = SUVATList[1]
            TLocal = SUVATList[4]
            ALocal = SUVATList[3]
            TLocalSquared = TLocal**2
            SLocal = (ULocal*TLocal) + ((ALocal*TLocalSquared)/2)
            print(SLocal,'AUT')
            self.setDisplacementSUVAT(SLocal)
        except:
            print('')

    def CalculateDisplacement2(self):
        try:
            # AVT Calc S then Calc U    APPROVED
            SUVATList = self.getSuvat()
            VLocal = SUVATList[2]
            TLocal = SUVATList[4]
            ALocal = SUVATList[3]
            TLocalSquared = TLocal**2
            SLocal = (VLocal*TLocal) - ((ALocal*TLocalSquared)/2)
            print(SLocal,'AVT')
            self.setDisplacementSUVAT(SLocal)
        except:
            print('')

    def CalculateDisplacement3(self):
        try:
            # AVU Calc S then Calc T   APPROVED
            SUVATList = self.getSuvat()
            ULocal = SUVATList[1]
            ULocalSquared = ULocal**2
            VLocal = SUVATList[2]
            ALocal = SUVATList[3]
            VLocalSquared = VLocal**2
            SLocalSquared = (VLocalSquared - ULocalSquared)/(2*ALocal)
            SLocal = math.sqrt(SLocalSquared)
            print(SLocal,'AVU')
            self.setDisplacementSUVAT(SLocal)
        except:
            print('')

    def CalculateDisplacement4(self):
        try:
            # VUT Calc S then Calc A  APPROVED
            SUVATList = self.getSuvat()
            ULocal = SUVATList[1]
            VLocal = SUVATList[2]
            TLocal = SUVATList[4]
            SLocal = (((ULocal+VLocal)*TLocal)/2)
            print(SLocal,'VUT')
            self.setDisplacementSUVAT(SLocal)
        except:
            print('')

##################################
## equations to calculate U

    def CalculateInitialVelocity1(self):
        try:
            # VAT Calc U then Calc S     APPROVED   
            SUVATList = self.getSuvat()
            VLocal = SUVATList[2]
            ALocal = SUVATList[3]
            TLocal = SUVATList[4]
            ULocal = VLocal - ALocal*TLocal
            print(ULocal,'VAT')
            self.setInitialVelocitySUVAT(ULocal)
        except:
            print('')
            
    def CalculateInitialVelocity2(self):
        try:
            # VST Calc U then Calc A    FAILED   
            SUVATList = self.getSuvat()
            VLocal = SUVATList[2]
            SLocal = SUVATList[0]
            TLocal = SUVATList[4]
            ULocal = ((2*SLocal)/TLocal)-VLocal
            print(ULocal,'VST')
            self.setInitialVelocitySUVAT(ULocal)
        except:
            print('')

    def CalculateInitialVelocity3(self):
        try:
            # VSA Calc U then Calc T   FAILED   
            SUVATList = self.getSuvat()
            VLocal = SUVATList[2]
            VLocalSquared = VLocal**2
            SLocal = SUVATList[0]
            ALocal = SUVATList[3]
            ULocalSquared = VLocalSquared- (2*(ALocal*SLocal))
            ULocal = math.sqrt(ULocalSquared)
            print(ULocal,'VSA')
            self.setInitialVelocitySUVAT(ULocal)
        except:
            print('')

    def CalculateInitialVelocity4(self):
        try:
            # SAT Calc U then Calc V FAILED
            SUVATList = self.getSuvat()
            TLocal = SUVATList[4]
            TLocalSquared = TLocal**2
            SLocal = SUVATList[0]
            ALocal = SUVATList[3]
            ULocal = ((((ALocal*TLocalSquared)*SLocal)/2)/TLocal)
            print(ULocal,'SAT')
            self.setInitialVelocitySUVAT(ULocal)
        except:
            print('')

##################################
## equations to calculate V

    def CalculateFinalVelocity1(self):
        try:
            # UAT Calc V then Calc S   APPROVED   
            SUVATList = self.getSuvat()
            TLocal = SUVATList[4]
            ALocal = SUVATList[3]
            ULocal = SUVATList[1]
            VLocal = ULocal + (ALocal*TLocal)
            print(VLocal,'UAT')
            self.setFinalVelocitySUVAT(VLocal)
        except:
            print('')

    def CalculateFinalVelocity2(self):
        try:
            # UST Calc V then Calc A   APPROVED  
            SUVATList = self.getSuvat()
            TLocal = SUVATList[4]
            SLocal = SUVATList[0]
            ULocal = SUVATList[1]
            VLocal = (((2*SLocal)/TLocal)-ULocal)
            print(VLocal,'UST')
            self.setFinalVelocitySUVAT(VLocal)
        except:
            print('')

    def CalculateFinalVelocity3(self):
        try:
            # USA Calc V then Calc T APPROVED  
            SUVATList = self.getSuvat()
            ALocal = SUVATList[3]
            SLocal = SUVATList[0]
            ULocal = SUVATList[1]
            ULocalSquared = ULocal**2
            VLocalSquared = (ULocalSquared+(2*(ALocal*SLocal)))
            VLocal = math.sqrt(VLocalSquared)
            print(VLocal,'USA')
            self.setFinalVelocitySUVAT(VLocal)
        except:
            print('')

    def CalculateFinalVelocity4(self):
        try:
            # SAT Calc V then Calc U APPROVED 
            SUVATList = self.getSuvat()
            ALocal = SUVATList[3]
            SLocal = SUVATList[0]
            TLocal = SUVATList[4]
            TLocalSquared = TLocal**2
            VLocal = SLocal +(((ALocal*TLocalSquared)/2)/TLocal)
            print(VLocal,'SAT')
            self.setFinalVelocitySUVAT(VLocal)
        except:
            print('')

##################################
## equations to calculate A

    def CalculateAcceleration1(self):
        try:
            # VUT Calc A then Calc U  APPROVED
            SUVATList = self.getSuvat()
            VLocal = SUVATList[2]
            ULocal = SUVATList[1]
            TLocal = SUVATList[4]
            ALocal = (VLocal-ULocal)/TLocal
            print(ALocal,'VST')
            self.setAccelerationSUVAT(ALocal)
        except:
            print('')

    def CalculateAcceleration2(self):
        try:
        # TVS Calc A then Calc T APPROVED
            SUVATList = self.getSuvat()
            VLocal = SUVATList[2]
            SLocal = SUVATList[0]
            TLocal = SUVATList[4]
            TLocalSquared = VLocal**2
            ALocal = (SLocal-(VLocal*TLocal)/TLocalSquared)
            print(ALocal,'VSU')
            self.setAccelerationSUVAT(ALocal)
        except:
            print('')

    def CalculateAcceleration3(self):
        try:
            # TUS Calc A then Calc S  APPROVED
            SUVATList = self.getSuvat()
            SLocal = SUVATList[2]
            ULocal = SUVATList[1]
            TLocal = SUVATList[4]
            TLocalSquared = TLocal**2
            ALocal = (2*(SLocal+ULocal*TLocal)/TLocalSquared)
            print(ALocal,'TUS')
            self.setAccelerationSUVAT(ALocal)
        except:
            print('Failed')

    def CalculateAcceleration4(self):
        try:
            # USV Calc A then Calc V  FAILED
            SUVATList = self.getSuvat()
            VLocal = SUVATList[2]
            VLocalSquared = VLocal**2
            SLocal = SUVATList[0]
            ULocal = SUVATList[4]
            ULocalSquared = TLocal**2
            ALocal = (VLocalSquared-ULocalSquared)/(2*SLocal)
            print(ALocal,'VST')
            self.setAccelerationSUVAT(ALocal)
        except:
            print('')

##################################
## equations to calculate T

    def CalculateTime1(self):
   #     try:
            # SAU Calc T then Calc A  APPROVED
            SUVATList = self.getSuvat()
            VLocal = SUVATList[2]
            SLocal = SUVATList[0]
            ULocal = SUVATList[1]
            TLocal = (2*SLocal)/(ULocal+VLocal)
            print(TLocal,'VUS')
            self.setTimeSUVAT(VLocal)
  #      except:
            print('')

    def CalculateTime2(self):
        try:
            # SAV Calc T then Calc U  APPROVED
            SUVATList = self.getSuvat()
            VLocal = SUVATList[2]
            SLocal = SUVATList[0]
            ALocal = SUVATList[3]
            TLocalSquared = (SLocal/VLocal)-(ALocal/2)
            TLocal = math.sqrt(TLocalSquared)
            print(TLocal,'VAS')
            self.setTimeSUVAT(TLocal)
        except:
            print('')
            
    def CalculateTime3(self):
        try:
            # SUV Calc T then Calc S APPROVED 
            SUVATList = self.getSuvat()
            VLocal = SUVATList[2]
            ULocal = SUVATList[1]
            SLocal = SUVATList[0]
            TLocal = (2*SLocal)-(VLocal+ULocal)
            print(TLocal,'SUV')
            self.setTimeSUVAT(TLocal)
        except:
            print('')

    def CalculateTime4(self):
        #try:
            # VUA Calc T then Calc V  APPROVED
            SUVATList = self.getSuvat()
            ULocal = SUVATList[1]
            VLocal = SUVATList[2]
            ALocal = SUVATList[3]
            TLocal = (VLocal-ULocal)/ALocal
            print(TLocal,'UAS')
            self.setTimeSUVAT(TLocal)
      #  except:
            print('')

##################################
## equations in second stage
        
    def CalculateDisplacement4Values(self):
        try:
            # S = (UT + (1/2 A(T^2)))
            SUVATList = self.getSuvat()
            ULocal = SUVATList[1]
            VLocal = SUVATList[2]
            ALocal = SUVATList[3]
            TLocal = SUVATList[4]
            TLocalSquared = TLocal**2
            SLocal = (ULocal*TLocal + (1/2(ALocal*TLocalSquared)))
            print(SLocal,'Displacement 2nd Stage')
            self.setDisplacementSUVAT(SLocal)
        except:
            print('')

    def CalculateInitialVelocity4Values(self):
        try:
            # U = V-AT
            SUVATList = self.getSuvat()
            VLocal = SUVATList[2]
            ALocal = SUVATList[3]
            TLocal = SUVATList[4]
            ULocal = (VLocal-(ALocal*TLocal))
            print(ULocal,'InitialVelocity 2nd Stage')
            self.setInitialVelocitySUVAT(ULocal)
        except:
            print('')

    def CalculateFinalVelocity4Values(self):
        try:
            # V = U+AT
            SUVATList = self.getSuvat()
            ULocal = SUVATList[1]
            ALocal = SUVATList[3]
            TLocal = SUVATList[4]
            VLocal = ULocal+ALocal*TLocal
            print(VLocal,'FinalVelocity 2nd Stage')
            self.setFinalVelocitySUVAT(VLocal)
        except:
            print('')

    def CalculateAcceleration4Values(self):
        try:
            # A = V-U/T
            SUVATList = self.getSuvat()
            ULocal = SUVATList[1]
            VLocal = SUVATList[2]
            TLocal = SUVATList[4]
            ALocal = VLocal-ULocal/TLocal
            print(ALocal,'acceleration 2nd Stage')
            self.setAccelerationSUVAT(ALocal)
        except:
            print('')

    def CalculateTime4Values(self):
        try:
            # T = V-U/A
            SUVATList = self.getSuvat()
            ULocal = SUVATList[1]
            VLocal = SUVATList[2]
            ALocal = SUVATList[3]
            TLocal = ((VLocal-ULocal)/ALocal)
            print(ALocal,'acceleration 2nd Stage')
            self.setTimeSUVAT(TLocal)
        except:
            print('')
        
##################################
## Inputs and Validation

    def SUVATInputs(self,InputList):
        SUVATValid = False
        SUVATList = []
        SUVATItemList =[]
        NumberSelected = 0
        if InputList[0] != 0 and 'Displacement' not in SUVATItemList:
            self.setDisplacementSUVAT(InputList[0])
            SUVATList.append('S')
            SUVATItemList.append('Displacement')
            NumberSelected +=1
        if InputList[1] != 0 and 'InitialVelocity' not in SUVATItemList:
            result = self.setInitialVelocitySUVAT(InputList[1])
            SUVATList.append('U')
            SUVATItemList.append('InitialVelocity')
            NumberSelected +=1
        if InputList[2] != 0 and 'FinalVelocity' not in SUVATItemList:
            result = self.setFinalVelocitySUVAT(InputList[2])
            SUVATList.append('V')
            SUVATItemList.append('FinalVelocity')
            NumberSelected +=1
        if InputList[3] != 0 and 'Acceleration' not in SUVATItemList:
            result = self.setAccelerationSUVAT(InputList[3])
            SUVATList.append('A')
            SUVATItemList.append('Acceleration')
            NumberSelected +=1
        if InputList[4] != 0 and 'Time' not in SUVATItemList:
            result = self.setTimeSUVAT(InputList[4])
            SUVATList.append('T')
            SUVATItemList.append('Time')
            NumberSelected +=1
        #print(SUVATItemList)
        return SUVATList

    def SUVATLink(self,SUVATList):
        ### SUVAT equation Matrix
        SUVATValid = False
        print(SUVATList)
        Item1 = str(SUVATList[0])
        Item2 = str(SUVATList[1])
        Item3 = str(SUVATList[2])
        SUVATListComparison=''
        Count = 1
        while SUVATValid != True:
            print(SUVATListComparison,Count)
            if Count == 1:
                SUVATListComparison = (Item1+Item2+Item3)
            elif Count == 2:
                SUVATListComparison = (Item1+Item3+Item2)
            elif Count == 3:
                SUVATListComparison = (Item2+Item1+Item3)
            elif Count == 4:
                SUVATListComparison = (Item2+Item3+Item1)
            elif Count == 5:
                SUVATListComparison = (Item3+Item1+Item2)
            elif Count == 6:
                SUVATListComparison = (Item3+Item2+Item1)
            if SUVATListComparison == 'VAT' or SUVATListComparison == 'VTA':
                self.CalculateInitialVelocity1()
                self.CalculateDisplacement4Values()
            elif SUVATListComparison == 'VST' or SUVATListComparison == 'VTS':
                self.CalculateInitialVelocity2()
                self.CalculateAcceleration4Values()
            elif SUVATListComparison == 'VSA' or SUVATListComparison == 'VAS':
                self.CalculateInitialVelocity3()
                self.CalculateTime4Values()
            elif SUVATListComparison == 'SAT' or SUVATListComparison == 'STA':
                self.CalculateInitialVelocity4()
                self.CalculateFinalVelocity4Values()
            elif SUVATListComparison == 'UAT' or SUVATListComparison == 'UTA':
                self.CalculateFinalVelocity1()
                self.CalculateDisplacement4Values()
            elif SUVATListComparison == 'UST' or SUVATListComparison == 'UTS':
                self.CalculateFinalVelocity2()
                self.CalculateAcceleration4Values()
            elif SUVATListComparison == 'USA'or SUVATListComparison == 'UAS':
                self.CalculateFinalVelocity3()
                self.CalculateTime4Values()
            elif SUVATListComparison == 'SAT' or SUVATListComparison == 'STA':
                self.CalculateFinalVelocity4()
                self.CalculateInitialVelocity4Values()
            elif SUVATListComparison == 'AUT' or SUVATListComparison == 'ATU':
                self.CalculateDisplacement1()
                self.CalculateFinalVelocity4Values()
            elif SUVATListComparison == 'AVT' or SUVATListComparison == 'ATV':
                self.CalculateDisplacement2()
                self.CalculateInitialVelocity4Values()
            elif SUVATListComparison == 'AVU' or SUVATListComparison == 'AUV':
                self.CalculateDisplacement3()
                self.CalculateTime4Values()
            elif SUVATListComparison == 'VUT' or SUVATListComparison == 'VTU':
                self.CalculateDisplacement4()
                self.CalculateAcceleration4Values()
            elif SUVATListComparison == 'SAU' or SUVATListComparison == 'SUA':
                self.CalculateTime1()
                self.CalculateFinalVelocity4Values()
            elif SUVATListComparison == 'SAV' or SUVATListComparison == 'SVA':
                self.CalculateTime2()
                self.CalculateInitialVelocity4Values()
            elif SUVATListComparison == 'SUV' or SUVATListComparison == 'SVU':
                self.CalculateTime3()
                self.CalculateAcceleration4Values()
            elif SUVATListComparison == 'VUA' or SUVATListComparison == 'VAU':
                self.CalculateTime4()
                self.CalculateDisplacement4Values()
            elif SUVATListComparison == 'TUV' or SUVATListComparison == 'TVU':
                self.CalculateAcceleration1()
                self.CalculateDisplacement4Values()
            elif SUVATListComparison == 'TVS' or SUVATListComparison == 'TSV':
                self.CalculateAcceleration2()
                self.CalculateInitialVelocity4Values()
            elif SUVATListComparison == 'TUS' or SUVATListComparison == 'TSU':
                self.CalculateAcceleration3()
                self.CalculateFinalVelocity4Values()
            elif SUVATListComparison == 'USV' or SUVATListComparison == 'UVS':
                self.CalculateAcceleration4()
                self.CalculateTime4Values()
            Count +=1
            if Count == 6:
                SUVATValid = True
            
        
    def CalculateInitialVectors(self):
        Projectile1 = Projectile('Rock',5,5)
        if self.getVerticalForce() == 0 and self.getHorizontalForce() == 0:
            #getcontext().prec = 6
            #Decimal('1')+
            VerticalVectorList = []
            Acceleration = self.getAcceleration()
            Mass = Projectile1.getMass()
            Angle = math.radians(self.getAngle())
            ULocal = self.getInitialVelocity()
            GLocal = self.getGravity()
            GLocalSquared = GLocal*abs(GLocal)
            F = Acceleration*Mass 
            Fh = F*math.cos(Angle)
            HorizontalVector = Fh/Mass
            FvInitial = F*math.sin(Angle)
            FvD = ((ULocal*ULocal)/GLocalSquared)
            FvDabs = abs(FvD)
            self.setVerticalDisplacement(FvDabs)
            Weight = GLocal*Projectile1.getMass()
            print(self.getTime())
            WeightDistributed = Weight/self.getTime()
            Acceleration = Acceleration+ ULocal
            TotalTime = self.getTime()
            SecondCounter = 1
            TotalTimeSimplified = round(TotalTime)
            RealTime = 0
            while RealTime < TotalTimeSimplified:
                RealTime = self.RunTime()
                if SecondCounter == int(RealTime):
                    Acceleration = Acceleration + WeightDistributed
                    VerticalVectorList.append(Acceleration)
                    print(Acceleration)
                    SecondCounter += 1
            return HorizontalVector,VerticalVectorList













                    
# A due to gravity = a due to gravity* real time
#every 0.1 seconds* Adue to gravity new apply it to A original

    def StartSimulation(self):
        self.CalculateInitialVectors()
    def Propulsionmain(self):
        SUVATList = self.SUVATInputs()
        self.SUVATLink(SUVATList)
        SUVAT = self.getSuvat()
        print('\n',SUVAT,'\n')
        self.StartSimulation()

if __name__ == "__main__":
    Projectile1 = Projectile('Rock',5,5)
    Propulsion = Propulsion('Spaceship',10,10,0,45,0,0,0,0,0,-9.81)
    Propulsion.Propulsionmain()
    
    
    
   
                                               
