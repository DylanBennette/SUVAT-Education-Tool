from A2_Physics_Student_Controller import *
import sys

class StudentTestingClass(Student_Controller):
    """ tests add student"""
    def __init__(self):
        super().__init__()
        self.Student_Controller = Student_Controller()
        

    def Student_BasicInputs(self):
        Student_ID = input('please enter a student ID')
        return Student_ID
    
    def Student_Inputs(self):
        FirstName = input('please enter your first name here')
        LastName = input('please enter your last name here')
        return FirstName,LastName

    def Student_UpdateInputs(self):
        FirstName = input('please enter your first name here')
        LastName = input('please enter your last name here')
        Student_ID = input('please enter a student ID')
        return FirstName,LastName,Student_ID

        
    def Add_StudentCreator(self,FirstName,LastName):
        #try to create new sudent with these value
        try:
            self.Student_Controller.Add_Student(FirstName,LastName)
        except:
            print('Sorry that did not work')

    def Update_StudentCreator(self,Student_ID,FirstName,LastName):
        # try to update an existing Students details
        try:
            self.Student_Controller.Update_Student(Student_ID,FirstName,LastName)
        except:
            print('Sorry that did not work')

    def Search_StudentCreator(self,Student_ID):
        #try to search for an existing student
        try:
            self.Student_Controller.Search_Student(Student_ID)
        except:
            print('Sorry that did not work')

    def Delete_StudentCreator(self,Student_ID):
        #try to search
        try:
            self.Student_Controller.Delete_Student(Student_ID)
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
                FirstName,LastName = StudentTestingClass.Student_Inputs()
                StudentTestingClass.Add_StudentCreator(FirstName,LastName)
            elif choice == 2:
                Student_ID = StudentTestingClass.Student_BasicInputs()
                StudentTestingClass.Delete_StudentCreator(Student_ID)
            elif choice == 3:
                Student_ID = StudentTestingClass.Student_BasicInputs()
                StudentTestingClass.Search_StudentCreator(Student_ID)
                Student_ID,FirstName,LastName = StudentTestingClass.Student_UpdateInputs()
                StudentTestingClass.Update_StudentCreator(Student_ID,FirstName,LastName)
            elif choice == 4:
                Student_ID = StudentTestingClass.Student_BasicInputs()
                StudentTestingClass.Search_StudentCreator(Student_ID)
                
                
StudentTestingClass = StudentTestingClass()
StudentTestingClass.menuchoice()
