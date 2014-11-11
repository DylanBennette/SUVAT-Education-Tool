from A2_Physics_TestQuestions_Controller import *
import sys

class TestQuestionsTestingClass(TestQuestions_Controller):
    """ tests add Attempt"""
    def __init__(self):
        super().__init__()
        self.TestQuestions_Controller = TestQuestions_Controller()

    def TestQuestions_BasicInputs(self):
        TestQuestions_ID = input('please enter a Test Question ID')
        return TestQuestions_ID

    def TestQuestions_Inputs(self):
        Questions_ID = input('please enter your Question ID here')
        Test_ID = input('please enter your Test ID here')
        return Questions_ID,Test_ID
    
    def TestQuestions_UpdateInputs(self):
        TestQuestions_ID = input('please enter your Test Question ID here')
        Questions_ID = input('please enter your Question ID here')
        Test_ID = input('please enter your Test ID here')
        return TestQuestions_ID,Questions_ID,Test_ID
    
    def Add_TestQuestionsCreator(self,Questions_ID,Test_ID):
        try:
            self.TestQuestions_Controller.Add_TestQuestions(Questions_ID)
            print('\nYour changes have been made \n')
        except:
            print('Your query does not work')

    def Delete_TestQuestionsCreator(self,TestQuestions_ID):
        try:
            self.TestQuestions_Controller.Delete_TestQuestions(TestQuestions_ID)
            print('\nYour changes have been made \n')
        except:
            print('Your query does not work')

    def UpdateTestQuestionsCreator(self,TestQuestions_ID,Questions_ID,Test_ID):
        try:
            self.TestQuestions_Controller.Update_TestQuestions(TestQuestions_ID,Questions_ID,Test_ID)
            print('\nYour changes have been made \n')
        except:
            print('Your query does not work')

    def SearchTestQuestionsCreator(self,TestQuestions_ID):
        try:
            self.TestQuestions_Controller.Search_TestQuestions(TestQuestions_ID)
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
                Questions_ID,Test_ID = TestQuestionsTestingClass.TestQuestions_Inputs()
                TestQuestionsTestingClass.Add_TestQuestionsCreator(Questions_ID)
            elif choice == 2:
                TestQuestions_ID = TestQuestionsTestingClass.TestQuestions_BasicInputs()
                TestQuestionsTestingClass.Delete_TestQuestionsCreator(TestQuestions_ID)               
            elif choice == 3:
                TestQuestions_ID = TestQuestionsTestingClass.TestQuestions_BasicInputs()
                TestQuestionsTestingClass.SearchTestQuestionsCreator(TestQuestions_ID)
                TestQuestions_ID,Questions_ID,Test_ID = TestQuestionsTestingClass.TestQuestions_UpdateInputs()
                TestQuestionsTestingClass.UpdateTestQuestionsCreator(TestQuestions_ID,Questions_ID,Test_ID)
            elif choice == 4:
                TestQuestions_ID = TestQuestionsTestingClass.TestQuestions_BasicInputs()
                TestQuestionsTestingClass.SearchTestQuestionsCreator(TestQuestions_ID)
               

TestQuestionsTestingClass = TestQuestionsTestingClass()
TestQuestionsTestingClass.menuchoice()
    

    
    
