from A2_Physics_Propulsion_redone import *
from A2_Physics_TestingClass import *
from A2_Physics_DatabaseEditor import *
import Base

def MainMenuDisplay():
    print('\n1.Physics Simulation\n2.Test\n3.DataBaseEditor\n')
          
def MainMenu():
    MainMenuSelectionValid = False
    MainMenuSelection = 0
    ExitValidation = False
    while MainMenuSelectionValid != True:
          MainMenuSelection = int(input('Please enter the number of what you want to do?\n'))
          print('2')
          if MainMenuSelection == 1:
              Propulsion.Propulsion = Propulsion("",0,0,0,0,45,0,0,0,0,-9.81)
              Projectile1 = Projectile("",1,0)
              Propulsion.Propulsion.Propulsionmain()
          if MainMenuSelection == 2:
              StudentTest.StudentTest =StudentTest("",0,[],[])
              StudentTest.StudentTest.menuchoice()
          if MainMenuSelection == 3:
              DataBaseEditor = DataBaseEditor()
              DataBaseEditor.DataBaseEditormain()
          if MainMenuSelection == 4:
              ExitValidation = input('\nAre you sure you would like to quit input Y to end:\n')
              if ExitValidation == 'Y':
                  sys.exit(0)



def CLIMain():
    MainMenu()
        
if __name__ == "__main__":
    CLIMain() 
    
