import math
import time
from A2_Physics_Projectile import *

class Propulsion():
    def __init__(self,PropulsionName,PropulsionHorizontalForce,PropulsionVerticalForce,PropulsionTotalForce,PropulsionAngle,PropulsionInitialVelocity,PropulsionFinalVelocity,PropulsionAcceleration,PropulsionDisplacement,PropulsionTime,PropulsionGravity):
        self._PropulsionName = ""
        self._PropulsionHorizontalDisplacement = 10
        self._PropulsionVerticalDisplacement = 10
        self._PropulsionTotalForce = 20
        self._PropulsionAngle = 25
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
    def getHorizontalForce(self):
        return self._PropulsionHorizontalDisplacement
    def setHorizontalForce(self):
        self._PropulsionHorizontalDisplacement = int(input("please input the amount of force making th object travel horizontally :"))
    def getVerticalForce(self):
        return self._PropulsionVerticalDisplacement
    def setVerticalForce(self):
        self._PropulsionVerticalDisplacement = int(input("Please input the amount of force in Newtons making the object travel vertically :"))
    def getTotalForce(self):
        return self._PropulsionTotalDisplacement
    def setTotalForce(self):
        self._PropulsionTotalDisplacement = int(input("Please input the Total Force Exerted on the object in Newtons :"))
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
        self._PropulsionTime = int(input("Please input how much time the object has been traveling for :"))
        print(self._PropulsionTime,'This is it')
    def setTimeSUVAT(self,T):
        self._PropulsionTime = T
    def RunTime(self,RunClock):
        while RunClock == True:
            Start = (time.clock())

        
        
        
    
    def GetSuvat(self):
        SUVATlist = []
        S = Propulsion.getDisplacement()
        U = Propulsion.getInitialVelocity()
        V = Propulsion.getFinalVelocity()
        A = Propulsion.getAcceleration()
        T = Propulsion.getTime()
        SUVATlist.append(S)
        SUVATlist.append(U)
        SUVATlist.append(V)
        SUVATlist.append(A)
        SUVATlist.append(T)
        return SUVATlist

    def CalculateInitialVelocity(self):
        # U = V-AT
        SUVATList = Propulsion.GetSuvat()
        SLocal = SUVATList[0]
        VLocal = SUVATList[2]
        ALocal = SUVATList[3]
        TLocal = SUVATList[4]
        U = (VLocal-(ALocal*TLocal))
        Propulsion.setInitialVelocitySUVAT(U)
        print(U,'calc1')

    def CalculateFinalVelocity(self):
        # V = U+AT
        SUVATList = Propulsion.GetSuvat()
        SLocal = SUVATList[0]
        ULocal = SUVATList[1]
        ALocal = SUVATList[3]
        TLocal = SUVATList[4]
        V = (ULocal+(ALocal*TLocal))
        Propulsion.setFinalVelocitySUVAT(V)
        print(V,'calc2')

    def CalculateAcceleration(self):
        #A = V-U/T
        SUVATList = Propulsion.GetSuvat()
        SLocal = SUVATList[0]
        ULocal = SUVATList[1]
        VLocal = SUVATList[2]
        TLocal = SUVATList[4]
        A = ((VLocal - ULocal)/TLocal)
        print(A,'calc3')
        Propulsion.setAccelerationSUVAT(A)
        
        
    def CalculateTime1(self):
        # T = V/A-U
        SUVATList = Propulsion.GetSuvat()
        SLocal = SUVATList[0]
        ULocal = SUVATList[1]
        ALocal = SUVATList[3]
        VLocal = SUVATList[2]
        T1 = (VLocal-ULocal)
        T2 = T1/ ALocal
        print(T2,'calc4')
        Propulsion.setTimeSUVAT(T2)
        

    def CalculateTime2(self):
        # S = UT
        # T = S/U
        SUVATList = Propulsion.GetSuvat()
        SLocal = SUVATList[0]
        ULocal = SUVATList[1]
        ALocal = SUVATList[3]
        VLocal = SUVATList[2]
        T = SLocal/ULocal
        print(T,'calc5')
        Propulsion.setTimeSUVAT(T)
        

    def CalculateTime3(self):
        # T = V/S
        SUVATList = Propulsion.GetSuvat()
        SLocal = SUVATList[0]
        ULocal = SUVATList[1]
        ALocal = SUVATList[3]
        VLocal = SUVATList[2]
        T = VLocal/SLocal
        print(T,'calc5')
        Propulsion.setTimeSUVAT(T)
        

    def CalculateDisplacement1(self):
        #S = UT+(AT^2)/2
        SUVATList = Propulsion.GetSuvat()
        TLocal = SUVATList[4]
        ULocal = SUVATList[1]
        ALocal = SUVATList[3]
        VLocal = SUVATList[2]
        TSquaredLocal = TLocal**2
        S = (ULocal*TLocal)+((ALocal*TSquaredLocal)/2)
        print(S,'calc6')
        Propulsion.setDisplacementSUVAT(S)
        

    def CalculateDisplacement2(self):
        #S = VT - AT^2/2
        SUVATList = Propulsion.GetSuvat()
        TLocal = SUVATList[4]
        ULocal = SUVATList[1]
        ALocal = SUVATList[3]
        VLocal = SUVATList[2] 
        TSquaredLocal = TLocal**2
        S = (VLocal*TLocal)-((ALocal*TSquaredLocal)/2)
        print(S,'calc7')
        Propulsion.setDisplacementSUVAT(S)
        

    def CalculateDisplacement3(self):
        #S = UT
        SUVATList = Propulsion.GetSuvat()
        TLocal = SUVATList[4]
        ULocal = SUVATList[1]
        ALocal = SUVATList[3]
        VLocal = SUVATList[2]
        S = ULocal*TLocal
        print(S,'calc8')
        Propulsion.setDisplacementSUVAT(S)
        
        
    def CalculateDisplacement4(self):
        #S=V/T
        SUVATList = Propulsion.GetSuvat()
        TLocal = SUVATList[4]
        ULocal = SUVATList[1]
        ALocal = SUVATList[3]
        VLocal = SUVATList[2]
        S = VLocal*TLocal
        print(S,'calc9')
        Propulsion.setDisplacementSUVAT(S)
        
    def calculateVerticalVectors(self):
        self.getVerticalDisplacement() 


    def EquationPriorityDisplacement(self,VariablesSelected,SUVATItemList):
        DisplacementValid = False
        SUVATList = Propulsion.GetSuvat()
        TLocal = SUVATList[4]
        ULocal = SUVATList[1]
        ALocal = SUVATList[3]
        VLocal = SUVATList[2] 
        SLocal = SUVATList[0]
        while DisplacementValid == False:
            for each in VariablesSelected:
                if each == 1 and each == 5:
                    if TLocal > 0 and SLocal > 0:
                        print('equation has entered validation')
                        Propulsion.setDisplacementSUVAT(0)
                        for each in VariablesSelected:
                            if each == 2:
                                print('ref3')
                                Propulsion.CalculateDisplacement3()
                                print('you have used U')
                            else:
                                Propulsion.setDisplacementSUVAT(0)
                                DisplacementValid = True
                elif each == 5 and TLocal == 0:
                    print('ref2')
                    Propulsion.setDisplacementSUVAT(0)
                elif each == 5 and TLocal > 0:
                    if each == 2:
                        print('ref1')
                        Propulsion.CalculateDisplacement3()
                    else:
                        Propulsion.CalculateDisplacement4()
                        DisplacementValid = True
                elif each == 5 and SLocal == 0:
                    Propulsion.setTimeSUVAT(0)
                elif each == 5 and SLocal > 0:
                    if each == 2:
                        Propulsion.CalculateTime2()
                    else:
                        Propulsion.CalculateTime3()
    
 
            

    def SUVATInput(self):
        #Set all SUVAT
        VariablesSelected = []  
        SUVATItemList = []
        count = 0
        VariableSelect = 0
        while count != 4:
            VariableSelect = int(input('Please select a SUVAT item to use!'))
            if VariableSelect == 1:
                    if VariableSelect == 1 and 'Displacement' not in SUVATItemList:
                        Propulsion.setDisplacement()
                        VariablesSelected.append(1)
                        SUVATItemList.append('Displacement')
                        count +=1
                    else:
                        print(' You have already set Displacement')
            elif VariableSelect == 2:
                if VariableSelect == 2 and 'Initial Velocity' not in SUVATItemList:
                    Propulsion.setInitialVelocity()
                    VariablesSelected.append(2)
                    SUVATItemList.append('Initial Velocity')
                    count += 1
                else:
                    print(' You have already set Initial Velocity')
            elif VariableSelect == 3:
                if VariableSelect == 3 and 'Final Velocity' not in SUVATItemList:
                    Propulsion.setFinalVelocity()
                    VariablesSelected.append(3)
                    SUVATItemList.append('Final Velocity')
                    count += 1
                else:
                    print(' You have already set Final Velocity')
            elif VariableSelect == 4:
                if VariableSelect == 4 and 'Acceleration' not in SUVATItemList:
                    Propulsion.setAcceleration()
                    VariablesSelected.append(4)
                    SUVATItemList.append('Acceleration')
                    count += 1
                else:
                    print(' You have already set Acceleration')
            elif VariableSelect == 5:
                if VariableSelect == 5 and 'Time' not in SUVATItemList:
                    Propulsion.setTime()
                    VariablesSelected.append(5)
                    SUVATItemList.append('Time')
                    count += 1
                else:
                    print(' You have already set Time')
        if VariableSelect == 6:
            self.SetGravity()
        print(SUVATItemList,'\n')
        return VariablesSelected,SUVATItemList
    
    def PrintSUVAT(self):
        #Get all SUVAT
        print('\n',Propulsion.GetSuvat(),'\n')
                
    def CompleteSUVATInputs(self):
        VariablesSelected,SUVATItemList = Propulsion.SUVATInput()
        Propulsion.PrepareSimulation(VariablesSelected,SUVATItemList)
        Propulsion.PrintSUVAT()

    def PrepareSimulation(self,VariablesSelected,SUVATItemList):
        Propulsion.PrintSUVAT()
        print(VariablesSelected)
        Displacement = False
        InitialVelocity = False
        FinalVelocity = False
        Acceleration = False
        Time = False
        for each in VariablesSelected:
            if each == 1:
                Displacement = True
            if each == 2:
                InitialVelocity = True
            if each == 3:
                FinalVelocity = True
            if each == 4:
                Acceleration = True
            if each == 5:
                Time = True
        if Displacement == True and Time == True:
            Propulsion.EquationPriorityDisplacement(VariablesSelected,SUVATItemList)
        if Displacement == False:
            Propulsion.EquationPriorityDisplacement(VariablesSelected,SUVATItemList)
        elif InitialVelocity == False:
            Propulsion.CalculateInitialVelocity()
        elif FinalVelocity == False:
            Propulsion.CalculateFinalVelocity()
        elif Acceleration == False:
            Propulsion.CalculateAcceleration()
        elif Time == False:
            Propulsion.CalculateTime1()

    def StartSimulation(self):
        RunSimulation = int(input('Please input 1 to run simulation'))
        if RunSimulation == True:        
            Start = self.RunTime(True)
            while RunSimulation == True:
                Propulsion.calculateVerticalVectors()
                Propulsion.CalculateHorizontalVectors()
            
                    
            



        
        
    
        
        
    
    def Propulsionmain(self):
        Propulsion.CompleteSUVATInputs()
        Propulsion.StartSimulation()

        
if __name__ == "__main__":
    Propulsion = Propulsion("",0,0,0,0,0,0,0,0,0,-9.81)
    Projectile = Projectile("",0,0)
    Propulsion.Propulsionmain()
    
    
    
   
                                               
