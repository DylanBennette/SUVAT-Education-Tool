from A2_Physics_Questions_Controller import *
import sys

class QuestionsTestingClass(Questions_Controller):
    """ tests add Attempt"""
    def __init__(self):
        super().__init__()
        self.Questions_Controller = Questions_Controller()

    def Questions_UpdateInputs(self):
        Question = input('Please enter the Question')
        Type_ID = input('Please enter the Type ID')
        Questions_ID = input('Please enter the Questions ID')
        return Question,Type_ID,Questions_ID

    def Questions_Inputs(self):
        Question = input('Please enter the Question')
        Type_ID = input('Please enter the Type ID')
        return Question,Type_ID
    
    def Questions_BasicInputs(self):
        Questions_ID = input('Please enter the Question ID')
        return Questions_ID
    
    def Add_QuestionsCreator(self,Question,Type_ID):
        try:
            self.Questions_Controller.Add_Question(Question,Type_ID)
            print('\nYour changes have been made \n')
        except:
            print('Your query does not work')

    def Delete_QuestionsCreator(self,Questions_ID):
        try:
            self.Questions_Controller.Delete_Question(Questions_ID)
            print('\nYour changes have been made \n')
        except:
            print('Your query does not work')

    def Update_QuestionsCreator(self,Type_ID,Question,Questions_ID):
            self.Questions_Controller.Update_Question(Questions_ID,Type_ID,Question)
            try:
                self.Questions_Controller.Update_Question(Questions_ID,Type_ID,Question)
                print('\nYour changes have been made \n')
            except:
                print('Your query does not work')

    def Search_QuestionsCreator(self,Questions_ID):
        try:
            self.Questions_Controller.Search_Questions(Questions_ID)
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
                Question,Type_ID = QuestionsTestingClass.Questions_Inputs()
                QuestionsTestingClass.Add_QuestionsCreator(Question,Type_ID)
            elif choice == 2:
                Questions_ID = QuestionsTestingClass.Questions_BasicInputs()
                QuestionsTestingClass.Delete_QuestionsCreator(Questions_ID)               
            elif choice == 3:
                Questions_ID = QuestionsTestingClass.Questions_BasicInputs()
                QuestionsTestingClass.Search_QuestionsCreator(Questions_ID)
                Type_ID,Question,Questions_ID = QuestionsTestingClass.Questions_UpdateInputs()
                QuestionsTestingClass.Update_QuestionsCreator(Type_ID,Question,Questions_ID)
            elif choice == 4:
                Questions_ID = QuestionsTestingClass.Questions_BasicInputs()
                QuestionsTestingClass.Search_QuestionsCreator(Questions_ID)


QuestionsTestingClass = QuestionsTestingClass()
QuestionsTestingClass.menuchoice()
    

    
    
