from A2_Physics_Attempts_Controller import *
import sys

class AttemptTestingClass(Attempts_Controller):
    """ Attemptss add Attempt"""
    def __init__(self):
        super().__init__()
        self.Attempts_Controller = Attempts_Controller()

    def Attempts_BasicInputs(self):
        Attempts_ID = input('please enter a Attempts ID')
        return Attempts_ID

    def Attempts_Inputs(self):
        Attempts_Score = input('Please enter a Attempts Score')
        Time_in_session = input('please enter your Time in session here')
        Date_of_Use = input('please enter your Date_of_Use here')
        Test_ID = input('please enter your Test_ID here')
        Student_ID = input('please enter your Student_ID here')
        return Attempts_Score,Time_in_session,Date_of_Use,Test_ID,Student_ID
    
    def Attempts_UpdateInputs(self):
        Attempts_ID = input('please enter your Attempts ID here')
        Attempts_Score = input('please enter your Attempts Score here')
        Time_in_session = input('please enter your time in session here')
        Date_of_Use = input('please enter your Date_of_Use here')
        Test_ID = input('please enter your Test_ID here')
        Student_ID = input('please enter your Student_ID here')
        return Attempts_ID,Attempts_Score,Time_in_session,Date_of_Use,Test_ID,Student_ID
    
    def Add_AttemptsCreator(self,Attempts_Score,Time_in_session,Date_of_Use,Test_ID,Student_ID):
        #try to create new Attempts
        try:
            self.Attempts_Controller.Add_Attempts(Attempts_Score,Time_in_session,Date_of_Use,Test_ID,Student_ID)
            print('\nYour changes have been made\n')
        except:
            print('Sorry that did not work')

    def Delete_AttemptsCreator(self,Attempt_ID):
        self.Attempts_Controller.Delete_Attempts(Attempt_ID)
        #Try to delete a Attempts
        try:
            self.Attempts_Controller.Delete_Attempts(Attempt_ID)
            print('\nYour changes have been made\n')
        except:
            print('Sorry that did not work')

    def Update_AttemptsCreator(self,Attempt_ID,Attempts_Score,Time_in_session,Date_of_Use,Test_ID,Student_ID):
        #try to update a Attempts
        try:
            self.Attempts_Controller.Update_Attempts(Attempt_ID,Attempts_Score,Time_in_session,Date_of_Use,Test_ID,Student_ID)
            print('\nYour changes have been made\n')
        except:
            print('Sorry that did not work')

    def Search_AttemptsCreator(self,Attempt_ID):
        #try to search a Attempts
        try:
            self.Attempts_Controller.Search_Attempts(Attempt_ID)
            print('\nYour changes have been made\n')
        except:
            print('Sorry that did not work')
        
    def displaychanges(self):
        print('1. ADD')
        print('2. DELETE')
        print('3. UPDATE')
        print('4. SEARCH\n')

    def menuchoice(self):
        self.displaychanges()
        choice = None
        while choice != -1:
            choice = int(input('please enter an option'))
            if choice == 1:
                Attempts_Score,Time_in_session,Date_of_Use,Test_ID,Student_ID = AttemptTestingClass.Attempts_Inputs()
                AttemptTestingClass.Add_AttemptsCreator(Attempts_Score,Time_in_session,Date_of_Use,Test_ID,Student_ID)
            elif choice == 2:
                Attempt_ID = AttemptTestingClass.Attempts_BasicInputs()
                AttemptTestingClass.Delete_AttemptsCreator(Attempt_ID)
            elif choice == 3:
                Attempt_ID,Attempts_Score,Time_in_session,Date_of_Use,Test_ID,Student_ID = AttemptTestingClass.Attempts_BasicInputs()
                AttemptTestingClass.Search_AttemptsCreator(Attempts_ID)
                Attempts_ID,Attempts_Score = AttemptTestingClass.Attempts_UpdateInputs()
                AttemptTestingClass.Update_AttemptsCreator(Attempt_ID,Attempts_Score,Time_in_session,Date_of_Use,Test_ID,Student_ID)
            elif choice == 4:
                Attempt_ID = AttemptTestingClass.Attempts_BasicInputs()
                AttemptTestingClass.Search_AttemptsCreator(Attempt_ID)
                
AttemptTestingClass = AttemptTestingClass()
AttemptTestingClass.menuchoice()
    

    
    
