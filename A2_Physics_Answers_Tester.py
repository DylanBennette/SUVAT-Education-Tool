from A2_Physics_Answers_Controller import *
import sys

class AnswersTestingClass(Answers_Controller):
    """ tests add Attempt"""
    def __init__(self):
        super().__init__()
        self.Answers_Controller = Answers_Controller()

    def Answers_UpdateInputs(self):
        Questions_ID = input('Please enter the Questions ID')
        Correct_Answer = input('Please enter the Correct Answer')
        Answers_ID = input('Please enter the Answers ID')
        return Questions_ID,Correct_Answer,Answers_ID

    def Answers_Inputs(self):
        Questions_ID = input('Please enter the Questions_ID')
        Correct_Answer = input('Please enter the Correct Answer')
        return Questions_ID,Correct_Answer
    
    def Answers_BasicInputs(self):
        Answers_ID = input('Please enter the Answers ID')
        return Answers_ID
    
    def Add_AnswersCreator(self,Questions_ID,Correct_Answer):
        self.Answers_Controller.Add_Answer(Questions_ID,Correct_Answer)
        try:
            self.Answers_Controller.Add_Answer(Questions_ID,Correct_Answer)
            print('\nYour changes have been made \n')
        except:
            print('Your query does not work')

    def Delete_AnswersCreator(self,Answers_ID):
        self.Answers_Controller.Delete_Answer(Answers_ID)
        try:
            self.Answers_Controller.Delete_Answer(Answers_ID)
            print('\nYour changes have been made \n')
        except:
            print('Your query does not work')

    def Update_AnswersCreator(self,Correct_Answer,Questions_ID,Answers_ID):
            try:
                self.Answers_Controller.Update_Answer(Answers_ID,Correct_Answer,Questions_ID)
                print('\nYour changes have been made \n')
            except:
                print('Your query does not work')

    def Search_AnswersCreator(self,Answers_ID):
        try:
            self.Answers_Controller.Search_Answers(Answers_ID)
        except:
            print('Your query does not work')
    
    def displaychanges(self):
        print('1. ADD')
        print('2. DELETE')
        print('3. UPDATE')
        print('4. SEARCH\n')

    def menuchoice(self):
        self.displaychanges()
        choice = None
        while choice != -1:
            choice = int(input('please enter an option\n'))
            if choice == 1:
                Questions_ID,Correct_Answer = AnswersTestingClass.Answers_Inputs()
                AnswersTestingClass.Add_AnswersCreator(Questions_ID,Correct_Answer)
            elif choice == 2:
                Answers_ID = AnswersTestingClass.Answers_BasicInputs()
                AnswersTestingClass.Delete_AnswersCreator(Answers_ID)               
            elif choice == 3:
                Answers_ID = AnswersTestingClass.Answers_BasicInputs()
                AnswersTestingClass.Search_AnswersCreator(Answers_ID)
                Correct_Answer,Questions_ID,Answers_ID = AnswersTestingClass.Answers_UpdateInputs()
                AnswersTestingClass.Update_AnswersCreator(Correct_Answer,Questions_ID,Answers_ID)
            elif choice == 4:
                Answers_ID = AnswersTestingClass.Answers_BasicInputs()
                AnswersTestingClass.Search_AnswersCreator(Answers_ID)


AnswersTestingClass = AnswersTestingClass()
AnswersTestingClass.menuchoice()
    

    
    
