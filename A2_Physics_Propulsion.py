import math                                                              
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
    def setInitialVelocitySUVAT(self,U):
        self._PropulsionInitalVelocity = U
    def getFinalVelocity(self):
        return self._PropulsionFinalVelocity
    def setFinalVelocity(self):
        self._PropulsionFinalVelocity = int(input("Please input the Final Velocity when Time is at its maximum :"))
    def setFinalVelocitySUVAT(self,V):
        self._PropulsionFinalVelocity = V
    def getAcceleration(self):
        return self._PropulsionAcceleration
    def setAcceleration(self):
        self._PropulsionAcceleration = int(input("please input the value for the acceleration of the object :"))
    def setAccelerationSUVAT(self,A):
        self._PropulsionAcceleration = A
    def getDisplacement(self):
        return self._PropulsionDisplacement
    def setDisplacement(self):
        self._PropulsionDisplacement = int(input("Please input the displacement of the objcet from it's point of origin :"))
    def setDisplacementSUVAT(self,S):
        self._PropulsionDisplacement = S 
    def getTime(self):
        return self._PropulsionTime
    def setTime(self):
        self._PropulsionTime = int(input("Please input how much time the object has been traveling for :"))
    def setTimeSUVAT(self,T):
        self._PropulsionTime = T
    
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
        print(U)
        Propulsion.setInitialVelocitySUVAT(U)
        print(Propulsion.getInitialVelocity())

    def CalculateFinalVelocity(self):
        # V = U+AT
        SUVATList = Propulsion.GetSuvat()
        SLocal = SUVATList[0]
        ULocal = SUVATList[1]
        ALocal = SUVATList[3]
        TLocal = SUVATList[4]
        V = (ULocal+(ALocal*TLocal))
        print(V)
        Propulsion.setFinalVelocitySUVAT(V)

    def CalculateAcceleration(self):
        #A = V-U/T
        SUVATList = Propulsion.GetSuvat()
        SLocal = SUVATList[0]
        ULocal = SUVATList[1]
        ALocal = SUVATList[3]
        TLocal = SUVATList[4]
        A = (ULocal+(ALocal*TLocal))
        print(A)
        Propulsion.setAccelerationSUVAT(A)
        

    def CalculateTime(self):
        # T = V/A-U
        SUVATList = Propulsion.GetSuvat()
        SLocal = SUVATList[0]
        ULocal = SUVATList[1]
        ALocal = SUVATList[3]
        VLocal = SUVATList[2]
        T = (VLocal/(ULocal-ALocal))
        print(T)
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
        print(S)
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
        print(S)
        Propulsion.setDisplacementSUVAT(S)

    def EquationPriorityDisplacement(self,VariablesSelected):
        InitialVelocity = False
        FinalVelocity = False
        SUVATItem1 = VariablesSelected[0]
        SUVATItem2 = VariablesSelected[1]
        SUVATItem3 = VariablesSelected[2]
        SUVATItem4 = VariablesSelected[3]
        if SUVATItem1 or SUVATItem2 or SUVATItem3 or SUVATItem4 == 2:
            InitialVelocity = True
        if SUVATItem1 or SUVATItem2 or SUVATItem3 or SUVATItem4 == 3:
            FinalVelocity = True
        if InitialVelocity and FinalVelocity == True:
            propulsion.CalculateDisplacement1()
        elif InitialVelocity == True and FinalVelocity == False:
            Propulsion.CalculateDisplacement1()
        elif initialVelocity == False and FinalVelocity == True:
            Propulsion.CalculateDisplacement2()


    def SUVATInput(self):
        #Set all SUVAT
        VariablesSelected = []
        count = 0
        VariableSelect = 0
        while count != 4:
            VariableSelect = int(input('Please select a Variable to input!'))
            if VariableSelect == 1:
                Propulsion.setDisplacement()
                VariablesSelected.append(1) 
            elif VariableSelect == 2:
                Propulsion.setInitialVelocity()
                VariablesSelected.append(2)
            elif VariableSelect == 3:
                Propulsion.setFinalVelocity()
                VariablesSelected.append(3)
            elif VariableSelect == 4:
                Propulsion.setAcceleration()
                VariablesSelected.append(4)
            elif VariableSelect == 5:
                Propulsion.setTime()
                VariablesSelected.append(5)
            count = count+1
        return VariablesSelected
        

    def PrintSUVAT(self):
        #Get all SUVAT
        print('\n',Propulsion.GetSuvat(),'\n')
        
    def ValidateSUVATVariables(self,VariablesSelected):
        Propulsion.PrintSUVAT()
        print(VariablesSelected)
        SUVATItem1 = VariablesSelected[0]
        SUVATItem2 = VariablesSelected[1]
        SUVATItem3 = VariablesSelected[2]
        SUVATItem4 = VariablesSelected[3]
        InputsApproved = True
        while InputsApproved == True:
            if SUVATItem1 == SUVATItem2 or SUVATItem1 == SUVATItem3 or SUVATItem1 == SUVATItem4 or SUVATItem2 == SUVATItem3 or SUVATItem2 == SUVATItem4 or SUVATItem3 == SUVATItem4:
                InputsApproved = False
                print('\nThis is an invalid combination of SUVAT Variables!')
        return InputsApproved
                
    def CompleteSUVATInputs(self):
        VariablesSelected = Propulsion.SUVATInput()
        InputsApproved = Propulsion.ValidateSUVATVariables(VariablesSelected)
        if InputsApproved == False:
            Propulsion.CompleteSUVATInputs()
        Propulsion.PrepareSimulation(VariablesSelected)

    def PrepareSimulation(self,VariablesSelected):
        Displacement = True
        InitialVelocity = True
        FinalVelocity = True
        Acceleration = True
        Time = True
        if SUVATItem1 or SUVATItem2 or SUVATItem3 or SUVATItem4 != 1:
            Displacement = False
            Propulsion.EquationPriorityDisplacement()
        if SUVATItem1 or SUVATItem2 or SUVATItem3 or SUVATItem4 != 2:
            InitialVelocity = False
            Propulsion.CalculateInitialVelocity()
        if SUVATItem1 or SUVATItem2 or SUVATItem3 or SUVATItem4 != 3:
            FinalVelocity = False
            Propulsion.CalculateFinalVelocity()
        if SUVATItem1 or SUVATItem2 or SUVATItem3 or SUVATItem4 != 4:
            Acceleration = False
            Propulsion.CalculateAcceleration()
        if SUVATItem1 or SUVATItem2 or SUVATItem3 or SUVATItem4 != 5:
            Time = False
            Propulsion.CalculateTime()
            
    def StartSimulation(self):
        Propulsion.CompleteSUVATInputs()

        
        
    
        
        
    
    def Propulsionmain(self):
        Propulsion = Propulsion("",10,10,20,25,25,0,15,20,0)

        
if __name__ == "__main__":
    Propulsion = Propulsion("",10,10,20,25,25,0,15,20,0)
    Propulsion.StartSimulation()
    Propulsion.CalculateInitialVelocity()
    Propulsion.CalculateFinalVelocity()
    Propulsion.CalculateTime()
    Propulsion.CalculateAcceleration()
    Propulsion.CalculateDisplacement1()
    Propulsion.CalculateDisplacement2()
    
    
   
                                               
