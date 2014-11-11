import Base
import sys
from PyQt4.QtGui import*
from PyQt4.QtGui import*
from PyQt4 import QtGui
from A2_Physics_TestingClass import *
from A2_Physics_Test_Tester import *
from A2_Physics_Type_Controller import *
from A2_Physics_Student_Controller import *
from A2_Physics_Answers_Controller import *
from A2_Physics_Attempt_Controller import *
from A2_Physics_TestQuestions_Controller import *
from A2_Physics_Response_Controller import *
from A2_Physics_Propulsion_redone import *
from A2_Physics_Projectile import*
from PyQt4 import QtGui, QtCore
#MainWindow
class MainWindow(QMainWindow):
    #constructor
    def __init__(self):
        #parentconstructor
        super().__init__()
        self.setWindowTitle('Physics Simulation')
        self.setWindowIcon(QtGui.QIcon('physics.png'))
        self.make_menubar()
            
    def make_menubar(self):
        """This creates a menu bar on which i can run the entire program """
        #this creates the exit action
        exitAction = QtGui.QAction(QtGui.QIcon("exit.png"),"&exit", self)
        exitAction.setShortcut('Ctrl+E+X')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
        #this runs the simulation menu
        DisplaySimulation = QtGui.QAction(QtGui.QIcon("Run Simulation.png"),"&Run Simualtion", self)
        DisplaySimulation.setShortcut("Ctrl+S")
        DisplaySimulation.setStatusTip("Displaying Simuation menu")
        DisplaySimulation.triggered.connect(self.RunSimulation)
        #this runs the Questions Menu
        DisplayQuestions = QtGui.QAction(QtGui.QIcon("Run Test.png"),"&Select Test", self)
        DisplayQuestions.setShortcut("Ctrl+T")
        DisplayQuestions.setStatusTip("Dislaying Test Selection Menu")
        DisplayQuestions.triggered.connect(self.TestSelection)
        #this allows you to logout
        DisplayPlayerName = QtGui.QAction(QtGui.QIcon("Display Questions.png"),"&Hello", self)
        DisplayPlayerName.setShortcut("Ctrl+P")
        DisplayPlayerName.setStatusTip("Dialog box for logging out")
        DisplayPlayerName.triggered.connect(self.StudentLogout)                                  
        #This allows you to View the database editor
        TestEditor = QtGui.QAction(QtGui.QIcon("Test Editor.png"),"&Test Editor", self)
        TestEditor.setShortcut("Ctrl+T+E")
        TestEditor.setStatusTip("Test Editor")
        TestEditor.triggered.connect(self.TestViewWindow)
        StudentEditor = QtGui.QAction(QtGui.QIcon("Student Editor.png"),"&Student Editor",self)
        StudentEditor.setShortcut("Ctrl+S")
        StudentEditor.setStatusTip("Student Editor")
        StudentEditor.triggered.connect(self.StudentViewWindow)
        QuestionEditor = QtGui.QAction(QtGui.QIcon("Question Editor.png"),"&Question Editor",self)
        QuestionEditor.setShortcut("Ctrl+Q")
        QuestionEditor.setStatusTip("Question Editor")
        QuestionEditor.triggered.connect(self.QuestionViewWindow)
        AttemptEditor = QtGui.QAction(QtGui.QIcon("Attempt Editor.png"),"&Attempt Editor",self)
        AttemptEditor.setShortcut("Ctrl+A+T")
        AttemptEditor.setStatusTip("Attempt Editor")
        AttemptEditor.triggered.connect(self.AttemptViewWindow)
        ResponseEditor = QtGui.QAction(QtGui.QIcon("Response Editor.png"),"&Response Editor",self)
        ResponseEditor.setShortcut("Ctrl+R")
        ResponseEditor.setStatusTip("Response Editor")
        ResponseEditor.triggered.connect(self.ResponseViewWindow)
        TestQuestionsEditor = QtGui.QAction(QtGui.QIcon("Test Questions Editor.png"),"&Test Questions Editor",self)
        TestQuestionsEditor.setShortcut("Ctrl+T+Q")
        TestQuestionsEditor.setStatusTip("Test Questions Editor")
        TestQuestionsEditor.triggered.connect(self.TestQuestionsViewWindow)
        TypeEditor = QtGui.QAction(QtGui.QIcon("Type Editor.png"),"&Type Editor",self)
        TypeEditor.setShortcut("Ctrl+T+Y")
        TypeEditor.setStatusTip("Type Editor")
        TypeEditor.triggered.connect(self.TypeViewWindow)
        AnswersEditor = QtGui.QAction(QtGui.QIcon("Answers Editor.png"),"&Answers Editor",self)
        AnswersEditor.setShortcut("Ctrl+A+N")
        AnswersEditor.setStatusTip("Answers Editor")
        AnswersEditor.triggered.connect(self.AnswersViewWindow)
        
        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        SimulationMenu = menubar.addMenu("&Simulation")
        QuestionsMenu = menubar.addMenu("&Testing")
        DatabaseMenu = menubar.addMenu("&Editor")
        DatabaseMenu.addAction(TestEditor)
        DatabaseMenu.addAction(QuestionEditor)
        DatabaseMenu.addAction(TypeEditor)
        DatabaseMenu.addAction(StudentEditor)
        DatabaseMenu.addAction(AnswersEditor)
        DatabaseMenu.addAction(AttemptEditor)
        DatabaseMenu.addAction(ResponseEditor)
        DatabaseMenu.addAction(TestQuestionsEditor)        
        SimulationMenu.addAction(DisplaySimulation)
        QuestionsMenu.addAction(DisplayQuestions)
        fileMenu.addAction(exitAction)
        self.setGeometry(300, 300, 300, 200)
        self.show()


        
    def TestViewWindow(self):
        test = Test_Controller()
        results = test.Return_TestsNoInput()
        Maxrows = len(results)
        self.setWindowTitle('Test Editor')
        self.RecordTable = QTableWidget(Maxrows,2)
        self.RecordTable.setHorizontalHeaderLabels(['ID Number','Test Name'])
        row = 0
        column = 0
        for i in range(0,2):
            for each in results:
                #print(each)
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                print(self.RecordTable.setItem(row,column,item))
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        #create table and push buttons
        #Searchfor Test
        self.SearchItem = QLineEdit('Test_Name')
        self.SearchSubmit = QPushButton('Start Search')
        self.AddTestButton = QPushButton('Add')
        self.EditTestButton = QPushButton('Edit')
        self.DeleteTestButton = QPushButton('Delete')
        #create layout
        self.TableBox = QVBoxLayout()
        self.TableBox.addWidget(self.RecordTable)
        #create vertical layout
        self.ButtonLayout = QHBoxLayout()
        self.ButtonLayout.addWidget(self.AddTestButton)
        self.ButtonLayout.addWidget(self.EditTestButton)
        self.ButtonLayout.addWidget(self.DeleteTestButton)
        #scond to last layout
        self.LastLayout = QVBoxLayout()
        self.LastLayout.addLayout(self.TableBox)
        self.LastLayout.addWidget(self.SearchItem)
        self.LastLayout.addWidget(self.SearchSubmit)
        self.LastLayout.addLayout(self.ButtonLayout)
        #Final Layout
        self.TestLayout = QWidget()
        self.TestLayout.setLayout(self.LastLayout)
        self.setCentralWidget(self.TestLayout)
        #connect
        self.AddTestButton.clicked.connect(self.AddTest)
        self.EditTestButton.clicked.connect(self.EditTest)
        self.DeleteTestButton.clicked.connect(self.DeleteTest)
        self.SearchSubmit.clicked.connect(self.SearchTestLayout)
        

    def SearchTestLayout(self):
        #Items
        Search = self.SearchItem.text()
        test = TestTestingClass()
        results = test.SearchFortest(Search)
        self.setWindowTitle('Test Editor')
        #create table and push buttons
        if results == [] or None:
            print('The Search failed')
        Maxrows = len(results)
        self.RecordTableSearchresults = QTableWidget(Maxrows,2)
        self.RecordTableSearchresults.setHorizontalHeaderLabels(['ID Number','Test Name'])
        row = 0
        column = 0
        for i in range(0,2):
            for each in results:
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                Item = QTableWidgetItem(additem)
                self.RecordTableSearchresults.setItem(row,column,Item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        #Searchfor Test
        self.SearchItem = QLineEdit('Test_Name')
        self.SearchSubmit = QPushButton('Start Search')
        self.AddTestButton = QPushButton('Add')
        self.EditTestButton = QPushButton('Edit')
        self.DeleteTestButton = QPushButton('Delete')
        #create layout
        self.TableBox = QVBoxLayout()
        self.TableBox.addWidget(self.RecordTableSearchresults)
        #create vertical layout
        self.ButtonLayout = QHBoxLayout()
        self.ButtonLayout.addWidget(self.AddTestButton)
        self.ButtonLayout.addWidget(self.EditTestButton)
        self.ButtonLayout.addWidget(self.DeleteTestButton)
        #scond to last layout
        self.LastLayout = QVBoxLayout()
        self.LastLayout.addLayout(self.TableBox)
        self.LastLayout.addWidget(self.SearchItem)
        self.LastLayout.addWidget(self.SearchSubmit)
        self.LastLayout.addLayout(self.ButtonLayout)
        #Final Layout
        self.TestLayout = QWidget()
        self.TestLayout.setLayout(self.LastLayout)
        self.setCentralWidget(self.TestLayout)
        #connect
        self.AddTestButton.clicked.connect(self.AddTest)
        self.EditTestButton.clicked.connect(self.EditTest)
        self.DeleteTestButton.clicked.connect(self.DeleteTest)
        
        
        


        
    def AddTest(self):
        test = Test_Controller()
        results = test.Return_TestsNoInput()
        self.setWindowTitle('Add Test')
        #create table and push buttons
        Maxrows = len(results)
        self.setWindowTitle('Test Editor')
        #create table and push buttons
        self.RecordTable = QTableWidget(Maxrows,2)
        self.RecordTable.setHorizontalHeaderLabels(['ID Number','Test Name'])
        row = 0
        column = 0
        for i in range(0,2):
            for each in results:
                #print(each)
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                self.RecordTable.setItem(row,column,item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        self.TestLabel = QLabel('Enter an appropriate Test here!')
        self.TestName = QLineEdit()
        self.SubmitChanges = QPushButton('Submit Changes')
        #create table layout
        self.TableLayout = QVBoxLayout()
        self.TableLayout.addWidget(self.RecordTable)
        #create layout
        self.AddTestLayout = QGridLayout()
        self.AddTestLayout.addWidget(self.TestLabel,0,0)
        self.AddTestLayout.addWidget(self.TestName,1,0)
        self.AddTestLayout.addWidget(self.SubmitChanges,2,0)
        self.FinalLayout = QVBoxLayout()
        self.FinalLayout.addLayout(self.TableLayout)
        self.FinalLayout.addLayout(self.AddTestLayout)
        self.AddTestLayout = QWidget()
        self.AddTestLayout.setLayout(self.FinalLayout)
        self.setCentralWidget(self.AddTestLayout)
        #something about result of line edit etc 
        self.SubmitChanges.clicked.connect(self.AddTestchanges)
        
    def AddTestchanges(self):
        self.Test_Name = self.TestName.text()
        test = Test_Controller()
        test.Add_Test(self.Test_Name)

    def EditTest(self):
        test = Test_Controller()
        results = test.Return_TestsNoInput()
        self.setWindowTitle('Test Editor')
        #create table and push buttons
        Maxrows = len(results)
        self.RecordTable = QTableWidget(Maxrows,2)
        self.RecordTable.setHorizontalHeaderLabels(['ID Number','Test Name'])
        row = 0
        column = 0
        for i in range(0,2):
            for each in results:
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                self.RecordTable.setItem(row,column,item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        self.Test_IDLabel = QLabel('enter an appropriate Test ID')
        self.Test_NameLabel = QLabel('Enter an appropriate Test')
        self.Test_ID = QLineEdit('Test_ID')
        self.TestName = QLineEdit('Test_Name')
        self.SubmitChanges = QPushButton('Submit Results')
        #create layout for labels and line edits
        self.InputLayout = QGridLayout()
        self.InputLayout.addWidget(self.Test_IDLabel,0,0)
        self.InputLayout.addWidget(self.Test_NameLabel,0,1)
        self.InputLayout.addWidget(self.Test_ID,1,0)
        self.InputLayout.addWidget(self.TestName,1,1)        
        #mainWidget
        self.FinalLayout =QVBoxLayout()
        self.FinalLayout.addWidget(self.RecordTable)
        self.FinalLayout.addLayout(self.InputLayout)
        self.FinalLayout.addWidget(self.SubmitChanges)
        self.EditQuestion = QWidget()
        self.EditQuestion.setLayout(self.FinalLayout)
        self.setCentralWidget(self.EditQuestion)
        #connections
        self.SubmitChanges.clicked.connect(self.UpdateTestchanges)
        

    def UpdateTestchanges(self):
        Test_ID = self.Test_ID.text()
        Test_Name = self.TestName.text()
        test = Test_Controller()
        print(Test_ID,Test_Name)
        test.Update_Test(Test_ID,Test_Name)
        
    def DeleteTest(self):
        test = Test_Controller()
        results = test.Return_TestsNoInput()
        self.setWindowTitle('Questions Editor')
        Maxrows = len(results)
        self.RecordTable = QTableWidget(Maxrows,2)
        self.RecordTable.setHorizontalHeaderLabels(['ID Number','Test Name'])
        row = 0
        column = 0
        for i in range(0,2):
            for each in results:
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                self.RecordTable.setItem(row,column,item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        #create table and push buttons
        self.TestIDLabel = QLabel('enter an appropriate Test ID')
        self.TestIDinfo = QLineEdit()
        self.SubmitChanges = QPushButton('Submit Changes')
        #create layout for labels and line edits
        self.InputLayout = QGridLayout()
        self.InputLayout.addWidget(self.TestIDLabel,0,0)
        self.InputLayout.addWidget(self.TestIDinfo,0,1)
        #mainWidget
        self.TestLayout =QVBoxLayout()
        self.TestLayout.addWidget(self.RecordTable)
        self.TestLayout.addLayout(self.InputLayout)
        self.TestLayout.addWidget(self.SubmitChanges)
        self.DeleteTest = QWidget()
        self.DeleteTest.setLayout(self.TestLayout)
        self.setCentralWidget(self.DeleteTest)
        #connections
        self.SubmitChanges.clicked.connect(self.DeleteTestchanges)
        
    def DeleteTestchanges(self):
        Test_ID = self.TestIDinfo.text()
        test = Test_Controller()
        test.Delete_Test(Test_ID)

            
        
    def AddQuestion(self):
        results = Questions_Controller.Questions_Controller.Search_QuestionsNoInput()
        self.setWindowTitle('Questions Editor')
        #create table and push buttons
        self.RecordTable = QTable(results)
        self.QuestionLabel = QLabel('Enter an appropriate Question here!')
        self.Type_IDLabel = QLabel('Enter an appropriate ID here')
        self.Questioninfo = QLineEdit('')
        self.Type_IDinfo = QLineEdit('')
        self.SubmitChanges = QPushButton()
        #create layout
        self.AddQuestionLayout = QGridLayout()
        self.AddQuestionLayout.addWidget(self.QuestionLabel,0,0)
        self.AddQuestionLayout.addWidget(self.Type_IDLabel,0,1)
        self.AddQuestionLayout.addWidget(self.Question,1,0)
        self.AddQuestionLayout.addWidget(self.Type_ID,1,1)
        self.AddQuestionLayout.addWidget(self.SubmitChanges,2,0)
        self.AddQuestion = QWidget
        self.EditQuestion.addLayout(QuestionLayout)
        self.setCentralWidget(self.CentralWidget)
        #something about result of line edit etc
        Question = self.Questioninfo.textEdited()
        Type_ID = self.Type_IDinfo.textEdited()
        return Question,Type_ID
        self.SubmitChanges.clicked.connect(AddQuestion)
        
    def AddQuestion(self,Question,Type_ID):
        self.Questions_Controller.Add_Question()
        
    def EditQuestion(self):
        results = Questions_Controller.Questions_Controller.Search_QuestionsNoInput()
        self.setWindowTitle('Questions Editor')
        #create table and push buttons
        self.RecordTable = QTable(results)
        self.QuestionIDLabel = QLabel('enter an appropriate Question ID')
        self.QuestionLabel = QLabel('Enter an appropriate Question')
        self.Type_IDLabel = QLabel('Question Type ID')
        self.QuestionIDinfo = QLineEdit('5656565')
        self.Questioninfo = QLineEdit('######')
        self.Type_IDinfo = QLineEdit('jytjytj')
        self.SubmitChanges = QPushButton()
        #create layout for labels and line edits
        self.InputLayout = QGridLayout
        self.InputLayout.addWidget(self.QuestionIDLabel,0,0)
        self.InputLayout.addWidget(self.QuestionLabel,0,1)
        self.InputLayout.addWidget(self.Type_IDLabel,1,0)
        self.InputLayout.addWidget(self.QuestionIDinfo,1,1)
        self.InputLayout.addWidget(self.Questioninfo,2,0)
        self.InputLayout.addWidget(self.Type_IDinfo,2,1)
        self.InputLayout.addWidget(self.SubmitChanges,2,2)
        #mainWidget
        self.QuestionLayout =QVBoxLayout()
        self.QuestionLayout.addLayout(self.RecordTable)
        self.QuestionLayout.addLayout(self.InputLayout)
        self.EditQuestion = QWidget()
        self.EditQuestion.addLayout(QuestionLayout)
        self.setCentralWidget(self.CentralWidget)
        #connections
        Question_ID = self.QuestionIDinfo.textEdited()
        Question = self.Questioninfo.textEdited()
        Type_ID = self.Type_IDinfo.textEdited()
        return Question_ID,Question,Type_ID
        self.SubmitChanges.clicked.connect(UpdateQuestion)

    def UpdateQuestion(self,Question_ID,Question,Type_ID):
        self.Questions_Controller.Update_Question()
        
    def DeleteQuestion(self):
        results = Questions_Controller.Questions_Controller.Search_QuestionsNoInput()
        self.setWindowTitle('Questions Editor')
        #create table and push buttons
        self.RecordTable = QTable(results)
        self.QuestionIDLabel = QLabel('enter an appropriate Question ID')
        self.QuestionIDInfo = QLineEdit()
        self.SubmitChanges = QPushButton()
        #create layout for labels and line edits
        self.InputLayout = QGridLayout
        self.InputLayout.addWidget(self.QuestionIDLabel,0,0)
        self.InputLayout.addWidget(self.QuestionIDInfo,0,1)
        self.InputLayout.addWidget(self.SubmitChanges,1,0)
        #mainWidget
        self.QuestionLayout =QVBoxLayout()
        self.QuestionLayout.addLayout(self.RecordTable)
        self.QuestionLayout.addLayout(self.InputLayout)
        self.EditQuestion = QWidget()
        self.EditQuestion.addLayout(QuestionLayout)
        self.setCentralWidget(self.CentralWidget)
        #connections
        Question_ID = self.QuestionIDInfo.textEdited()
        return Question_ID
        self.SubmitChanges.clicked.connect(DeleteQuestion)
        
    def DeleteQuestion(self,Question_ID):
        self.Questions_Controller.Delete_Question()

    def StudentLogout(self):
        #Actions
        self.CancelAction = QPushButton("Cancel")
        self.ConfirmAction = QPushButton("Confirm")
        self.DialogLabel = QLabel("Are you sure you would like to Logout?")
        #button layout
        self.ActionBox = QGridLayout()
        self.ActionBox.addWidget(self.ConfirmAction,0,0)
        self.ActionBox.addWidget(self.CancelAction,0,1)
        #main layout
        self.QDialogButtonBox.addWidget(self.DialogLabel)
        self.QDialogButtonBox.addLayout(self.ActionBox)
        if self.ConfirmAction.clicked.connect:
            print("Your login script doesnt exist you idiot!")
        elif self.CancelAction.clicked.connect:
            StudentLogout.close()

    def QuestionViewWindow(self):
        Question = Questions_Controller()
        results = Question.Search_QuestionsNoInput()
        Maxrows = len(results)
        self.setWindowTitle('Question Editor')
        self.RecordTable = QTableWidget(Maxrows,3)
        self.RecordTable.setHorizontalHeaderLabels(['ID Number','Question','Question Type'])
        row = 0
        column = 0
        for i in range(0,3):
            for each in results:
                #print(each)
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                print(self.RecordTable.setItem(row,column,item))
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        #create table and push buttons
        #Searchfor Question
        self.SearchItem = QLineEdit('Question_Name')
        self.SearchSubmit = QPushButton('Start Search')
        self.AddQuestionButton = QPushButton('Add')
        self.EditQuestionButton = QPushButton('Edit')
        self.DeleteQuestionButton = QPushButton('Delete')
        #create layout
        self.TableBox = QVBoxLayout()
        self.TableBox.addWidget(self.RecordTable)
        #create vertical layout
        self.ButtonLayout = QHBoxLayout()
        self.ButtonLayout.addWidget(self.AddQuestionButton)
        self.ButtonLayout.addWidget(self.EditQuestionButton)
        self.ButtonLayout.addWidget(self.DeleteQuestionButton)
        #scond to last layout
        self.LastLayout = QVBoxLayout()
        self.LastLayout.addLayout(self.TableBox)
        self.LastLayout.addWidget(self.SearchItem)
        self.LastLayout.addWidget(self.SearchSubmit)
        self.LastLayout.addLayout(self.ButtonLayout)
        #Final Layout
        self.QuestionLayout = QWidget()
        self.QuestionLayout.setLayout(self.LastLayout)
        self.setCentralWidget(self.QuestionLayout)
        #connect
        self.AddQuestionButton.clicked.connect(self.AddQuestion)
        self.EditQuestionButton.clicked.connect(self.EditQuestion)
        self.DeleteQuestionButton.clicked.connect(self.DeleteQuestion)
        self.SearchSubmit.clicked.connect(self.SearchQuestionLayout)
        

    def SearchQuestionLayout(self):
        #Items
        Search = self.SearchItem.text()
        Question = Questions_Controller()
        results = Question.SearchForQuestion(Search)
        self.setWindowTitle('Question Editor')
        #create table and push buttons
        if results == [] or None:
            print('The Search failed')
        Maxrows = len(results)
        self.RecordTableSearchresults = QTableWidget(Maxrows,3)
        self.RecordTableSearchresults.setHorizontalHeaderLabels(['ID Number','Question Name','Question Type'])
        row = 0
        column = 0
        for i in range(0,3):
            for each in results:
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                Item = QTableWidgetItem(additem)
                self.RecordTableSearchresults.setItem(row,column,Item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        #Searchfor Question
        self.SearchItem = QLineEdit('Question_Name')
        self.SearchSubmit = QPushButton('Start Search')
        self.AddQuestionButton = QPushButton('Add')
        self.EditQuestionButton = QPushButton('Edit')
        self.DeleteQuestionButton = QPushButton('Delete')
        #create layout
        self.TableBox = QVBoxLayout()
        self.TableBox.addWidget(self.RecordTableSearchresults)
        #create vertical layout
        self.ButtonLayout = QHBoxLayout()
        self.ButtonLayout.addWidget(self.AddQuestionButton)
        self.ButtonLayout.addWidget(self.EditQuestionButton)
        self.ButtonLayout.addWidget(self.DeleteQuestionButton)
        #scond to last layout
        self.LastLayout = QVBoxLayout()
        self.LastLayout.addLayout(self.TableBox)
        self.LastLayout.addWidget(self.SearchItem)
        self.LastLayout.addWidget(self.SearchSubmit)
        self.LastLayout.addLayout(self.ButtonLayout)
        #Final Layout
        self.QuestionLayout = QWidget()
        self.QuestionLayout.setLayout(self.LastLayout)
        self.setCentralWidget(self.QuestionLayout)
        #connect
        self.AddQuestionButton.clicked.connect(self.AddQuestion)
        self.EditQuestionButton.clicked.connect(self.EditQuestion)
        self.DeleteQuestionButton.clicked.connect(self.DeleteQuestion)
        
    def AddQuestion(self):
        Question = Questions_Controller()
        results = Question.Search_QuestionsNoInput()
        self.setWindowTitle('Add Question')
        #create table and push buttons
        Maxrows = len(results)
        self.setWindowTitle('Question Editor')
        #create table and push buttons
        self.RecordTable = QTableWidget(Maxrows,3)
        self.RecordTable.setHorizontalHeaderLabels(['ID Number','Question Name','Question Type'])
        row = 0
        column = 0
        for i in range(0,3):
            for each in results:
                #print(each)
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                self.RecordTable.setItem(row,column,item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        self.QuestionLabel = QLabel('Enter an appropriate Question here!')
        self.Question = QLineEdit()
        self.QuestionTypeLabel = QLabel('Enter an appropriate Question Type here!')
        self.QuestionType= QLineEdit()        
        self.SubmitChanges = QPushButton('Submit Changes')
        #create table layout
        self.TableLayout = QVBoxLayout()
        self.TableLayout.addWidget(self.RecordTable)
        #create layout
        self.AddQuestionLayout = QGridLayout()
        self.AddQuestionLayout.addWidget(self.QuestionLabel,0,0)
        self.AddQuestionLayout.addWidget(self.Question,1,0)
        self.AddQuestionLayout.addWidget(self.QuestionTypeLabel,0,1)
        self.AddQuestionLayout.addWidget(self.QuestionType,1,1)
        self.AddQuestionLayout.addWidget(self.SubmitChanges,2,0)
        self.FinalLayout = QVBoxLayout()
        self.FinalLayout.addLayout(self.TableLayout)
        self.FinalLayout.addLayout(self.AddQuestionLayout)
        self.AddQuestionLayout = QWidget()
        self.AddQuestionLayout.setLayout(self.FinalLayout)
        self.setCentralWidget(self.AddQuestionLayout)
        #something about result of line edit etc 
        self.SubmitChanges.clicked.connect(self.AddQuestionchanges)
        
    def AddQuestionchanges(self):
        self.Question_Name = self.Question.text()
        self.Question_Type =self.QuestionType.text()
        Question = Questions_Controller() 
        Question.Add_Question(self.Question_Name,self.Question_Type)

    def EditQuestion(self):
        Question = Questions_Controller()
        results = Question.Search_QuestionsNoInput()
        self.setWindowTitle('Question Editor')
        #create table and push buttons
        Maxrows = len(results)
        self.RecordTable = QTableWidget(Maxrows,3)
        self.RecordTable.setHorizontalHeaderLabels(['ID Number','Question','Question Type'])
        row = 0
        column = 0
        for i in range(0,3):
            for each in results:
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                self.RecordTable.setItem(row,column,item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        self.Question_IDLabel = QLabel('enter an appropriate Question ID')
        self.Question_NameLabel = QLabel('Enter an appropriate Question')
        self.QuestionTypeLabel = QLabel('Enter an appropriate Question Type here!')
        self.QuestionType = QLineEdit('Question_Type')          
        self.Question_ID = QLineEdit('Question_ID')
        self.QuestionName = QLineEdit('Question_Name')
        self.SubmitChanges = QPushButton('Submit Results')
        #create layout for labels and line edits
        self.EditQuestionLayout = QGridLayout()
        self.EditQuestionLayout.addWidget(self.Question_IDLabel,0,0)
        self.EditQuestionLayout.addWidget(self.Question_NameLabel,0,2)
        self.EditQuestionLayout.addWidget(self.QuestionTypeLabel,0,1)
        self.EditQuestionLayout.addWidget(self.QuestionType,1,1)
        self.EditQuestionLayout.addWidget(self.Question_ID,1,0)
        self.EditQuestionLayout.addWidget(self.QuestionName,1,2)        
        #mainWidget
        self.FinalLayout =QVBoxLayout()
        self.FinalLayout.addWidget(self.RecordTable)
        self.FinalLayout.addLayout(self.EditQuestionLayout)
        self.FinalLayout.addWidget(self.SubmitChanges)
        self.EditQuestion = QWidget()
        self.EditQuestion.setLayout(self.FinalLayout)
        self.setCentralWidget(self.EditQuestion)
        #connections
        self.SubmitChanges.clicked.connect(self.UpdateQuestionchanges)

    def UpdateQuestionchanges(self):
        Question_ID = self.Question_ID.text()
        Question = self.QuestionName.text()
        Question_Type = self.QuestionType.text()
        Question1 = Questions_Controller()
        Question1.Update_Question(Question,Question_Type,Question_ID)
        
    def DeleteQuestion(self):
        Question = Questions_Controller()
        results = Question.Search_QuestionsNoInput()
        self.setWindowTitle('Questions Editor')
        Maxrows = len(results)
        self.RecordTable = QTableWidget(Maxrows,3)
        self.RecordTable.setHorizontalHeaderLabels(['ID Number','Question','Question Type'])
        row = 0
        column = 0
        for i in range(0,3):
            for each in results:
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                self.RecordTable.setItem(row,column,item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        #create table and push buttons
        self.QuestionIDLabel = QLabel('enter an appropriate Question ID')
        self.QuestionIDinfo = QLineEdit()
        self.SubmitChanges = QPushButton('Submit Changes')
        #create layout for labels and line edits
        self.InputLayout = QGridLayout()
        self.InputLayout.addWidget(self.QuestionIDLabel,0,0)
        self.InputLayout.addWidget(self.QuestionIDinfo,0,1)
        #mainWidget
        self.QuestionLayout =QVBoxLayout()
        self.QuestionLayout.addWidget(self.RecordTable)
        self.QuestionLayout.addLayout(self.InputLayout)
        self.QuestionLayout.addWidget(self.SubmitChanges)
        self.DeleteQuestion = QWidget()
        self.DeleteQuestion.setLayout(self.QuestionLayout)
        self.setCentralWidget(self.DeleteQuestion)
        #connections
        self.SubmitChanges.clicked.connect(self.DeleteQuestionchanges)
        
    def DeleteQuestionchanges(self):
        Question_ID = self.QuestionIDinfo.text()
        Question = Questions_Controller()
        Question.Delete_Question(Question_ID)

    def TypeViewWindow(self):
        Type = Type_Controller()
        results = Type.Return_TypeNoInput()
        Maxrows = len(results)
        self.setWindowTitle('Type Editor')
        self.TypeRecordTable = QTableWidget(Maxrows,2)
        self.TypeRecordTable.setHorizontalHeaderLabels(['ID Number','Question_Type',])
        row = 0
        column = 0
        for i in range(0,2):
            for each in results:
                #print(each)
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                print(self.TypeRecordTable.setItem(row,column,item))
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        #create table and push buttons
        #Searchfor Type
        self.TypeSearchItem = QLineEdit('Type_Name')
        self.TypeSearchSubmit = QPushButton('Start Search')
        self.AddTypeButton = QPushButton('Add')
        self.EditTypeButton = QPushButton('Edit')
        self.DeleteTypeButton = QPushButton('Delete')
        #create layout
        self.TypeTableBox = QVBoxLayout()
        self.TypeTableBox.addWidget(self.TypeRecordTable)
        #create vertical layout
        self.TypeButtonLayout = QHBoxLayout()
        self.TypeButtonLayout.addWidget(self.AddTypeButton)
        self.TypeButtonLayout.addWidget(self.EditTypeButton)
        self.TypeButtonLayout.addWidget(self.DeleteTypeButton)
        #scond to last layout
        self.TypeLastLayout = QVBoxLayout()
        self.TypeLastLayout.addLayout(self.TypeTableBox)
        self.TypeLastLayout.addWidget(self.TypeSearchItem)
        self.TypeLastLayout.addWidget(self.TypeSearchSubmit)
        self.TypeLastLayout.addLayout(self.TypeButtonLayout)
        #Final Layout
        self.TypeLayout = QWidget()
        self.TypeLayout.setLayout(self.TypeLastLayout)
        self.setCentralWidget(self.TypeLayout)
        #connect
        self.AddTypeButton.clicked.connect(self.AddType)
        self.EditTypeButton.clicked.connect(self.EditType)
        self.DeleteTypeButton.clicked.connect(self.DeleteType)
        self.TypeSearchSubmit.clicked.connect(self.TypeSearchLayout)
        

    def TypeSearchLayout(self):
        #Items
        Search = self.TypeSearchItem.text()
        Type = Type_Controller()
        results = Type.SearchForType(Search)
        print(results)
        self.setWindowTitle('Type Editor')
        #create table and push buttons
        if results == [] or None:
            print('The Search failed')
        Maxrows = len(results)
        self.TypeRecordTableSearchresults = QTableWidget(Maxrows,2)
        self.TypeRecordTableSearchresults.setHorizontalHeaderLabels(['ID Number','Question_Type',])
        row = 0
        column = 0
        for i in range(0,2):
            for each in results:
                print(each)
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                self.TypeRecordTableSearchresults.setItem(row,column,item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
                        
        #Searchfor Type
        self.TypeSearchItem = QLineEdit('Type_Name')
        self.TypeSearchSubmit = QPushButton('Start Search')
        self.AddTypeButton = QPushButton('Add')
        self.EditTypeButton = QPushButton('Edit')
        self.DeleteTypeButton = QPushButton('Delete')
        #create layout
        self.TypeTableBox = QVBoxLayout()
        self.TypeTableBox.addWidget(self.TypeRecordTableSearchresults)
        #create vertical layout
        self.TypeButtonLayout = QHBoxLayout()
        self.TypeButtonLayout.addWidget(self.AddTypeButton)
        self.TypeButtonLayout.addWidget(self.EditTypeButton)
        self.TypeButtonLayout.addWidget(self.DeleteTypeButton)
        #scond to last layout
        self.TypeLastLayout = QVBoxLayout()
        self.TypeLastLayout.addLayout(self.TypeTableBox)
        self.TypeLastLayout.addWidget(self.TypeSearchItem)
        self.TypeLastLayout.addWidget(self.TypeSearchSubmit)
        self.TypeLastLayout.addLayout(self.TypeButtonLayout)
        #Final Layout
        self.TypeLayout = QWidget()
        self.TypeLayout.setLayout(self.TypeLastLayout)
        self.setCentralWidget(self.TypeLayout)
        #connect
        self.AddTypeButton.clicked.connect(self.AddType)
        self.EditTypeButton.clicked.connect(self.EditType)
        self.DeleteTypeButton.clicked.connect(self.DeleteType)
        
    def AddType(self):
        Type = Type_Controller()
        results = Type.Return_TypeNoInput()
        self.setWindowTitle('Add Type')
        #create table and push buttons
        Maxrows = len(results)
        self.setWindowTitle('Type Editor')
        #create table and push buttons
        self.RecordTable = QTableWidget(Maxrows,2)
        self.RecordTable.setHorizontalHeaderLabels(['ID Number','Question_Type'])
        row = 0
        column = 0
        for i in range(0,2):
            for each in results:
                #print(each)
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                self.RecordTable.setItem(row,column,item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        self.Question_TypeLabel = QLabel('Enter an appropriate Question Type here!')
        self.Question_Type= QLineEdit()        
        self.SubmitChanges = QPushButton('Submit Changes')
        #create table layout
        self.TableLayout = QVBoxLayout()
        self.TableLayout.addWidget(self.RecordTable)
        #create layout
        self.AddTypeLayout = QGridLayout()
        self.AddTypeLayout.addWidget(self.Question_TypeLabel,0,0)
        self.AddTypeLayout.addWidget(self.Question_Type,0,1)
        self.FinalLayout = QVBoxLayout()
        self.FinalLayout.addLayout(self.TableLayout)
        self.FinalLayout.addLayout(self.AddTypeLayout)
        self.FinalLayout.addWidget(self.SubmitChanges)
        self.AddTypeLayout = QWidget()
        self.AddTypeLayout.setLayout(self.FinalLayout)
        self.setCentralWidget(self.AddTypeLayout)
        #something about result of line edit etc 
        self.SubmitChanges.clicked.connect(self.AddTypechanges)
        
    def AddTypechanges(self):
        self.Type_Name = self.Question_Type.text()
        Type = Type_Controller() 
        Type.Add_Type(self.Type_Name)

    def EditType(self):
        Type = Type_Controller()
        results = Type.Return_TypeNoInput()
        self.setWindowTitle('Type Editor')
        #create table and push buttons
        Maxrows = len(results)
        self.RecordTable = QTableWidget(Maxrows,2)
        self.RecordTable.setHorizontalHeaderLabels(['ID Number','Question_TypeType'])
        row = 0
        column = 0
        for i in range(0,2):
            for each in results:
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                self.RecordTable.setItem(row,column,item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        self.Type_IDLabel = QLabel('enter an appropriate Type ID')
        self.Question_TypeLabel = QLabel('Enter an appropriate Question_Type')
        self.Question_Type= QLineEdit('Question_Type')          
        self.Type_ID = QLineEdit('Type_ID')
        self.SubmitChanges = QPushButton('Submit Results')
        #create layout for labels and line edits
        self.EditTypeLayout = QGridLayout()
        self.EditTypeLayout.addWidget(self.Type_IDLabel,0,0)
        self.EditTypeLayout.addWidget(self.Question_TypeLabel,0,1)
        self.EditTypeLayout.addWidget(self.Question_Type,1,1)
        self.EditTypeLayout.addWidget(self.Type_ID,1,0)     
        #mainWidget
        self.FinalLayout =QVBoxLayout()
        self.FinalLayout.addWidget(self.RecordTable)
        self.FinalLayout.addLayout(self.EditTypeLayout)
        self.FinalLayout.addWidget(self.SubmitChanges)
        self.EditType = QWidget()
        self.EditType.setLayout(self.FinalLayout)
        self.setCentralWidget(self.EditType)
        #connections
        self.SubmitChanges.clicked.connect(self.UpdateTypechanges)

    def UpdateTypechanges(self):
        Type_ID = self.Type_ID.text()
        Question_Type = self.Question_Type.text()
        Type = Type_Controller()
        Type.Update_Type(Type_ID,Question_Type)
        
    def DeleteType(self):
        Type = Type_Controller()
        results = Type.Return_TypeNoInput()
        self.setWindowTitle('Types Editor')
        Maxrows = len(results)
        self.RecordTable = QTableWidget(Maxrows,2)
        self.RecordTable.setHorizontalHeaderLabels(['ID Number','Question_Type'])
        row = 0
        column = 0
        for i in range(0,2):
            for each in results:
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                self.RecordTable.setItem(row,column,item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        #create table and push buttons
        self.TypeIDLabel = QLabel('enter an appropriate Type ID')
        self.TypeIDinfo = QLineEdit()
        self.SubmitChanges = QPushButton('Submit Changes')
        #create layout for labels and line edits
        self.InputLayout = QGridLayout()
        self.InputLayout.addWidget(self.TypeIDLabel,0,0)
        self.InputLayout.addWidget(self.TypeIDinfo,0,1)
        #mainWidget
        self.TypeLayout =QVBoxLayout()
        self.TypeLayout.addWidget(self.RecordTable)
        self.TypeLayout.addLayout(self.InputLayout)
        self.TypeLayout.addWidget(self.SubmitChanges)
        self.DeleteType = QWidget()
        self.DeleteType.setLayout(self.TypeLayout)
        self.setCentralWidget(self.DeleteType)
        #connections
        self.SubmitChanges.clicked.connect(self.DeleteTypechanges)
        
    def DeleteTypechanges(self):
        Type_ID = self.TypeIDinfo.text()
        Type = Type_Controller()
        Type.Delete_Type(Type_ID)


    def StudentViewWindow(self):
        Student = Student_Controller()
        results = Student.Return_StudentNoInput()
        Maxrows = len(results)
        self.setWindowTitle('Student Editor')
        self.StudentViewRecordTable = QTableWidget(Maxrows,3)
        self.StudentViewRecordTable.setHorizontalHeaderLabels(['Student ID','First Name','Last Name'])
        row = 0
        column = 0
        for i in range(0,3):
            for each in results:
                #print(each)
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                print(self.StudentViewRecordTable.setItem(row,column,item))
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        #create table and push buttons
        #Searchfor Student
        self.SearchItem = QLineEdit('Student_Name')
        self.StudentSearchSubmit = QPushButton('Start Search')
        self.AddStudentButton = QPushButton('Add')
        self.EditStudentButton = QPushButton('Edit')
        self.DeleteStudentButton = QPushButton('Delete')
        #create layout
        self.StudentTableBox = QVBoxLayout()
        self.StudentTableBox.addWidget(self.StudentViewRecordTable)
        #create vertical layout
        self.StudentButtonLayout = QHBoxLayout()
        self.StudentButtonLayout.addWidget(self.AddStudentButton)
        self.StudentButtonLayout.addWidget(self.EditStudentButton)
        self.StudentButtonLayout.addWidget(self.DeleteStudentButton)
        #scond to last layout
        self.StudentSearchLastLayout = QVBoxLayout()
        self.StudentSearchLastLayout.addLayout(self.StudentTableBox)
        self.StudentSearchLastLayout.addWidget(self.SearchItem)
        self.StudentSearchLastLayout.addWidget(self.StudentSearchSubmit)
        self.StudentSearchLastLayout.addLayout(self.StudentButtonLayout)
        #Final Layout
        self.StudentLayout = QWidget()
        self.StudentLayout.setLayout(self.StudentSearchLastLayout)
        self.setCentralWidget(self.StudentLayout)
        #connect
        self.AddStudentButton.clicked.connect(self.AddStudent)
        self.EditStudentButton.clicked.connect(self.EditStudent)
        self.DeleteStudentButton.clicked.connect(self.DeleteStudent)
        self.StudentSearchSubmit.clicked.connect(self.StudentSearchLayout)
        

    def StudentSearchLayout(self):
        #Items
        Search = self.SearchItem.text()
        Student = Student_Controller()
        results = Student.SearchForStudent(Search)
        print(results)
        self.setWindowTitle('Student Editor')
        #create table and push buttons
        if results == [] or None:
            print('The Search failed')
        Maxrows = len(results)
        self.StudentRecordTableSearchresults = QTableWidget(Maxrows,3)
        self.StudentRecordTableSearchresults.setHorizontalHeaderLabels(['ID Number','First Name','Last Name'])
        row = 0
        column = 0
        for i in range(0,3):
            for each in results:
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                self.StudentRecordTableSearchresults.setItem(row,column,item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        #Searchfor Student
        self.SearchItem = QLineEdit('Student_Name')
        self.StudentSearchSubmit = QPushButton('Start Search')
        self.AddStudentButton = QPushButton('Add')
        self.EditStudentButton = QPushButton('Edit')
        self.DeleteStudentButton = QPushButton('Delete')
        #create layout
        self.StudentTableBox = QVBoxLayout()
        self.StudentTableBox.addWidget(self.StudentRecordTableSearchresults)
        #create vertical layout
        self.StudentButtonLayout = QHBoxLayout()
        self.StudentButtonLayout.addWidget(self.AddStudentButton)
        self.StudentButtonLayout.addWidget(self.EditStudentButton)
        self.StudentButtonLayout.addWidget(self.DeleteStudentButton)
        #scond to last layout
        self.StudentSearchLastLayout = QVBoxLayout()
        self.StudentSearchLastLayout.addLayout(self.StudentTableBox)
        self.StudentSearchLastLayout.addWidget(self.SearchItem)
        self.StudentSearchLastLayout.addWidget(self.StudentSearchSubmit)
        self.StudentSearchLastLayout.addLayout(self.StudentButtonLayout)
        #Final Layout
        self.StudentLayout = QWidget()
        self.StudentLayout.setLayout(self.StudentSearchLastLayout)
        self.setCentralWidget(self.StudentLayout)
        #connect
        self.AddStudentButton.clicked.connect(self.AddStudent)
        self.EditStudentButton.clicked.connect(self.EditStudent)
        self.DeleteStudentButton.clicked.connect(self.DeleteStudent)
        
    def AddStudent(self):
        Student = Student_Controller()
        results = Student.Return_StudentNoInput()
        self.setWindowTitle('Add Student')
        #create table and push buttons
        Maxrows = len(results)
        self.setWindowTitle('Student Editor')
        #create table and push buttons
        self.AddStudentRecordTable = QTableWidget(Maxrows,3)
        self.AddStudentRecordTable.setHorizontalHeaderLabels(['ID Number','First Name','Last Name'])
        row = 0
        column = 0
        for i in range(0,3):
            for each in results:
                #print(each)
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                self.AddStudentRecordTable.setItem(row,column,item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        self.StudentFirstNameLabel = QLabel('Enter an appropriate First Name here!')
        self.StudentLastNameLabel = QLabel('Enter an appropriate Last Name here!')
        self.First_Name =  QLineEdit()
        self.Last_Name = QLineEdit()
        self.SubmitChanges = QPushButton('Submit Changes')
        #create table layout
        self.AddStudentTableLayout = QVBoxLayout()
        self.AddStudentTableLayout.addWidget(self.AddStudentRecordTable)
        #create layout
        self.AddStudentLayout = QGridLayout()
        self.AddStudentLayout.addWidget(self.StudentFirstNameLabel,0,0)
        self.AddStudentLayout.addWidget(self.StudentLastNameLabel,0,1)
        self.AddStudentLayout.addWidget(self.First_Name,1,0)
        self.AddStudentLayout.addWidget(self.Last_Name,1,1)
        self.AddStudentFinalLayout = QVBoxLayout()
        self.AddStudentFinalLayout.addLayout(self.AddStudentTableLayout)
        self.AddStudentFinalLayout.addLayout(self.AddStudentLayout)
        self.AddStudentFinalLayout.addWidget(self.SubmitChanges)
        self.AddStudentLayout = QWidget()
        self.AddStudentLayout.setLayout(self.AddStudentFinalLayout)
        self.setCentralWidget(self.AddStudentLayout)
        #something about result of line edit etc 
        self.SubmitChanges.clicked.connect(self.AddStudentchanges)
        
    def AddStudentchanges(self):
        self.StudentFirst_Name = self.First_Name.text()
        self.StudentLast_Name = self.Last_Name.text()
        Student = Student_Controller() 
        Student.Add_Student(self.StudentFirst_Name,self.StudentLast_Name)

    def EditStudent(self):
        Student = Student_Controller()
        results = Student.Return_StudentNoInput()
        self.setWindowTitle('Student Editor')
        #create table and push buttons
        Maxrows = len(results)
        self.EditStudentRecordTable = QTableWidget(Maxrows,3)
        self.EditStudentRecordTable.setHorizontalHeaderLabels(['ID Number','First Name','Last Name'])
        row = 0
        column = 0
        for i in range(0,3):
            for each in results:
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                self.EditStudentRecordTable.setItem(row,column,item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        self.Student_IDLabel = QLabel('enter an appropriate Student ID')
        self.StudentFirstNameLabel = QLabel('Enter an appropriate First Name')
        self.StudentLastNameLabel = QLabel('Enter an appropriate Last Name')
        self.Student_ID= QLineEdit('Student_ID')          
        self.StudentFirstName = QLineEdit('First_Name')
        self.StudentLastName = QLineEdit('Last_Name')
        self.SubmitChanges = QPushButton('Submit Results')
        #create layout for labels and line edits
        self.EditStudentInputLayout = QGridLayout()
        self.EditStudentInputLayout.addWidget(self.Student_IDLabel,0,0)
        self.EditStudentInputLayout.addWidget(self.StudentFirstNameLabel,1,0)
        self.EditStudentInputLayout.addWidget(self.StudentLastNameLabel,2,0)
        self.EditStudentInputLayout.addWidget(self.Student_ID,0,1)
        self.EditStudentInputLayout.addWidget(self.StudentFirstName,1,1)
        self.EditStudentInputLayout.addWidget(self.StudentLastName,2,1)
        #mainWidget
        self.EditStudentFinalLayout =QVBoxLayout()
        self.EditStudentFinalLayout.addWidget(self.EditStudentRecordTable)
        self.EditStudentFinalLayout.addLayout(self.EditStudentInputLayout)
        self.EditStudentFinalLayout.addWidget(self.SubmitChanges)
        self.EditStudent = QWidget()
        self.EditStudent.setLayout(self.EditStudentFinalLayout)
        self.setCentralWidget(self.EditStudent)
        #connections
        self.SubmitChanges.clicked.connect(self.UpdateStudentchanges)

    def UpdateStudentchanges(self):
        Student_ID = self.Student_ID.text()
        First_Name = self.StudentFirstName.text()
        Last_Name = self.StudentLastName.text()
        Student = Student_Controller()
        Student.Update_Student(First_Name,Last_Name,Student_ID)
        
    def DeleteStudent(self):
        Student = Student_Controller()
        results = Student.Return_StudentNoInput()
        self.setWindowTitle('Students Editor')
        Maxrows = len(results)
        self.DeleteStudentRecordTable = QTableWidget(Maxrows,3)
        self.DeleteStudentRecordTable.setHorizontalHeaderLabels(['ID Number','First Name','Last Name'])
        row = 0
        column = 0
        for i in range(0,3):
            for each in results:
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                self.DeleteStudentRecordTable.setItem(row,column,item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        #create table and push buttons
        self.StudentIDLabel = QLabel('enter an appropriate Student ID')
        self.StudentIDinfo = QLineEdit()
        self.SubmitChanges = QPushButton('Submit Changes')
        #create layout for labels and line edits
        self.DeleteStudentInputLayout = QGridLayout()
        self.DeleteStudentInputLayout.addWidget(self.StudentIDLabel,0,0)
        self.DeleteStudentInputLayout.addWidget(self.StudentIDinfo,0,1)
        #mainWidget
        self.DeleteStudentLayout =QVBoxLayout()
        self.DeleteStudentLayout.addWidget(self.DeleteStudentRecordTable)
        self.DeleteStudentLayout.addLayout(self.DeleteStudentInputLayout)
        self.DeleteStudentLayout.addWidget(self.SubmitChanges)
        self.DeleteStudent = QWidget()
        self.DeleteStudent.setLayout(self.DeleteStudentLayout)
        self.setCentralWidget(self.DeleteStudent)
        #connections
        self.SubmitChanges.clicked.connect(self.DeleteStudentchanges)
        
    def DeleteStudentchanges(self):
        Student_ID = self.StudentIDinfo.text()
        Student = Student_Controller()
        Student.Delete_Student(Student_ID)

    def AnswersViewWindow(self):
        Answers = Answers_Controller()
        results = Answers.Return_AnswersNoInput()
        Maxrows = len(results)
        self.setWindowTitle('Answers Editor')
        self.AnswersViewRecordTable = QTableWidget(Maxrows,3)
        self.AnswersViewRecordTable.setHorizontalHeaderLabels(['Answers ID','Correct Answer','Questions ID'])
        row = 0
        column = 0
        for i in range(0,3):
            for each in results:
                #print(each)
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                print(self.AnswersViewRecordTable.setItem(row,column,item))
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        #create table and push buttons
        #Searchfor Answers
        self.SearchItem = QLineEdit('Answers_Name')
        self.AnswersSearchSubmit = QPushButton('Start Search')
        self.AddAnswersButton = QPushButton('Add')
        self.EditAnswersButton = QPushButton('Edit')
        self.DeleteAnswersButton = QPushButton('Delete')
        #create layout
        self.AnswersTableBox = QVBoxLayout()
        self.AnswersTableBox.addWidget(self.AnswersViewRecordTable)
        #create vertical layout
        self.AnswersButtonLayout = QHBoxLayout()
        self.AnswersButtonLayout.addWidget(self.AddAnswersButton)
        self.AnswersButtonLayout.addWidget(self.EditAnswersButton)
        self.AnswersButtonLayout.addWidget(self.DeleteAnswersButton)
        #scond to last layout
        self.AnswersSearchLastLayout = QVBoxLayout()
        self.AnswersSearchLastLayout.addLayout(self.AnswersTableBox)
        self.AnswersSearchLastLayout.addWidget(self.SearchItem)
        self.AnswersSearchLastLayout.addWidget(self.AnswersSearchSubmit)
        self.AnswersSearchLastLayout.addLayout(self.AnswersButtonLayout)
        #Final Layout
        self.AnswersLayout = QWidget()
        self.AnswersLayout.setLayout(self.AnswersSearchLastLayout)
        self.setCentralWidget(self.AnswersLayout)
        #connect
        self.AddAnswersButton.clicked.connect(self.AddAnswers)
        self.EditAnswersButton.clicked.connect(self.EditAnswers)
        self.DeleteAnswersButton.clicked.connect(self.DeleteAnswers)
        self.AnswersSearchSubmit.clicked.connect(self.AnswersSearchLayout)
        

    def AnswersSearchLayout(self):
        #Items
        Search = self.SearchItem.text()
        Answers = Answers_Controller()
        results = Answers.SearchForAnswers(Search)
        print(results)
        self.setWindowTitle('Answers Editor')
        #create table and push buttons
        if results == [] or None:
            print('The Search failed')
        Maxrows = len(results)
        self.AnswersRecordTableSearchresults = QTableWidget(Maxrows,3)
        self.AnswersRecordTableSearchresults.setHorizontalHeaderLabels(['ID Number','Correct Answer','Questions ID'])
        row = 0
        column = 0
        for i in range(0,3):
            for each in results:
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                Item = QTableWidgetItem(additem)
                self.AnswersRecordTableSearchresults.setItem(row,column,Item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        #Searchfor Answers
        self.SearchItem = QLineEdit('Answers_Name')
        self.AnswersSearchSubmit = QPushButton('Start Search')
        self.AddAnswersButton = QPushButton('Add')
        self.EditAnswersButton = QPushButton('Edit')
        self.DeleteAnswersButton = QPushButton('Delete')
        #create layout
        self.AnswersTableBox = QVBoxLayout()
        self.AnswersTableBox.addWidget(self.AnswersRecordTableSearchresults)
        #create vertical layout
        self.AnswersButtonLayout = QHBoxLayout()
        self.AnswersButtonLayout.addWidget(self.AddAnswersButton)
        self.AnswersButtonLayout.addWidget(self.EditAnswersButton)
        self.AnswersButtonLayout.addWidget(self.DeleteAnswersButton)
        #scond to last layout
        self.AnswersSearchLastLayout = QVBoxLayout()
        self.AnswersSearchLastLayout.addLayout(self.AnswersTableBox)
        self.AnswersSearchLastLayout.addWidget(self.SearchItem)
        self.AnswersSearchLastLayout.addWidget(self.AnswersSearchSubmit)
        self.AnswersSearchLastLayout.addLayout(self.AnswersButtonLayout)
        #Final Layout
        self.AnswersLayout = QWidget()
        self.AnswersLayout.setLayout(self.AnswersSearchLastLayout)
        self.setCentralWidget(self.AnswersLayout)
        #connect
        self.AddAnswersButton.clicked.connect(self.AddAnswers)
        self.EditAnswersButton.clicked.connect(self.EditAnswers)
        self.DeleteAnswersButton.clicked.connect(self.DeleteAnswers)
        
    def AddAnswers(self):
        Answers = Answers_Controller()
        results = Answers.Return_AnswersNoInput()
        self.setWindowTitle('Add Answers')
        #create table and push buttons
        Maxrows = len(results)
        self.setWindowTitle('Answers Editor')
        #create table and push buttons
        self.AddAnswersRecordTable = QTableWidget(Maxrows,3)
        self.AddAnswersRecordTable.setHorizontalHeaderLabels(['ID Number','Correct Answer','Questions ID'])
        row = 0
        column = 0
        for i in range(0,3):
            for each in results:
                #print(each)
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                self.AddAnswersRecordTable.setItem(row,column,item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        self.AnswersLabel = QLabel('Enter an appropriate Answer here!')
        self.AnswersQuestionIDLabel = QLabel('Enter an appropriate Question_ID here!')
        self.CorrectAnswer= QLineEdit()
        self.AnswersQuestionID = QLineEdit()
        self.SubmitChanges = QPushButton('Submit Changes')
        #create table layout
        self.AddAnswersTableLayout = QVBoxLayout()
        self.AddAnswersTableLayout.addWidget(self.AddAnswersRecordTable)
        #create layout
        self.AddAnswersLayout = QGridLayout()
        self.AddAnswersLayout.addWidget(self.AnswersLabel,0,0)
        self.AddAnswersLayout.addWidget(self.AnswersQuestionIDLabel,0,1)
        self.AddAnswersLayout.addWidget(self.CorrectAnswer,1,0)
        self.AddAnswersLayout.addWidget(self.AnswersQuestionID,1,1)
        self.AddAnswersFinalLayout = QVBoxLayout()
        self.AddAnswersFinalLayout.addLayout(self.AddAnswersTableLayout)
        self.AddAnswersFinalLayout.addLayout(self.AddAnswersLayout)
        self.AddAnswersFinalLayout.addWidget(self.SubmitChanges)
        self.AddLastAnswersLayout = QWidget()
        self.AddLastAnswersLayout.setLayout(self.AddAnswersFinalLayout)
        self.setCentralWidget(self.AddLastAnswersLayout)
        #something about result of line edit etc 
        self.SubmitChanges.clicked.connect(self.AddAnswerschanges)
        
    def AddAnswerschanges(self):
        self.Answers_Name = self.CorrectAnswer.text()
        self.AnswersQuestion = self.AnswersQuestionID.text()
        Answers = Answers_Controller() 
        Answers.Add_Answer(self.Answers_Name,self.AnswersQuestion)

    def EditAnswers(self):
        Answers = Answers_Controller()
        results = Answers.Return_AnswersNoInput()
        self.setWindowTitle('Answers Editor')
        #create table and push buttons
        Maxrows = len(results)
        self.EditAnswersRecordTable = QTableWidget(Maxrows,3)
        self.EditAnswersRecordTable.setHorizontalHeaderLabels(['ID Number','Correct Answer','Questions ID'])
        row = 0
        column = 0
        for i in range(0,3):
            for each in results:
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                self.EditAnswersRecordTable.setItem(row,column,item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        self.Answers_IDLabel = QLabel('Enter an appropriate Answers ID')
        self.CorrectAnswersLabel = QLabel('Enter an appropriate Correct Answer')
        self.AnswersQuestionIDLabel= QLabel('Enter an appropriate QuestionID')
        self.Answers_ID= QLineEdit('Answers_ID')
        self.AnswersQuestionID= QLineEdit('Questions_ID')
        self.CorrectAnswer = QLineEdit('Correct_Answer')
        self.SubmitChanges = QPushButton('Submit Results')
        #create layout for labels and line edits
        self.EditAnswersInputLayout = QGridLayout()
        self.EditAnswersInputLayout.addWidget(self.Answers_IDLabel,0,0)
        self.EditAnswersInputLayout.addWidget(self.CorrectAnswersLabel,1,0)
        self.EditAnswersInputLayout.addWidget(self.AnswersQuestionIDLabel,2,0)
        self.EditAnswersInputLayout.addWidget(self.Answers_ID,0,1)
        self.EditAnswersInputLayout.addWidget(self.CorrectAnswer,1,1)
        self.EditAnswersInputLayout.addWidget(self.AnswersQuestionID,2,1)
        
        #mainWidget
        self.EditAnswersFinalLayout =QVBoxLayout()
        self.EditAnswersFinalLayout.addWidget(self.EditAnswersRecordTable)
        self.EditAnswersFinalLayout.addLayout(self.EditAnswersInputLayout)
        self.EditAnswersFinalLayout.addWidget(self.SubmitChanges)
        self.EditAnswers = QWidget()
        self.EditAnswers.setLayout(self.EditAnswersFinalLayout)
        self.setCentralWidget(self.EditAnswers)
        #connections
        self.SubmitChanges.clicked.connect(self.UpdateAnswerschanges)

    def UpdateAnswerschanges(self):
        Answers_ID = self.Answers_ID.text()
        CorrectAnswer = self.CorrectAnswer.text()
        Question_ID = self.AnswersQuestionID.text()
        Answers = Answers_Controller()
        Answers.Update_Answer(CorrectAnswer,Question_ID,Answers_ID)
        
    def DeleteAnswers(self):
        Answers = Answers_Controller()
        results = Answers.Return_AnswersNoInput()
        self.setWindowTitle('Answerss Editor')
        Maxrows = len(results)
        self.DeleteAnswersRecordTable = QTableWidget(Maxrows,3)
        self.DeleteAnswersRecordTable.setHorizontalHeaderLabels(['ID Number','Correct Answer','Questions ID'])
        row = 0
        column = 0
        for i in range(0,3):
            for each in results:
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                self.DeleteAnswersRecordTable.setItem(row,column,item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        #create table and push buttons
        self.AnswersIDLabel = QLabel('enter an appropriate Answers ID')
        self.AnswersIDinfo = QLineEdit()
        self.SubmitChanges = QPushButton('Submit Changes')
        #create layout for labels and line edits
        self.DeleteAnswersInputLayout = QGridLayout()
        self.DeleteAnswersInputLayout.addWidget(self.AnswersIDLabel,0,0)
        self.DeleteAnswersInputLayout.addWidget(self.AnswersIDinfo,0,1)
        #mainWidget
        self.DeleteAnswersLayout =QVBoxLayout()
        self.DeleteAnswersLayout.addWidget(self.DeleteAnswersRecordTable)
        self.DeleteAnswersLayout.addLayout(self.DeleteAnswersInputLayout)
        self.DeleteAnswersLayout.addWidget(self.SubmitChanges)
        self.DeleteAnswers = QWidget()
        self.DeleteAnswers.setLayout(self.DeleteAnswersLayout)
        self.setCentralWidget(self.DeleteAnswers)
        #connections
        self.SubmitChanges.clicked.connect(self.DeleteAnswerschanges)
        
    def DeleteAnswerschanges(self):
        Answers_ID = self.AnswersIDinfo.text()
        Answers = Answers_Controller()
        Answers.Delete_Answer(Answers_ID)
        
    def AttemptViewWindow(self):
        Attempt = Attempts_Controller()
        results = Attempt.Return_AttemptNoInput()
        Maxrows = len(results)
        self.setWindowTitle('Attempt Editor')
        self.AttemptViewRecordTable = QTableWidget(Maxrows,5)
        self.AttemptViewRecordTable.setHorizontalHeaderLabels(['Attempt ID','Attempt_Score','Time_in_session','Date_of_Use','Test_ID','student_ID'])
        row = 0
        column = 0
        for i in range(0,5):
            for each in results:
                #print(each)
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                self.AttemptViewRecordTable.setItem(row,column,item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        #create table and push buttons
        #Searchfor Attempt
        self.SearchItem = QLineEdit('Attempt_Name')
        self.AttemptSearchSubmit = QPushButton('Start Search')
        self.AddAttemptButton = QPushButton('Add')
        self.EditAttemptButton = QPushButton('Edit')
        self.DeleteAttemptButton = QPushButton('Delete')
        #create layout
        self.AttemptTableBox = QVBoxLayout()
        self.AttemptTableBox.addWidget(self.AttemptViewRecordTable)
        #create vertical layout
        self.AttemptButtonLayout = QHBoxLayout()
        self.AttemptButtonLayout.addWidget(self.AddAttemptButton)
        self.AttemptButtonLayout.addWidget(self.EditAttemptButton)
        self.AttemptButtonLayout.addWidget(self.DeleteAttemptButton)
        #scond to last layout
        self.AttemptSearchLastLayout = QVBoxLayout()
        self.AttemptSearchLastLayout.addLayout(self.AttemptTableBox)
        self.AttemptSearchLastLayout.addWidget(self.SearchItem)
        self.AttemptSearchLastLayout.addWidget(self.AttemptSearchSubmit)
        self.AttemptSearchLastLayout.addLayout(self.AttemptButtonLayout)
        #Final Layout
        self.AttemptLayout = QWidget()
        self.AttemptLayout.setLayout(self.AttemptSearchLastLayout)
        self.setCentralWidget(self.AttemptLayout)
        #connect
        self.AddAttemptButton.clicked.connect(self.AddAttempt)
        self.EditAttemptButton.clicked.connect(self.EditAttempt)
        self.DeleteAttemptButton.clicked.connect(self.DeleteAttempt)
        self.AttemptSearchSubmit.clicked.connect(self.AttemptSearchLayout)
        

    def AttemptSearchLayout(self):
        #Items
        Search = self.SearchItem.text()
        Attempt = Attempts_Controller()
        results = Attempt.SearchForAttempt(Search)
        print(results)
        self.setWindowTitle('Attempt Editor')
        #create table and push buttons
        if results == [] or None:
            print('The Search failed')
        Maxrows = len(results)
        self.AttemptRecordTableSearchresults = QTableWidget(Maxrows,5)
        self.AttemptRecordTableSearchresults.setHorizontalHeaderLabels(['Attempt ID','Attempt_Score','Time_in_session','Date_of_Use','Test_ID','student_ID'])
        row = 0
        column = 0
        for i in range(0,5):
            for each in results:
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                Item = QTableWidgetItem(additem)
                self.AttemptRecordTableSearchresults.setItem(row,column,Item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        #Searchfor Attempt
        self.SearchItem = QLineEdit('Attempt_Name')
        self.AttemptSearchSubmit = QPushButton('Start Search')
        self.AddAttemptButton = QPushButton('Add')
        self.EditAttemptButton = QPushButton('Edit')
        self.DeleteAttemptButton = QPushButton('Delete')
        #create layout
        self.AttemptTableBox = QVBoxLayout()
        self.AttemptTableBox.addWidget(self.AttemptRecordTableSearchresults)
        #create vertical layout
        self.AttemptButtonLayout = QHBoxLayout()
        self.AttemptButtonLayout.addWidget(self.AddAttemptButton)
        self.AttemptButtonLayout.addWidget(self.EditAttemptButton)
        self.AttemptButtonLayout.addWidget(self.DeleteAttemptButton)
        #scond to last layout
        self.AttemptSearchLastLayout = QVBoxLayout()
        self.AttemptSearchLastLayout.addLayout(self.AttemptTableBox)
        self.AttemptSearchLastLayout.addWidget(self.SearchItem)
        self.AttemptSearchLastLayout.addWidget(self.AttemptSearchSubmit)
        self.AttemptSearchLastLayout.addLayout(self.AttemptButtonLayout)
        #Final Layout
        self.AttemptLayout = QWidget()
        self.AttemptLayout.setLayout(self.AttemptSearchLastLayout)
        self.setCentralWidget(self.AttemptLayout)
        #connect
        self.AddAttemptButton.clicked.connect(self.AddAttempt)
        self.EditAttemptButton.clicked.connect(self.EditAttempt)
        self.DeleteAttemptButton.clicked.connect(self.DeleteAttempt)
        
    def AddAttempt(self):
        Attempt = Attempts_Controller()
        results = Attempt.Return_AttemptNoInput()
        self.setWindowTitle('Add Attempt')
        #create table and push buttons
        Maxrows = len(results)
        self.setWindowTitle('Attempt Editor')
        #create table and push buttons
        self.AddAttemptRecordTable = QTableWidget(Maxrows,5)
        self.AddAttemptRecordTable.setHorizontalHeaderLabels(['Attempt ID','Attempt_Score','Time_in_session','Date_of_Use','Test_ID','Student_ID'])
        row = 0
        column = 0
        for i in range(0,5):
            for each in results:
                #print(each)
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                self.AddAttemptRecordTable.setItem(row,column,item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        self.AttemptScoreLabel = QLabel('Enter an appropriate Attempt Score here!')
        self.TimeinSessionLabel = QLabel('Enter an appropriate Time in Session here!')
        self.DateOfUseLabel = QLabel('Enter an appropriate DateOfUse here!')
        self.TestIDLabel = QLabel('Enter an appropriate TestID here!')
        self.StudentIDLabel = QLabel('Enter an appropriate Student ID here!')
        self.AtteptScore = QLineEdit('AttemptScore')
        self.TimeinSession = QLineEdit('TimeinSession')
        self.DateOfUse = QLineEdit('DateOfUse')
        self.TestID = QLineEdit('TestID')
        self.StudentID = QLineEdit('StudentID')
        self.SubmitChanges = QPushButton('Submit Changes')
        #create table layout
        self.AddAttemptTableLayout = QVBoxLayout()
        self.AddAttemptTableLayout.addWidget(self.AddAttemptRecordTable)
        self.AddAttemptLayout = QGridLayout()
        self.AddAttemptLayout.addWidget(self.AttemptScoreLabel,0,0)
        self.AddAttemptLayout.addWidget(self.TimeinSessionLabel,1,0)
        self.AddAttemptLayout.addWidget(self.DateOfUseLabel,2,0)
        self.AddAttemptLayout.addWidget(self.TestIDLabel,3,0)
        self.AddAttemptLayout.addWidget(self.StudentIDLabel,4,0)
        
        self.AddAttemptLayout.addWidget(self.AtteptScore,0,1)
        self.AddAttemptLayout.addWidget(self.TimeinSession,1,1)
        self.AddAttemptLayout.addWidget(self.DateOfUse,2,1)
        self.AddAttemptLayout.addWidget(self.TestID,3,1)
        self.AddAttemptLayout.addWidget(self.StudentID,4,1)
        #create layout
        self.AddAttemptFinalLayout = QVBoxLayout()
        self.AddAttemptFinalLayout.addLayout(self.AddAttemptTableLayout)
        self.AddAttemptFinalLayout.addLayout(self.AddAttemptLayout)
        self.AddAttemptFinalLayout.addWidget(self.SubmitChanges)
        self.AddAttemptLayout = QWidget()
        self.AddAttemptLayout.setLayout(self.AddAttemptFinalLayout)
        self.setCentralWidget(self.AddAttemptLayout)
        #something about result of line edit etc 
        self.SubmitChanges.clicked.connect(self.AddAttemptchanges)
        
    def AddAttemptchanges(self):
        AttemptScore1 = self.AtteptScore.text()
        TimeinSession1 = self.TimeinSession.text()
        DateOfUse1 = self.DateOfUse.text()
        TestID1 = self.TestID.text()
        StudentID1 = self.StudentID.text()
        Attempt = Attempts_Controller() 
        Attempt.Add_Attempts(AttemptScore1,TimeinSession1,DateOfUse1,TestID1,StudentID1)

    def EditAttempt(self):
        Attempt = Attempts_Controller()
        results = Attempt.Return_AttemptNoInput()
        self.setWindowTitle('Attempt Editor')
        #create table and push buttons
        Maxrows = len(results)
        self.EditAttemptRecordTable = QTableWidget(Maxrows,5)
        self.EditAttemptRecordTable.setHorizontalHeaderLabels(['Attempt ID','Attempt_Score','Time_in_session','Date_of_Use','Test_ID','student_ID'])
        row = 0
        column = 0
        for i in range(0,5):
            for each in results:
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                self.EditAttemptRecordTable.setItem(row,column,item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        self.AttemptIDLabel = QLabel('Enter an appropriate Attempt ID here!')
        self.AttemptScoreLabel = QLabel('Enter an appropriate Score here!')
        self.TimeinSessionLabel = QLabel('Enter an appropriate Time in session here!')
        self.DateOfUseLabel = QLabel('Enter an appropriate Date of Use here!')
        self.TestIDLabel = QLabel('Enter an appropriate Test ID here!')
        self.StudentIDLabel = QLabel('Enter an appropriate Student ID here!')
        self.AttemptID = QLineEdit('Attempt ID')
        self.AtteptScore = QLineEdit('AttemptScore')
        self.TimeinSession = QLineEdit('TimeinSession')
        self.DateOfUse = QLineEdit('DateOfUse')
        self.TestID = QLineEdit('TestID')
        self.StudentID = QLineEdit('StudentID')
        self.SubmitChanges = QPushButton('SubmitChanges')
        #create layout for labels and line edits
        self.EditAttemptLayout = QGridLayout()
        self.EditAttemptLayout.addWidget(self.AttemptIDLabel,0,0)
        self.EditAttemptLayout.addWidget(self.AttemptScoreLabel,1,0)
        self.EditAttemptLayout.addWidget(self.TimeinSessionLabel,2,0)
        self.EditAttemptLayout.addWidget(self.DateOfUseLabel,3,0)
        self.EditAttemptLayout.addWidget(self.TestIDLabel,4,0)
        self.EditAttemptLayout.addWidget(self.StudentIDLabel,5,0)
        
        self.EditAttemptLayout.addWidget(self.AttemptID,0,1)
        self.EditAttemptLayout.addWidget(self.AtteptScore,1,1)
        self.EditAttemptLayout.addWidget(self.TimeinSession,2,1)
        self.EditAttemptLayout.addWidget(self.DateOfUse,3,1)
        self.EditAttemptLayout.addWidget(self.TestID,4,1)
        self.EditAttemptLayout.addWidget(self.StudentID,5,1)
        #mainWidget
        self.EditAttemptFinalLayout =QVBoxLayout()
        self.EditAttemptFinalLayout.addWidget(self.EditAttemptRecordTable)
        self.EditAttemptFinalLayout.addLayout(self.EditAttemptLayout)
        self.EditAttemptFinalLayout.addWidget(self.SubmitChanges)
        self.EditAttempt = QWidget()
        self.EditAttempt.setLayout(self.EditAttemptFinalLayout)
        self.setCentralWidget(self.EditAttempt)
        #connections
        self.SubmitChanges.clicked.connect(self.UpdateAttemptchanges)

    def UpdateAttemptchanges(self):
        Attempt_ID = self.AttemptID.text()
        AtteptScore = self.AtteptScore.text()
        TimeinSession = self.TimeinSession.text()
        DateOfUse = self.DateOfUse.text()
        TestID = self.TestID.text()
        StudentID = self.StudentID.text()
        Attempt = Attempts_Controller()
        Attempt.Update_Attempts(Attempt_ID,AtteptScore,TimeinSession,DateOfUse,TestID,StudentID)
        
    def DeleteAttempt(self):
        Attempt = Attempts_Controller()
        results = Attempt.Return_AttemptNoInput()
        self.setWindowTitle('Attempts Editor')
        Maxrows = len(results)
        self.DeleteAttemptRecordTable = QTableWidget(Maxrows,5)
        self.DeleteAttemptRecordTable.setHorizontalHeaderLabels(['Attempt ID','Attempt_Score','Time_in_session','Date_of_Use','Test_ID','student_ID'])
        row = 0
        column = 0
        for i in range(0,5):
            for each in results:
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                self.DeleteAttemptRecordTable.setItem(row,column,item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        #create table and push buttons
        self.AttemptIDLabel = QLabel('enter an appropriate Attempt ID')
        self.AttemptIDinfo = QLineEdit()
        self.SubmitChanges = QPushButton('Submit Changes')
        #create layout for labels and line edits
        self.DeleteAttemptInputLayout = QGridLayout()
        self.DeleteAttemptInputLayout.addWidget(self.AttemptIDLabel,0,0)
        self.DeleteAttemptInputLayout.addWidget(self.AttemptIDinfo,0,1)
        #mainWidget
        self.DeleteAttemptLayout =QVBoxLayout()
        self.DeleteAttemptLayout.addWidget(self.DeleteAttemptRecordTable)
        self.DeleteAttemptLayout.addLayout(self.DeleteAttemptInputLayout)
        self.DeleteAttemptLayout.addWidget(self.SubmitChanges)
        self.DeleteAttempt = QWidget()
        self.DeleteAttempt.setLayout(self.DeleteAttemptLayout)
        self.setCentralWidget(self.DeleteAttempt)
        #connections
        self.SubmitChanges.clicked.connect(self.DeleteAttemptchanges)
        
    def DeleteAttemptchanges(self):
        Attempt_ID = self.AttemptIDinfo.text()
        Attempt = Attempts_Controller()
        Attempt.Delete_Attempts(Attempt_ID)


    def TestQuestionsViewWindow(self):
        TestQuestions = TestQuestions_Controller()
        results = TestQuestions.Return_TestQuestionsNoInput()
        Maxrows = len(results)
        self.setWindowTitle('TestQuestions Editor')
        self.TestQuestionsRecordTable = QTableWidget(Maxrows,3)
        self.TestQuestionsRecordTable.setHorizontalHeaderLabels(['ID Number','Question_ID','Test_ID'])
        row = 0
        column = 0
        for i in range(0,3):
            for each in results:
                #print(each)
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                self.TestQuestionsRecordTable.setItem(row,column,item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        #create table and push buttons
        #Searchfor TestQuestions
        self.TestQuestionsSearchItem = QLineEdit('TestQuestions_Name')
        self.TestQuestionsSearchSubmit = QPushButton('Start Search')
        self.AddTestQuestionsButton = QPushButton('Add')
        self.EditTestQuestionsButton = QPushButton('Edit')
        self.DeleteTestQuestionsButton = QPushButton('Delete')
        #create layout
        self.TestQuestionsTableBox = QVBoxLayout()
        self.TestQuestionsTableBox.addWidget(self.TestQuestionsRecordTable)
        #create vertical layout
        self.TestQuestionsButtonLayout = QHBoxLayout()
        self.TestQuestionsButtonLayout.addWidget(self.AddTestQuestionsButton)
        self.TestQuestionsButtonLayout.addWidget(self.EditTestQuestionsButton)
        self.TestQuestionsButtonLayout.addWidget(self.DeleteTestQuestionsButton)
        #scond to last layout
        self.TestQuestionsLastLayout = QVBoxLayout()
        self.TestQuestionsLastLayout.addLayout(self.TestQuestionsTableBox)
        self.TestQuestionsLastLayout.addWidget(self.TestQuestionsSearchItem)
        self.TestQuestionsLastLayout.addWidget(self.TestQuestionsSearchSubmit)
        self.TestQuestionsLastLayout.addLayout(self.TestQuestionsButtonLayout)
        #Final Layout
        self.TestQuestionsLayout = QWidget()
        self.TestQuestionsLayout.setLayout(self.TestQuestionsLastLayout)
        self.setCentralWidget(self.TestQuestionsLayout)
        #connect
        self.AddTestQuestionsButton.clicked.connect(self.AddTestQuestions)
        self.EditTestQuestionsButton.clicked.connect(self.EditTestQuestions)
        self.DeleteTestQuestionsButton.clicked.connect(self.DeleteTestQuestions)
        self.TestQuestionsSearchSubmit.clicked.connect(self.TestQuestionsSearchLayout)
        

    def TestQuestionsSearchLayout(self):
        #Items
        Search = self.TestQuestionsSearchItem.text()
        TestQuestions = TestQuestions_Controller()
        results = TestQuestions.SearchForTestQuestions(Search)
        print(results)
        self.setWindowTitle('TestQuestions Editor')
        #create table and push buttons
        if results == [] or None:
            print('The Search failed')
        Maxrows = len(results)
        self.TestQuestionsRecordTableSearchresults = QTableWidget(Maxrows,3)
        self.TestQuestionsRecordTableSearchresults.setHorizontalHeaderLabels(['ID Number','Question_ID','Test_ID'])
        row = 0
        column = 0
        for i in range(0,3):
            for each in results:
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                self.TestQuestionsRecordTableSearchresults.setItem(row,column,item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0         
        #Searchfor TestQuestions
        self.TestQuestionsSearchItem = QLineEdit('TestQuestions_Name')
        self.TestQuestionsSearchSubmit = QPushButton('Start Search')
        self.AddTestQuestionsButton = QPushButton('Add')
        self.EditTestQuestionsButton = QPushButton('Edit')
        self.DeleteTestQuestionsButton = QPushButton('Delete')
        #create layout
        self.TestQuestionsTableBox = QVBoxLayout()
        self.TestQuestionsTableBox.addWidget(self.TestQuestionsRecordTableSearchresults)
        #create vertical layout
        self.TestQuestionsButtonLayout = QHBoxLayout()
        self.TestQuestionsButtonLayout.addWidget(self.AddTestQuestionsButton)
        self.TestQuestionsButtonLayout.addWidget(self.EditTestQuestionsButton)
        self.TestQuestionsButtonLayout.addWidget(self.DeleteTestQuestionsButton)
        #scond to last layout
        self.TestQuestionsLastLayout = QVBoxLayout()
        self.TestQuestionsLastLayout.addLayout(self.TestQuestionsTableBox)
        self.TestQuestionsLastLayout.addWidget(self.TestQuestionsSearchItem)
        self.TestQuestionsLastLayout.addWidget(self.TestQuestionsSearchSubmit)
        self.TestQuestionsLastLayout.addLayout(self.TestQuestionsButtonLayout)
        #Final Layout
        self.TestQuestionsLayout = QWidget()
        self.TestQuestionsLayout.setLayout(self.TestQuestionsLastLayout)
        self.setCentralWidget(self.TestQuestionsLayout)
        #connect
        self.AddTestQuestionsButton.clicked.connect(self.AddTestQuestions)
        self.EditTestQuestionsButton.clicked.connect(self.EditTestQuestions)
        self.DeleteTestQuestionsButton.clicked.connect(self.DeleteTestQuestions)
        
    def AddTestQuestions(self):
        TestQuestions = TestQuestions_Controller()
        results = TestQuestions.Return_TestQuestionsNoInput()
        self.setWindowTitle('Add TestQuestions')
        #create table and push buttons
        Maxrows = len(results)
        self.setWindowTitle('TestQuestions Editor')
        #create table and push buttons
        self.RecordTable = QTableWidget(Maxrows,2)
        self.RecordTable.setHorizontalHeaderLabels(['ID Number','Question_ID','Test_ID'])
        row = 0
        column = 0
        for i in range(0,2):
            for each in results:
                #print(each)
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                self.RecordTable.setItem(row,column,item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        self.TQQuestion_IDLabel = QLabel('Enter an appropriate Question ID here!')
        self.TQQuestion_ID= QLineEdit()  
        self.TQTest_IDLabel = QLabel('Enter an appropriate Test ID here!') 
        self.TQTest_ID= QLineEdit()    
        self.SubmitChanges = QPushButton('Submit Changes')
        #create table layout
        self.TableLayout = QVBoxLayout()
        self.TableLayout.addWidget(self.RecordTable)
        #create layout
        self.AddTestQuestionsLayout = QGridLayout()
        self.AddTestQuestionsLayout.addWidget(self.TQQuestion_IDLabel,0,0)
        self.AddTestQuestionsLayout.addWidget(self.TQQuestion_ID,0,1)
        self.AddTestQuestionsLayout.addWidget(self.TQTest_IDLabel,1,0)
        self.AddTestQuestionsLayout.addWidget(self.TQTest_ID,1,1)
        self.FinalLayout = QVBoxLayout()
        self.FinalLayout.addLayout(self.TableLayout)
        self.FinalLayout.addLayout(self.AddTestQuestionsLayout)
        self.FinalLayout.addWidget(self.SubmitChanges)
        self.AddTestQuestionsLayout = QWidget()
        self.AddTestQuestionsLayout.setLayout(self.FinalLayout)
        self.setCentralWidget(self.AddTestQuestionsLayout)
        #something about result of line edit etc 
        self.SubmitChanges.clicked.connect(self.AddTestQuestionschanges)
        
    def AddTestQuestionschanges(self):
        Questions_ID = self.TQQuestion_ID.text()
        Test_ID = self.TQTest_ID.text()
        TestQuestions = TestQuestions_Controller() 
        TestQuestions.Add_TestQuestions(Questions_ID,Test_ID)

    def EditTestQuestions(self):
        TestQuestions = TestQuestions_Controller()
        results = TestQuestions.Return_TestQuestionsNoInput()
        self.setWindowTitle('TestQuestions Editor')
        #create table and push buttons
        Maxrows = len(results)
        self.RecordTable = QTableWidget(Maxrows,3)
        self.RecordTable.setHorizontalHeaderLabels(['ID Number','Question_ID','Test_ID'])
        row = 0
        column = 0
        for i in range(0,3):
            for each in results:
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                self.RecordTable.setItem(row,column,item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        self.TQQuestion_IDLabel = QLabel('Enter an appropriate Question ID here!')
        self.TQQuestion_ID= QLineEdit()  
        self.TQTest_IDLabel = QLabel('Enter an appropriate Test ID here!') 
        self.TQTest_ID= QLineEdit()    
        self.TQLabel = QLabel('Enter an appropriate Test Questions ID here!') 
        self.TQID= QLineEdit()    
        self.SubmitChanges = QPushButton('Submit Results')
        #create layout for labels and line edits
        self.EditTestQuestionsLayout = QGridLayout()
        self.EditTestQuestionsLayout.addWidget(self.TQQuestion_IDLabel,0,0)
        self.EditTestQuestionsLayout.addWidget(self.TQQuestion_ID,0,1)
        self.EditTestQuestionsLayout.addWidget(self.TQTest_IDLabel,1,1)
        self.EditTestQuestionsLayout.addWidget(self.TQTest_ID,1,0)
        self.EditTestQuestionsLayout.addWidget(self.TQLabel,1,2)
        self.EditTestQuestionsLayout.addWidget(self.TQID,2,0)       
        #mainWidget
        self.FinalLayout =QVBoxLayout()
        self.FinalLayout.addWidget(self.RecordTable)
        self.FinalLayout.addLayout(self.EditTestQuestionsLayout)
        self.FinalLayout.addWidget(self.SubmitChanges)
        self.EditTestQuestions = QWidget()
        self.EditTestQuestions.setLayout(self.FinalLayout)
        self.setCentralWidget(self.EditTestQuestions)
        #connections
        self.SubmitChanges.clicked.connect(self.UpdateTestQuestionschanges)

    def UpdateTestQuestionschanges(self):
        Questions_ID = self.TQQuestion_ID.text()
        Test_ID = self.TQTest_ID.text()
        TestQuestions_ID = self.TQID.text()
        TestQuestions = TestQuestions_Controller()
        TestQuestions.Update_TestQuestions(Questions_ID,Test_ID,TestQuestions_ID)
        
    def DeleteTestQuestions(self):
        TestQuestions = TestQuestions_Controller()
        results = TestQuestions.Return_TestQuestionsNoInput()
        self.setWindowTitle('TestQuestionss Editor')
        Maxrows = len(results)
        self.RecordTable = QTableWidget(Maxrows,2)
        self.RecordTable.setHorizontalHeaderLabels(['ID Number','Question_ID','Test_ID'])
        row = 0
        column = 0
        for i in range(0,2):
            for each in results:
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                self.RecordTable.setItem(row,column,item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        #create table and push buttons
        self.TestQuestionsIDLabel = QLabel('enter an appropriate TestQuestions ID')
        self.TestQuestionsIDinfo = QLineEdit()
        self.SubmitChanges = QPushButton('Submit Changes')
        #create layout for labels and line edits
        self.InputLayout = QGridLayout()
        self.InputLayout.addWidget(self.TestQuestionsIDLabel,0,0)
        self.InputLayout.addWidget(self.TestQuestionsIDinfo,0,1)
        #mainWidget
        self.TestQuestionsLayout =QVBoxLayout()
        self.TestQuestionsLayout.addWidget(self.RecordTable)
        self.TestQuestionsLayout.addLayout(self.InputLayout)
        self.TestQuestionsLayout.addWidget(self.SubmitChanges)
        self.DeleteTestQuestions = QWidget()
        self.DeleteTestQuestions.setLayout(self.TestQuestionsLayout)
        self.setCentralWidget(self.DeleteTestQuestions)
        #connections
        self.SubmitChanges.clicked.connect(self.DeleteTestQuestionschanges)
        
    def DeleteTestQuestionschanges(self):
        TestQuestions_ID = self.TestQuestionsIDinfo.text()
        TestQuestions = TestQuestions_Controller()
        TestQuestions.Delete_TestQuestions(TestQuestions_ID)


    def ResponseViewWindow(self):
        Response = Response_Controller()
        results = Response.Return_ResponseNoInput()
        Maxrows = len(results)
        self.setWindowTitle('Response Editor')
        self.ResponseRecordTable = QTableWidget(Maxrows,4)
        self.ResponseRecordTable.setHorizontalHeaderLabels(['ID Number','Question_ID','Attempt_ID','Student Response'])
        row = 0
        column = 0
        for i in range(0,4):
            for each in results:
                #print(each)
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                self.ResponseRecordTable.setItem(row,column,item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        #create table and push buttons
        #Searchfor Response
        self.ResponseSearchItem = QLineEdit('Response_Name')
        self.ResponseSearchSubmit = QPushButton('Start Search')
        self.AddResponseButton = QPushButton('Add')
        self.EditResponseButton = QPushButton('Edit')
        self.DeleteResponseButton = QPushButton('Delete')
        #create layout
        self.ResponseTableBox = QVBoxLayout()
        self.ResponseTableBox.addWidget(self.ResponseRecordTable)
        #create vertical layout
        self.ResponseButtonLayout = QHBoxLayout()
        self.ResponseButtonLayout.addWidget(self.AddResponseButton)
        self.ResponseButtonLayout.addWidget(self.EditResponseButton)
        self.ResponseButtonLayout.addWidget(self.DeleteResponseButton)
        #scond to last layout
        self.ResponseLastLayout = QVBoxLayout()
        self.ResponseLastLayout.addLayout(self.ResponseTableBox)
        self.ResponseLastLayout.addWidget(self.ResponseSearchItem)
        self.ResponseLastLayout.addWidget(self.ResponseSearchSubmit)
        self.ResponseLastLayout.addLayout(self.ResponseButtonLayout)
        #Final Layout
        self.ResponseLayout = QWidget()
        self.ResponseLayout.setLayout(self.ResponseLastLayout)
        self.setCentralWidget(self.ResponseLayout)
        #connect
        self.AddResponseButton.clicked.connect(self.AddResponse)
        self.EditResponseButton.clicked.connect(self.EditResponse)
        self.DeleteResponseButton.clicked.connect(self.DeleteResponse)
        self.ResponseSearchSubmit.clicked.connect(self.ResponseSearchLayout)
        

    def ResponseSearchLayout(self):
        #Items
        Search = self.ResponseSearchItem.text()
        Response = Response_Controller()
        results = Response.SearchForResponse(Search)
        print(results)
        self.setWindowTitle('Response Editor')
        #create table and push buttons
        if results == [] or None:
            print('The Search failed')
        Maxrows = len(results)
        self.ResponseRecordTableSearchresults = QTableWidget(Maxrows,4)
        self.ResponseRecordTableSearchresults.setHorizontalHeaderLabels(['ID Number','Question_ID','Attempt_ID','Student Response'])
        row = 0
        column = 0
        for i in range(0,4):
            for each in results:
                print(each)
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                self.ResponseRecordTableSearchresults.setItem(row,column,item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
                        
        #Searchfor Response
        self.ResponseSearchItem = QLineEdit('Response_Name')
        self.ResponseSearchSubmit = QPushButton('Start Search')
        self.AddResponseButton = QPushButton('Add')
        self.EditResponseButton = QPushButton('Edit')
        self.DeleteResponseButton = QPushButton('Delete')
        #create layout
        self.ResponseTableBox = QVBoxLayout()
        self.ResponseTableBox.addWidget(self.ResponseRecordTableSearchresults)
        #create vertical layout
        self.ResponseButtonLayout = QHBoxLayout()
        self.ResponseButtonLayout.addWidget(self.AddResponseButton)
        self.ResponseButtonLayout.addWidget(self.EditResponseButton)
        self.ResponseButtonLayout.addWidget(self.DeleteResponseButton)
        #scond to last layout
        self.ResponseLastLayout = QVBoxLayout()
        self.ResponseLastLayout.addLayout(self.ResponseTableBox)
        self.ResponseLastLayout.addWidget(self.ResponseSearchItem)
        self.ResponseLastLayout.addWidget(self.ResponseSearchSubmit)
        self.ResponseLastLayout.addLayout(self.ResponseButtonLayout)
        #Final Layout
        self.ResponseLayout = QWidget()
        self.ResponseLayout.setLayout(self.ResponseLastLayout)
        self.setCentralWidget(self.ResponseLayout)
        #connect
        self.AddResponseButton.clicked.connect(self.AddResponse)
        self.EditResponseButton.clicked.connect(self.EditResponse)
        self.DeleteResponseButton.clicked.connect(self.DeleteResponse)
        
    def AddResponse(self):
        Response = Response_Controller()
        results = Response.Return_ResponseNoInput()
        self.setWindowTitle('Add Response')
        #create table and push buttons
        Maxrows = len(results)
        self.setWindowTitle('Response Editor')
        #create table and push buttons
        self.RecordTable = QTableWidget(Maxrows,4)
        self.RecordTable.setHorizontalHeaderLabels(['ID Number','Question_ID','Attempt_ID','Student Response'])
        row = 0
        column = 0
        for i in range(0,4):
            for each in results:
                #print(each)
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                self.RecordTable.setItem(row,column,item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        self.RQuestion_IDLabel = QLabel('Enter an appropriate Question ID here!')
        self.RQuestion_ID= QLineEdit()  
        self.RAttempt_IDLabel = QLabel('Enter an appropriate Attempt ID here!') 
        self.RAttempt_ID= QLineEdit()    
        self.StudentResponseLabel = QLabel('Enter an appropriate Student Response here!') 
        self.StudentResponse= QLineEdit()    
        self.SubmitChanges = QPushButton('Submit Changes')
        #create table layout
        self.TableLayout = QVBoxLayout()
        self.TableLayout.addWidget(self.RecordTable)
        #create layout
        self.AddResponseLayout = QGridLayout()
        self.AddResponseLayout.addWidget(self.RQuestion_IDLabel,0,0)
        self.AddResponseLayout.addWidget(self.RQuestion_ID,0,1)
        self.AddResponseLayout.addWidget(self.RAttempt_IDLabel,1,0)
        self.AddResponseLayout.addWidget(self.RAttempt_ID,1,1)
        self.AddResponseLayout.addWidget(self.StudentResponseLabel,2,0)
        self.AddResponseLayout.addWidget(self.StudentResponse,2,1)
        self.FinalLayout = QVBoxLayout()
        self.FinalLayout.addLayout(self.TableLayout)
        self.FinalLayout.addLayout(self.AddResponseLayout)
        self.FinalLayout.addWidget(self.SubmitChanges)
        self.AddResponseLayout = QWidget()
        self.AddResponseLayout.setLayout(self.FinalLayout)
        self.setCentralWidget(self.AddResponseLayout)
        #something about result of line edit etc 
        self.SubmitChanges.clicked.connect(self.AddResponsechanges)
        
    def AddResponsechanges(self):
        Questions_ID = self.RQuestion_ID.text()
        Attempt_ID = self.RAttempt_ID.text()
        StudentResponse = self.StudentResponse.text()
        Response = Response_Controller() 
        Response.Add_Response(Questions_ID,Attempt_ID,StudentResponse)

    def EditResponse(self):
        Response = Response_Controller()
        results = Response.Return_ResponseNoInput()
        self.setWindowTitle('Response Editor')
        #create table and push buttons
        Maxrows = len(results)
        self.RecordTable = QTableWidget(Maxrows,4)
        self.RecordTable.setHorizontalHeaderLabels(['ID Number','Question_ID','Attempt_ID','Student Response'])
        row = 0
        column = 0
        for i in range(0,4):
            for each in results:
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                self.RecordTable.setItem(row,column,item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        self.RQuestion_IDLabel = QLabel('Enter an appropriate Question ID here!')
        self.RQuestion_ID= QLineEdit()  
        self.RAttempt_IDLabel = QLabel('Enter an appropriate Attempt ID here!') 
        self.RAttempt_ID= QLineEdit()    
        self.ResponseLabel = QLabel('Enter an appropriate Test Response ID here!') 
        self.ResponseID= QLineEdit()    
        self.StudentResponseLabel = QLabel('Enter an appropriate Student Response here!') 
        self.StudentResponse= QLineEdit()  
        self.SubmitChanges = QPushButton('Submit Results')
        #create layout for labels and line edits
        self.EditResponseLayout = QGridLayout()
        self.EditResponseLayout.addWidget(self.RQuestion_IDLabel,0,0)
        self.EditResponseLayout.addWidget(self.RQuestion_ID,0,1)
        self.EditResponseLayout.addWidget(self.RAttempt_IDLabel,1,1)
        self.EditResponseLayout.addWidget(self.RAttempt_ID,1,0)
        self.EditResponseLayout.addWidget(self.ResponseLabel,1,2)
        self.EditResponseLayout.addWidget(self.ResponseID,2,0) 
        self.EditResponseLayout.addWidget(self.StudentResponseLabel,2,1)
        self.EditResponseLayout.addWidget(self.SubmitChanges,2,2)       
        #mainWidget
        self.FinalLayout =QVBoxLayout()
        self.FinalLayout.addWidget(self.RecordTable)
        self.FinalLayout.addLayout(self.EditResponseLayout)
        self.FinalLayout.addWidget(self.SubmitChanges)
        self.EditResponse = QWidget()
        self.EditResponse.setLayout(self.FinalLayout)
        self.setCentralWidget(self.EditResponse)
        #connections
        self.SubmitChanges.clicked.connect(self.UpdateResponsechanges)

    def UpdateResponsechanges(self):
        Questions_ID = self.RQuestion_ID.text()
        Attempt_ID = self.RAttempt_ID.text()
        Response_ID = self.ResponseID.text()
        StudentResponse = self.StudentResponse.text()
        Response = Response_Controller()
        Response.Update_Response(Questions_ID,Attempt_ID,Response_ID,StudentResponse)
        
    def DeleteResponse(self):
        Response = Response_Controller()
        results = Response.Return_ResponseNoInput()
        self.setWindowTitle('Responses Editor')
        Maxrows = len(results)
        self.RecordTable = QTableWidget(Maxrows,4)
        self.RecordTable.setHorizontalHeaderLabels(['ID Number','Question_ID','Attempt_ID','Student Response'])
        row = 0
        column = 0
        for i in range(0,4):
            for each in results:
                additem = results[row][column]
                if type(additem) == int:
                    additem = str(additem)
                item = QTableWidgetItem(additem)
                self.RecordTable.setItem(row,column,item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
        #create table and push buttons
        self.ResponseIDLabel = QLabel('enter an appropriate Response ID')
        self.ResponseIDinfo = QLineEdit()
        self.SubmitChanges = QPushButton('Submit Changes')
        #create layout for labels and line edits
        self.InputLayout = QGridLayout()
        self.InputLayout.addWidget(self.ResponseIDLabel,0,0)
        self.InputLayout.addWidget(self.ResponseIDinfo,0,1)
        #mainWidget
        self.ResponseLayout =QVBoxLayout()
        self.ResponseLayout.addWidget(self.RecordTable)
        self.ResponseLayout.addLayout(self.InputLayout)
        self.ResponseLayout.addWidget(self.SubmitChanges)
        self.DeleteResponse = QWidget()
        self.DeleteResponse.setLayout(self.ResponseLayout)
        self.setCentralWidget(self.DeleteResponse)
        #connections
        self.SubmitChanges.clicked.connect(self.DeleteResponsechanges)
        
    def DeleteResponsechanges(self):
        Response_ID = self.ResponseIDinfo.text()
        Response = Response_Controller()
        Response.Delete_Response(Response_ID)

    def SUVATInputLayout(self):
        self.setWindowTitle('SimulationWindow')
        #create line edits and labels
        self.SimulationMessage = QLabel("Welcome to SUVAT Equation Simulation")
        self.DisplacementLabel = QLabel("Displacement")
        self.DisplacementLineEdit = QLineEdit()
        self.InitialvelocityLabel = QLabel("Initial Velocity")
        self.InitialvelocityLineEdit = QLineEdit()
        self.FinalLabel = QLabel("Final Velocity")
        self.FinalLineEdit = QLineEdit()
        self.AccelerationLabel = QLabel("Acceleration")
        self.AccelerationLineEdit = QLineEdit()
        self.TimeLabel = QLabel("Time")
        self.TimeLineEdit = QLineEdit()
        self.SubmitButton = QPushButton('SubmitItems')
        #SUVAT inputs
        self.InputGridLayout = QGridLayout()
        self.InputGridLayout.addWidget(self.DisplacementLabel,0,0)
        self.InputGridLayout.addWidget(self.DisplacementLineEdit,0,1)
        self.InputGridLayout.addWidget(self.InitialvelocityLabel,1,0)
        self.InputGridLayout.addWidget(self.InitialvelocityLineEdit,1,1)
        self.InputGridLayout.addWidget(self.FinalLabel,2,0)
        self.InputGridLayout.addWidget(self.FinalLineEdit,2,1)
        self.InputGridLayout.addWidget(self.AccelerationLabel,3,0)
        self.InputGridLayout.addWidget(self.AccelerationLineEdit,3,1)
        self.InputGridLayout.addWidget(self.TimeLabel,4,0)
        self.InputGridLayout.addWidget(self.TimeLineEdit,4,1)
        self.InputsLayout = QVBoxLayout()
        self.InputsLayout.addWidget(self.SimulationMessage)
        self.InputsLayout.addLayout(self.InputGridLayout)
        self.InputsLayout.addWidget(self.SubmitButton)
        #QWidget
        self.SUVATInputsWidget = QWidget()
        self.SUVATInputsWidget.setLayout(self.InputsLayout)
        self.setCentralWidget(self.SUVATInputsWidget)
        #Connect
        self.SubmitButton.clicked.connect(self.SimulationPrep)

    def SimulationPrep(self):
        Displacement = self.DisplacementLineEdit.text()
        try:
            Displacement = int(Displacement)
        except:
            if Displacement == '':
                Displacement = 0
        InitialVelocity = self.InitialvelocityLineEdit.text()
        try:
            InitialVelocity = int(InitialVelocity)
        except:
            if InitialVelocity == '':
                InitialVelocity = 0
        FinalVelocity = self.FinalLineEdit.text()
        try:
            FinalVelocity = int(FinalVelocity)
        except:
            if FinalVelocity == '':
                FinalVelocity = 0
        Acceleration = self.AccelerationLineEdit.text()
        try:
            Acceleration = int(Acceleration)
        except:
            if Acceleration == '':
                Acceleration = 0
        Time = self.TimeLineEdit.text()
        try:
            Time = int(Time)
        except:
            if Time == '':
                Time = 0
        InputList = [Displacement,InitialVelocity,FinalVelocity,Acceleration,Time]
        Propulsion1 = Propulsion('Spaceship',0,0,0,45,InitialVelocity,FinalVelocity,Acceleration,Displacement,Time,-9.81)
        PreSimulationResults = Propulsion1.SUVATInputs(InputList)
        Propulsion1.SUVATLink(PreSimulationResults)
        SUVAT = Propulsion1.StartSimulation()
        SUVAT2 = Propulsion1.getSuvat()
        self.SimulationWindow(SUVAT,SUVAT2)
        
        
        
    def SimulationWindow(self,SUVAT,SUVAT2):
        print(SUVAT)
        FormattedTime = SUVAT2[4]
        FormattedTime = FormattedTime*1000
        Distance = SUVAT2[0]
        Distance = ((Distance*10)/10)
        DistanceDec = Distance
        #Image container
        ProjectileScenes = MyView()
        # graphics view
        #Graphics Items
        Image = QPixmap('ball-6x6.png')
        scene = QtGui.QGraphicsScene(self)
        item = QtGui.QGraphicsPixmapItem(Image)
        #first item is 
        scene.addItem(item)
        # Remember to hold the references to QTimeLine and QGraphicsItemAnimation instances.
        # They are not kept anywhere, even if you invoke QTimeLine.start().
        self.TimeLine = QtCore.QTimeLine(FormattedTime)
        self.TimeLine.setFrameRange(0,1)
        self.Animate = QtGui.QGraphicsItemAnimation()
        self.Animate.setItem(item)
        self.Animate.setTimeLine(self.TimeLine)
        # Each method determining an animation state (e.g. setPosAt, setRotationAt etc.)
        # takes as a first argument a step which is a value between 0 (the beginning of the
        # animation) and 1 (the end of the animation)
        self.Animate.setPosAt(0, QtCore.QPointF(0,0))
        self.Animate.setPosAt(0.1, QtCore.QPointF(Distance,-20))
        Distance = Distance+DistanceDec
        self.Animate.setPosAt(0.2, QtCore.QPointF(Distance,-40))
        Distance = Distance+DistanceDec
        self.Animate.setPosAt(0.3, QtCore.QPointF(Distance,-60))
        Distance = Distance+DistanceDec
        self.Animate.setPosAt(0.4, QtCore.QPointF(Distance,-80))
        Distance = Distance+DistanceDec
        self.Animate.setPosAt(0.4, QtCore.QPointF(Distance,-90))
        Distance = Distance+DistanceDec
        self.Animate.setPosAt(0.6, QtCore.QPointF(Distance,-80))
        Distance = Distance+DistanceDec
        self.Animate.setPosAt(0.7, QtCore.QPointF(Distance,-60))
        Distance = Distance+DistanceDec
        self.Animate.setPosAt(0.8, QtCore.QPointF(Distance,-40))
        Distance = Distance+DistanceDec
        self.Animate.setPosAt(0.9, QtCore.QPointF(Distance,-20))
        Distance = Distance+DistanceDec
        self.Animate.setPosAt(1, QtCore.QPointF(Distance,0))
        self.ProjectileView = QtGui.QGraphicsView(scene)
        #Push Buttons
        self.MakeProjectile = QPushButton("Make a projectile")
        self.StartSim = QPushButton("Start Simulating")
        #create grid layout
        self.BottomGridLayout = QGridLayout()
        #add items to grid
        self.BottomGridLayout.addWidget(self.StartSim,1,5)
        #create box layout
        self.SimulationBoxLayout = QVBoxLayout()
        #add grid layout and Label to Box Layout
        self.SimulationBoxLayout.addWidget(self.ProjectileView)
        self.SimulationBoxLayout.addLayout(self.BottomGridLayout)
        #create main Widget
        self.SimulationWidget = QWidget()
        self.SimulationWidget.setLayout(self.SimulationBoxLayout)
        self.setCentralWidget(self.SimulationWidget)
        #connect
        self.StartSim.clicked.connect(self.RunGraphics)

    def RunGraphics(self):
        self.TimeLine.start()
        
    def RunSimulation(self):
        self.SUVATInputLayout()

    def TestingClassWindow(self):
        self.setWindowTitle('Tests')
        #create line edits and labels
        self.TestInput = Q

    def SimulationReset(self):
        Choice = None
        if self.ResetButton.clicked.connect:
            choice = 1
            print("the button works")
        else:
            choice = 2

    def Retry(self):
        print('1')
        
    def TestSelection(self):
        self.setWindowTitle("Test Selection")
        #createMenu and Labels
        TestList = StudentTest.getTests(StudentTest)
        #ComboCox
        self.ComboBoxInput = QComboBox()
        for each in TestList:
            self.ComboBoxInput.addItem(each[0])
        self.DialogLabel = QLabel("Please Select a Test!")
        # GridLayout
        self.GridLayout = QGridLayout()
        self.GridLayout.addWidget(self.DialogLabel,0,0)
        self.GridLayout.addWidget(self.ComboBoxInput,0,1)
        #setMain Widget
        self.TestWidget = QWidget()
        self.TestWidget.setLayout(self.GridLayout)
        self.setCentralWidget(self.TestWidget)
        #return TestList
        self.ComboBoxInput.currentIndexChanged.connect(self.TestComboBox)

    def TestComboBox(self,string):
        Test_Name = ''
        TestList = StudentTest.getTests(StudentTest)
        TestValue = 0
        for i in range(len(TestList)):
            TestList[i]=i
        for each in TestList:
            if each == string:
                TestValue = each
                for i in range(len(TestList)):
                    if i == TestValue:
                        TestList = StudentTest.getTests(StudentTest)
                        Test_Name = TestList[-i][0]
                        Test_Name = str(Test_Name)
                        print(Test_Name,)
        Test_ID = StudentTest.getTestID(StudentTest,Test_Name)
        for i in range(len(Test_ID)):
            Test_ID = Test_ID[-i][0]
            print(Test_ID,'1')
        Questions_ID = StudentTest.RetrieveQuestionsID(self,Test_ID)
        print(Questions_ID)
        QuestionsOriginal = StudentTest.RetrieveQuestions(self,Questions_ID)
        Questions = QuestionsOriginal
        print(Questions)
        for i in range(len(Questions)):
            Questions = [-1][-1]
        Answers = StudentTest.RetrieveAnswers(self,Questions_ID)
        for i in range(len(Answers)):
            Answers = [-1][0]
        CorrectAnswer = Answers
        self.TestResponses(Test_Name,Questions_ID,QuestionsOriginal,Answers,CorrectAnswer)
        
        

    def TestResponses(self,Test_Name,Questions_ID,QuestionsOriginal,Answers,CorrectAnswer):
        print(Test_Name,Questions_ID,QuestionsOriginal,Answers)
        self.setWindowTitle("TestQuestions")
        # Push Buttons
        self.TestRetryButton= QPushButton("Retry?")
        self.SubmitResults = QPushButton("Submit Results")
        #create layouts
        self.BottomGridLayout = QGridLayout()
        self.ButtonBoxLayout = QVBoxLayout()
        #create Line Edits and Labels
        #append items to layout
        self.Question1 = QLabel(QuestionsOriginal[-1][-1])
        self.QuestionResponse1 = QLineEdit()
        self.BottomGridLayout.addWidget(self.Question1,0,0)
        self.BottomGridLayout.addWidget(self.QuestionResponse1,0,1)
        if len(QuestionsOriginal) >1:
            self.Question2 = QLabel(QuestionsOriginal[1])
            self.QuestionResponse2 = QLineEdit()
            self.BottomGridLayout.addWidget(self.Question2,1,0)
            self.BottomGridLayout.addWidget(self.QuestionResponse2,1,1)
        if len(QuestionsOriginal) >2:
            self.Question3 = QLabel(QuestionsOriginal[2])
            self.QuestionResponse3 = QLineEdit()
            self.BottomGridLayout.addWidget(self.Question3,2,0)
            self.BottomGridLayout.addWidget(self.QuestionResponse3,2,1)
        if len(QuestionsOriginal) >3:
            self.Question4 = QLabel(QuestionsOriginal[3])
            self.QuestionResponse4 = QLineEdit()
            self.BottomGridLayout.addWidget(self.Question4,3,0)
            self.BottomGridLayout.addWidget(self.QuestionResponse4,3,1)            
        if len(QuestionsOriginal) >4:
            self.Question5 = QLabel(QuestionsOriginal[4])
            self.QuestionResponse5 = QLineEdit()
        if len(QuestionsOriginal) >5:
            self.Question6 = QLabel(QuestionsOriginal[5])
            self.QuestionResponse6 = QLineEdit()               
            self.BottomGridLayout.addWidget(self.Question5,4,0)
            self.BottomGridLayout.addWidget(self.QuestionResponse5,4,1)
        if len(QuestionsOriginal) >6:
            self.Question7 = QLabel(QuestionsOriginal[6])
            self.QuestionResponse7 = QLineEdit()
            self.BottomGridLayout.addWidgeLinkTestingLayoutt(self.Question6,5,0)
            self.BottomGridLayout.addWidget(self.QuestionResponse6,5,1)               
        if len(QuestionsOriginal) >7:
            self.Question8 = QLabel(QuestionsOriginal[7])
            self.QuestionResponse8 = QLineEdit()
            self.BottomGridLayout.addWidget(self.Question7,6,0)
            self.BottomGridLayout.addWidget(self.QuestionResponse7,6,1)               
        if len(QuestionsOriginal) >8:
            self.Question9 = QLabel(QuestionsOriginal[8])
            self.QuestionResponse9 = QLineEdit()
            self.BottomGridLayout.addWidget(self.Question8,7,0)
            self.BottomGridLayout.addWidget(self.QuestionResponse8,7,1)
        if len(QuestionsOriginal) >9:
            self.Question9 = QLabel(QuestionsOriginal[8])
            self.QuestionResponse9 = QLineEdit()
            self.BottomGridLayout.addWidget(self.Question9,8,0)
            self.BottomGridLayout.addWidget(self.QuestionResponse9,8,1)               
        if len(QuestionsOriginal) >10:
            self.Question10 = QLabel(QuestionsOriginal[9])
            self.QuestionResponse10 = QLineEdit()
            self.BottomGridLayout.addWidget(self.Question10,9,0)
            self.BottomGridLayout.addWidget(self.QuestionResponse10,9,1)
        self.QuestionMessage = QLabel("Answer all of the questions correctly!")
        #QVBoxlayout
        self.ButtonBoxLayout.addWidget(self.TestRetryButton)
        self.ButtonBoxLayout.addWidget(self.SubmitResults)
        #create box layout
        self.QuestionLayout = QVBoxLayout()
        #add grid to aelf.InfoHold(Test_Name,Questions_ID,QuestionsOriginal,Answers)nd label to box layout
        self.QuestionLayout.addWidget(self.QuestionMessage)
        self.QuestionLayout.addLayout(self.BottomGridLayout)
        self.QuestionLayout.addLayout(self.ButtonBoxLayout)
        #create main widget
        self.QuestionWidget = QWidget()
        self.QuestionWidget.setLayout(self.QuestionLayout)
        self.setCentralWidget(self.QuestionWidget)
        #add functions to buttons
        self.TestRetryButton.clicked.connect(self.Retry)
        self.SubmitResults.clicked.connect(self.MarkQuestions)
        self.SubmitResults.clicked.connect(lambda:CorrectAnswer)

    def MarkResponses(self):
        self.ResponseList = []
        try:
            self.QuestionResult = self.QuestionResponse1.text()
            self.ResponseList.append(self.QuestionResult)
        except:
            print()
        try:
            self.QuestionResult1 = self.QuestionResponse2.text()
            self.ResponseList.append(self.QuestionResult1)
        except:
            print()
        try:
            self.QuestionResult2 = self.QuestionResponse3.text()
            self.ResponseList.append(self.QuestionResult2)
        except:
            print()
        try:
            self.QuestionResult3 = self.QuestionResponse4.text()
            self.ResponseList.append(self.QuestionResult3)
        except:
            print()
        try:
            self.QuestionResult4 = self.QuestionResponse5.text()
            self.ResponseList.append(self.QuestionResult4)
        except:
            print()
        try:
            self.QuestionResult5 = self.QuestionResponse6.text()
            self.ResponseList.append(self.QuestionResult5)
        except:
            print()
        try:
            self.QuestionResult6 = self.QuestionResponse7.text()
            self.ResponseList.append(self.QuestionResult6)
        except:
            print()
        try:
            self.QuestionResult7 = self.QuestionResponse8.text()
            self.ResponsCorrectAnswereList.append(self.QuestionResult7)
        except:
            print()
        try:
            self.QuestionResult8 = self.QuestionResponse9.text()
            self.ResponseList.append(self.QuestionResult8)
        except:
            print()
        try:
            self.QuestionResult9 = self.QuestionResponse10.text()
            self.ResponseList.append(self.QuestionResult9)
        except:
            print()
        print(self.ResponseList)
        return self.ResponseList

    def MarkQuestions(self,CorrectAnswer):
        Answers = self.MarkResponses()
        Answered = False
        Score = 1
        TrueScore = 0
        print(CorrectAnswer)
        MaxScore = len(CorrectAnswer)
        while Answered != True:
            for each in Answers:
                for i in range(MaxScore):
                    if each == (CorrectAnswer[i]):
                        TrueScore += 1
                        Score +=1
                        print('Question',i+1,'. was correct')
                        Answered = True
                        i = 0
                    elif each != (CorrectAnswer[i]):
                        print('Question',i+1,'. was wrong')
                        Answered = False
            if Answered == False:            
                Retry = 0
                Retry = input('would you like to retry enter 1 if you would like too!')
                if Retry == '1':
                    for each in Answers:
                        Answers.pop()
                        TrueScore = 0
                        Score = 1
                        Retry = 0
                        i = 0
                        self.Retry(QuestionIDList)
                else:
                    if Answers[0] == Answers:
                        TrueScore += 1
                        Score +=1
                        Answered = True
            if TrueScore == MaxScore:
                Answered = True
        print('You Scored',TrueScore,'out of a total of',MaxScore)
        self.AnswerReview(TrueScore,MaxScore)

    def AnswerReview(self,TrueScore,MaxScore):
        self.setWindowTitle("Answers Review!")
        TrueScore = str(TrueScore)
        MaxScore = str(MaxScore)
        #createMenu and Labels
        self.AnswersTable = QGridLayout()
        self.AnswerLabel1 = QLabel('You Got:')
        self.AnswerLabel2 = QLabel(TrueScore)
        self.AnswerLabel3 = QLabel('out of:')
        self.AnswerLabel4 = QLabel(MaxScore)          
        # GridLayout
        self.AnswersTable.addWidget(self.AnswerLabel1)
        self.AnswersTable.addWidget(self.AnswerLabel2)
        self.AnswersTable.addWidget(self.AnswerLabel3)
        self.AnswersTable.addWidget(self.AnswerLabel4)
        self.AnswersReviewGridLayout = QVBoxLayout()
        self.AnswersReviewGridLayout.addWidget(self.AnswersTable)




        
        #setMain Widget
        self.AnswersReviewWidget = QWidget()
        self.AnswersReviewWidget.setLayout(self.AnswersReviewGridLayout)
        self.setCentralWidget(self.AnswersReviewWidget)
        
        

 


       
        




class MyView(QtGui.QGraphicsView):
    def __init__(self):
         QtGui.QGraphicsView.__init__(self)
         self.Image = QPixmap('rocket.jpg')
         self.scene = QtGui.QGraphicsScene(self)
         self.item = QtGui.QGraphicsPixmapItem(self.Image)
         #first item is 
         self.scene.addItem(self.item)
         self.setScene(self.scene)

         # Remember to hold the references to QTimeLine and QGraphicsItemAnimation instances.
         # They are not kept anywhere, even if you invoke QTimeLine.start().
         self.tl = QtCore.QTimeLine(14000)
         self.tl.setFrameRange(0, 100)
         self.a = QtGui.QGraphicsItemAnimation()
         self.a.setItem(self.item)
         self.a.setTimeLine(self.tl)

         # Each method determining an animation state (e.g. setPosAt, setRotationAt etc.)
         # takes as a first argument a step which is a value between 0 (the beginning of the
         # animation) and 1 (the end of the animation)
         self.a.setPosAt(0, QtCore.QPointF(0, -10))
         self.a.setRotationAt(0.5, 36000)
         self.a.setPosAt(0.9, QtCore.QPointF(-10,100))
         self.a.setPosAt(1, QtCore.QPointF(1000,100))
         self.tl.start()


        
if __name__ == "__main__":
    application = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    MainWindow.raise_()
    application.exec_()

    
