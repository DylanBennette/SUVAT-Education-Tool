from A2_Physics_Response_Controller import *
import sys

class ResponseTestingClass(Response_Controller):
    """ Attemptss add Attempt"""
    def __init__(self):
        super().__init__()
        self.Response_Controller = Response_Controller()

    def Response_BasicInputs(self):
        Response_ID = input('please enter a Response ID')
        return Response_ID

    def Response_Inputs(self):
        Student_Response = input('Please enter a Student Response')
        Attempt_ID = input('please enter your Attempt ID here')
        Questions_ID = input('please enter your Questions ID here')
        return Student_Response,Attempt_ID,Questions_ID
    
    def Response_UpdateInputs(self):
        Attempts_ID = input('please enter your Attempts ID here')
        Student_Response = input('please enter your Student Response here')
        Response_ID = input('please enter your Response ID here')
        Questions_ID = input('please enter your Questions ID here')
        return Attempts_ID,Student_Response,Response_ID,Questions_ID
    
    def Add_ResponseCreator(self,Student_Response,Attempt_ID,Questions_ID):
        #try to create new Attempts
        try:
            self.Response_Controller.Add_Response(Student_Response,Attempt_ID,Questions_ID)
            print('\nYour changes have been made\n')
        except:
            print('Sorry that did not work')

    def Delete_ResponseCreator(self,Response_ID):
        self.Response_Controller.Delete_Response(Response_ID)
        #Try to delete a Attempts
        try:
            self.Response_Controller.Delete_Response(Response_ID)
            print('\nYour changes have been made\n')
        except:
            print('Sorry that did not work')

    def Update_ResponseCreator(self,Attempt_ID,Student_Response,Response_ID,Questions_ID):
        self.Response_Controller.Update_Response(Attempt_ID,Student_Response,Response_ID,Questions_ID)
        #try to update a Attempts
        try:
            self.Response_Controller.Update_Response(Attempt_ID,Student_Response,Response_ID,Questions_ID)
            print('\nYour changes have been made\n')
        except:
            print('Sorry that did not work')

    def Search_ResponseCreator(self,Response_ID):
        #try to search a Attempts
        try:
            self.Response_Controller.Search_Response(Response_ID)
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
                Student_Response,Attempt_ID,Questions_ID = ResponseTestingClass.Response_Inputs()
                ResponseTestingClass.Add_ResponseCreator(Student_Response,Attempt_ID,Questions_ID)
            elif choice == 2:
                Response_ID = ResponseTestingClass.Response_BasicInputs()
                ResponseTestingClass.Delete_ResponseCreator(Response_ID)
            elif choice == 3:
                Response_ID = ResponseTestingClass.Response_BasicInputs()
                ResponseTestingClass.Search_ResponseCreator(Response_ID)
                Attempt_ID,Student_Response,Response_ID,Questions_ID = ResponseTestingClass.Response_UpdateInputs()
                ResponseTestingClass.Update_ResponseCreator(Attempt_ID,Student_Response,Response_ID,Questions_ID)
            elif choice == 4:
                Response_ID = ResponseTestingClass.Response_BasicInputs()
                ResponseTestingClass.Search_ResponseCreator(Response_ID)
                
ResponseTestingClass = ResponseTestingClass()
ResponseTestingClass.menuchoice()
    

    
    
