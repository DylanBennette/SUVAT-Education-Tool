from A2_Physics_Test_Controller import *
from A2_Physics_Answers_Controller import *
from A2_Physics_Attempts_Controller import *
from A2_Physics_TestQuestions_Controller import *
from A2_Physics_Questions_Controller  import *
from A2_Physics_Response_Controller import *
from PyQt4.QtGui import*
from PyQt4.QtGui import*
from PyQt4 import QtGui
import sys
import Base

class StudentTest(Test_Controller,Answers_Controller,TestQuestions_Controller,Attempts_Controller,Questions_Controller):
    def __init__(self,TestName,AttemptScore,Questions,Answers):
        self._TestName = ""
        self._AttemptScore = 0
        self._Questions = []
        self._Answers = []
        super().__init__()
        self.Test_Controller = Test_Controller()
        self.Attempts_Controller = Attempts_Controller()
        self.TestQuestions_Controller = TestQuestions_Controller()
        self.Answers_Controller = Answers_Controller()
        self.Questions_Controller = Questions_Controller()
        


    def getTests(self):
        test = Test_Controller()
        returned = test.QComboBox_Tests()
        return returned
    def getTestID(self,Test_Name):
        test = Test_Controller()
        returned = test.QComboBox_Retrieve_ID(Test_Name)
        return returned
    def getTestName(self):
        return self._TestName
    def setTestName(self):
        TestInfo = False
        while TestInfo != True:
            try:
                TestInput = input('Please enter the test you are after')
                results = self.Test_Controller.Return_Tests(TestInput)
                for each in results:
                    Test_ID = each[0]
                    ResultsSimplified = each[1]
                self._TestName = ResultsSimplified
                TestInfo = True
                return Test_ID
            except:
                print('That test does not exist or you cannot spell!')
        
    def RetrieveQuestionsID(self,Test_ID):
        QuestionsInfo = False
        QuestionIDList = []
        QuestionIDListValidated = []
        while QuestionsInfo != True:
          #  try:
                TestQuestions = TestQuestions_Controller()
                results = TestQuestions.Search_TestQuestionsSTUDENTTESTING(Test_ID)
                for i in range(len(results)):
                    for each in results:
                        Questions_ID = each[0]
                        QuestionIDList.append(Questions_ID)
                        i +=1
                        if i > 1:
                            if QuestionIDList[0] == QuestionIDList[1]:
                                QuestionIDList.pop()
                if not results:
                    print('This is not a valid test')
                else:
                     QuestionsInfo = True
                     return QuestionIDList
          #  except:
                print('That test does not exist or you cannot spell!')
                pass
            
    def RetrieveQuestions(self,QuestionIDList):
        QuestionsInfo = False
        while QuestionsInfo != True:
            try:
                for each in QuestionIDList:
                    QuestionsC = Questions_Controller()
                    results = QuestionsC.Search_QuestionsSTUDENTTEST(each)
                    for each in results:
                        Question = each[0]
                    if not results:
                       self.setTestName()
                    else:
                        QuestionsInfo = True
                return results
            except:
                print('That test does not exist or you cannot spell!')
                pass

    def RetrieveAnswers(self,QuestionIDList):
        QuestionsInfo = False
        CorrectAnswer = []
        while QuestionsInfo != True:
            try:
                for each in QuestionIDList:
                    A_C = Answers_Controller()
                    results = A_C.Search_AnswersSTUDENTTEST(each)
                    for i in range(len(results)):
                        for each in results:
                            Answer = each[0]
                            CorrectAnswer.append(Answer)
                            i +=1
                            if i > 1:
                                if CorrectAnswer[0] == CorrectAnswer[1]:
                                    CorrectAnswer.pop()
                    else:
                        QuestionsInfo = True
                return CorrectAnswer
            except:
                print('That test does not exist or you cannot spell!')
                self.setTestName()

    def getAttemptScore(self):
        return self._AttemptScore
    def getAnswers(self):
        return self._Answers
    def setAnswers(self,Questions):
        for each in self.getQuestions():
            try:
                CorrectResults = Answers_Controller.Search_Answers(Questions[0])
                print('\nYour changes have been made \n')
            except:
                print('Your query does not work')
        

    def getQuestions(self):
        return self._Questions
    def setQuestions(self):
        pass
    

    def AnswerQuestions(self):
        self.displaychanges()
        AnswerCounter = 1
        TestFinished = False
        while TestFinished != True:
            for each in self.getQuestions():
                AnswerInput = input('Please enter your answer here')
                self._Answers.append(AnswerInput)
                AnswerCounter += 1
                if AnswerCounter >= len(self.getQuestions()):
                    TestFinished = True

    def MarkQuestions(self,CorrectAnswer,QuestionIDList):
        Answered = False
        Answers = self.getAnswers()
        Score = 1
        TrueScore = 0
        MaxScore = len(self.getQuestions())
        while Answered != True:
            for each in CorrectAnswer:
                for i in range(MaxScore):
                    if each == (Answers[i]):
                        TrueScore += 1
                        Score +=1
                        print('Question',i+1,'. was correct')
                        Answered = True
                        i = 0
                    elif each != (Answers[i]):
                        print('Question',i+1,'. was wrong')
                        Answered = False
            if Answered == False:            
                Retry = 0
                Retry = input('would you like to retry enter 1 if you would like too!')
                if Retry == '1':
                    for each in self._Answers:
                        self._Answers.pop()
                        TrueScore = 0
                        Score = 1
                        Retry = 0
                        i = 0
                        self.Retry(QuestionIDList)
                else:
                    Answered = True
            if TrueScore == MaxScore:
                Answered = True
                print('You Scored',TrueScore,'out of a total of',MaxScore)
                
    def displaychanges(self):
        QNum = 1
        for each in self.getQuestions():
            print(QNum,'.',each)
            QNum += 1

##    def AddResponseTest(self,ResponseList):
##        ResponseController = Response_Controller()
##        for each in ResponseList:
##            Student_Response = ResponseList[each]
##            Attempt_ID =
##            Questions_ID
##            Response_Controller.AddResponse(Student_Response,Attempt_ID,Questions_ID)

    def Retry(self,QuestionIDList):
        self.AnswerQuestions()
        CorrectAnswer = self.RetrieveAnswers(QuestionIDList)
        self.MarkQuestions(CorrectAnswer,QuestionIDList)
    def menuchoice(self):
        Test_ID = self.setTestName()
        QuestionIDList = self.RetrieveQuestionsID(Test_ID)
        self.RetrieveQuestions(QuestionIDList)
        self.AnswerQuestions()
        CorrectAnswer = self.RetrieveAnswers(QuestionIDList)
        self.MarkQuestions(CorrectAnswer,QuestionIDList)

if __name__ == "__main__":
    StudentTest = StudentTest('',0,[],[])
    StudentTest.menuchoice()
