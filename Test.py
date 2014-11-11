from A2_Physics_Attempt_Controller import *
from A2_Physics_Response_Controller import *
from A2_Physics_Test_Controller import *
from A2_Physics_Answers_Controller import *
from A2_Physics_Questions_Controller import *
from A2_Physics_Controller import *

class StudentTest(A2_Physics_Controller):
	"""This Object creates the StudentTests"""
        def __init__(self,Question_ID,Test_ID,Attemps_ID,Response_ID,Question,Type_ID,Answers_ID,Correct_Answer,Test_Name):
		super().__init__()
		#Entity List [Response,Attempt,Questions,Answers,Test]
		#Items from Response entity
		self._Question_ID = None
		self._Test_ID = None
		self._Attempts_ID = None
		self._Response_ID = None
		#Items from Question Entity
		self._Question = ''
		self._Type_ID = None
		#Items from Answers Entity
		self._Answers_ID = None
		self._Correct_Answer = ''
		#Other items that are needed as utilities 
		self._Test_Name = ''

        def GetAttemptID(self,Attempts_ID):
                return self._Attempts_ID

        def SetAttemptID(self,Attempts_ID):
                LocalAttempts_ID = self._Attempts_ID
                if LocalAttempts_ID == None:
                        sql = """ Select max(Attempt_ID)
                                  from Attempts"""
                        results = self._select_query(sql)
                        if results ==[]:
                                print('I dont know how this did not work!!')
                        else:
                                newresults = results[:2]
                                print(results[-1])
                                self._Attempts_ID = results[-1]

	def GetTestName():
		pass

StudentTest = StudentTest(None,None,None,None,'',None,None,'','')
StudentTest.SetAttemptID(None)
		
