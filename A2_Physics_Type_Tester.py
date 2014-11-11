from A2_Physics_Type_Controller import *
import sys

class TypeTestingClass(Type_Controller):
    """ tests add Attempt"""
    def __init__(self):
        super().__init__()
        self.Type_Controller = Type_Controller()

    def Type_BasicInputs(self):
        Type_ID = input('please enter a Type ID')
        return Type_ID

    def Type_Inputs(self):
        Question_Type = input('please enter your Question Type here')
        return Question_Type
    
    def Type_UpdateInputs(self):
        Type_ID = input('please enter your Type ID here')
        Question_Type = input('please enter your Question Type here')
        return Type_ID,Question_Type
    
    def Add_TypeCreator(self,Question_Type):
        try:
            self.Type_Controller.Add_Type(Question_Type)
            print('\nYour changes have been made \n')
        except:
            print('Your query does not work')

    def Delete_TypeCreator(self,Type_ID):
        try:
            self.Type_Controller.Delete_Type(Type_ID)
            print('\nYour changes have been made \n')
        except:
            print('Your query does not work')

    def Update_TypeCreator(self,Type_ID,Question_Type):
        try:
            self.Type_Controller.Update_Type(Type_ID,Question_Type)
            print('\nYour changes have been made \n')
        except:
            print('Your query does not work')

    def Search_TypeCreator(self,Type_ID):
        try:
            self.Type_Controller.Search_Type(Type_ID)
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
                Question_Type = TypeTestingClass.Type_Inputs()
                TypeTestingClass.Add_TypeCreator(Question_Type)
            elif choice == 2:
                Type_ID = TypeTestingClass.Type_BasicInputs()
                TypeTestingClass.Delete_TypeCreator(Type_ID)               
            elif choice == 3:
                Type_ID = TypeTestingClass.Type_BasicInputs()
                TypeTestingClass.Search_TypeCreator(Type_ID)
                Type_ID,Question_Type = TypeTestingClass.Type_UpdateInputs()
                TypeTestingClass.Update_TypeCreator(Type_ID,Question_Type)
            elif choice == 4:
                Type_ID = TypeTestingClass.Type_BasicInputs()
                TypeTestingClass.Search_TypeCreator(Type_ID)
               

TypeTestingClass = TypeTestingClass()
TypeTestingClass.menuchoice()
    

    
    
