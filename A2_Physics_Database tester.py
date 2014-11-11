from A2_Physics_Student_Controller import *
import sys

class StudentTestingClass(Student_Controller):
    """ tests add student"""
    def __init__(self):
        super().__init__()
        self.Student_Controller = Student_Controller()
        
    def Student_Inputs(self):
        FirstName = input('please enter your first name here')
        LastName = input('please enter your last name here')
        return FirstName,LastName
        
    def Add_StudentCreator(self,FirstName,LastName):
        #try to create new sudent with these value
        try:
            self.Student_Controller.Add_Student(FirstName,LastName)
        except:
            print('your Quer does not work')
    
StudentTestingClass = StudentTestingClass()
FirstName,LastName = StudentTestingClass.Student_Inputs()
StudentTestingClass.Add_StudentCreator(FirstName,LastName)

