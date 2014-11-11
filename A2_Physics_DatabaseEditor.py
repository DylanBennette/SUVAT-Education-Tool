from A2_Physics_Type_Tester import *
from A2_Physics_TestQuestions_Tester import *
from A2_Physics_Test_Tester import *
from A2_Physics_Student_Tester import *
from A2_Physics_Response_Tester import *
from A2_Physics_Questions_Tester import *
from A2_Physics_Attempt_Tester import *
from A2_Physics_Answers_Tester import *

def DatabaseEditorMain(self):
	SelectionValid = False 
	while SelectionValid != True:
		selection = int(input("Please enter a selection here!"))
		if selection == 1:
			EditType_Tester()
		elif selection == 2:
			EditTest_Tester()
		elif selection == 3:
			EditStudent_Tester()
		elif selection == 4:
			EditResponse_Tester()
		elif selection == 5:
			EditQuestions_Tester()
		elif selection == 6:
			EditAttempts_Tester()
		elif selection == 7:
			EditAnswers_Tester()

def EditType_Tester(self):
	TypeTestingClass = TypeTestingClass()
	TypeTestingClass.menuchoice()

def EditTest_Tester(self):
	TestTestingClass = TestTestingClass()
	TestTestingClass.menuchoice()

def EditStudent_Tester(self):
	StudentTestingClass = StudentsTestingClass()
	StudentTestingClass.menuchoice()

def EditResponse_Tester(self):
	ResponseTestingClass = ResponseTestingClass()
	ResponseTestingClass.menuchoice()

def EditQuestions_Tester(self):
	QuestionsTestingClass = QuestionsTestingClass()
	QuestionsTestingClass.menuchoice()

def EditAttempts_Tester(self):
	AttemptsTestingClass = AttemptssTestingClass()
	AttemptsTestingClass.menuchoice()

def EditAnswers_Tester(self):
	AnswersTestingClass = AnswersTestingClass()
	AnswersTestingClass.menuchoice()
