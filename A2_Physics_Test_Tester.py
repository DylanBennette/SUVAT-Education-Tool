from A2_Physics_Test_Controller import *
import sys

class TestTestingClass(Test_Controller):
    """ tests add Attempt"""
    def __init__(self):
        super().__init__()
        self.Test_Controller = Test_Controller()

    def Test_BasicInputs(self):
        Test_ID = input('please enter a Test ID')
        return Test_ID

    def Test_Inputs(self):
        Test_Name = input('Please enter a Test Name')
        return Test_Name
    
    def Test_UpdateInputs(self):
        Test_ID = input('please enter your Test ID here')
        Test_Name = input('please enter your Test Name here')
        return Test_ID,Test_Name
    
    def Add_TestCreator(self,Test_Name):
        #try to create new Test
        try:
            self.Test_Controller.Add_Test(Test_Name)
        except:
            print('Sorry that did not work')

    def Delete_TestCreator(self,Test_ID):
        #Try to delete a Test
        try:
            self.Test_Controller.Delete_Test(Test_ID)
        except:
            print('Sorry that did not work')

    def Update_TestCreator(self,Test_ID,Test_Name):
        #try to update a Test
        try:
            self.Test_Controller.Update_Test(Test_ID,Test_Name)
        except:
            print('Sorry that did not work')

    def Search_TestCreator(self,Test_ID):
        #try to search a Test
       # try:
            self.Test_Controller.Return_Tests(Test_ID)
      #  except:
            print('Sorry that did not work')
        
    def displaychanges(self):
        print('1. ADD')
        print('2. DELETE')
        print('3. UPDATE')
        print('4. SEARCH')
        print('5. search by any item\n')

    def SearchFortest(self,SearchItem):
        print('entered the search')
        Search = SearchItem
        IntegerSearch = False
        test = Test_Controller()
        Tests = test.Return_TestsNoInput()
        ItemFound = False
        row = 0 
        column = 0
        MaxItems = len(Tests)
        for i in range(0,2):
            for each in Tests:
                Item = Tests[row][column]
                if Item == Search:
                    ItemFound = True
                if row <= MaxItems:
                    row += 1
                if row == MaxItems:
                    column += 1
                    row = 0
        if ItemFound == True:      
            print(ItemFound)
        if ItemFound == True:
            if type(Search) == int:
                print('Integer')
                IntegerSearch = True
                Test_ID = Search
                results = test.Return_TestsbyID(Test_ID)
                return results
            else:
                print('String')
                Test_Name = Search
                results= test.Return_TestsbyName(Test_Name)
                return results
        else:
            print('Hah it did not work')
            
    def menuchoice(self):
        self.displaychanges()
        choice = None
        while choice != -1:
            choice = int(input('please enter an option'))
            if choice == 1:
                Test_Name = TestTestingClass.Test_Inputs()
                TestTestingClass.Add_TestCreator(Test_Name)
            elif choice == 2:
                Test_ID = TestTestingClass.Test_BasicInputs()
                TestTestingClass.Delete_TestCreator(Test_ID)
            elif choice == 3:
                Test_ID = TestTestingClass.Test_BasicInputs()
                TestTestingClass.Search_TestCreator(Test_ID)
                Test_ID,Test_Name = TestTestingClass.Test_UpdateInputs()
                TestTestingClass.Update_TestCreator(Test_ID,Test_Name)
            elif choice == 4:
                Test_ID = TestTestingClass.Test_BasicInputs()
                TestTestingClass.Search_TestCreator(Test_ID)
            elif choice == 5:
                self.SearchFortest()
                

    
    
