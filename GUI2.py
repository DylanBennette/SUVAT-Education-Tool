import Base
import sys
from PyQt4.QtGui import*
from PyQt4.QtGui import*
from PyQt4 import QtGui
from A2_Physics_TestingClass import *
from A2_Physics_Test_Tester import *
from A2_Physics_Propulsion_redone import *

#MainWindow
class MainWindow(QMainWindow):
    #constructor
    def __init__(self):
        #parentconstructor
        super().__init__()
        self.setWindowTitle('MainWindow')
        self.make_menubar()

    def MainWindow(self):
        self.ContinueButton = QPushButton('Continue')
        self.MainWindowButtongroup = QButtonGroup()
        self.RadioButtonNames = ("Go to Simulation","Go to Results")
        self.RadioButtonList = []
        #create and add buttons to list
        for each in range (len(self.RadioButtonNames)):
            self.RadioButtonList.append(QRadioButton(self.RadioButtonNames[each]))
        self.RadioButtonList[0].setChecked(True)
        #Layout
        self.infoRadioButtonLayout = QVBoxLayout()
        #get Pictures
        self.ProjectileScenes = self.getPicturesScene()
        # graphics view
        self.ProjectileView = QtGui.QGraphicsView(self.ProjectileScenes[0])
        #add buttons to layout
        for each in range(len(self.RadioButtonList)):
            #layout
            self.infoRadioButtonLayout.addWidget(self.RadioButtonList[each])
            #controller
            self.MainWindowButtongroup.addButton(self.RadioButtonList[each])
            #add an ID 
            self.MainWindowButtongroup.setId(self.RadioButtonList[each],each)
        #groupBox
        self.infoButtonGroupBox = QGroupBox("please select an action")
        #add radio buttons
        self.infoButtonGroupBox.setLayout(self.infoRadioButtonLayout)
        #create layout
        self.Layout = QVBoxLayout()
        self.Layout.addWidget(self.ProjectileView)
        #add components
        #MainWidget
        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.Layout)
        self.setCentralWidget(self.mainWidget)
        #connect
        self.ContinueButton.clicked.connect(self.MainWindowChoices)

    def MainWindowChoices(self):
        choice = None
        if self.RadioButtonList[0].clicked.connect:
            choice = 1
            self.SimulationWindow()
        else:
            choice = 2
            
    def make_menubar(self):
        """This creates a menu bar on which i can run the entire program """
        #this creates the exit action
        
        exitAction = QtGui.QAction(QtGui.QIcon("exit.png"),"&exit", self)
        exitAction.setShortcut('Ctrl+E+X')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        #this runs the simulation menu

        DisplaySimulation = QtGui.QAction(QtGui.QIcon("Display Simulation.png"),"&Display Simualtion", self)
        DisplaySimulation.setShortcut("Ctrl+S")
        DisplaySimulation.setStatusTip("Displaying Simuation menu")
        DisplaySimulation.triggered.connect(self.SimulationWindow)

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

##        StudentEditor = QtGui.QAction(QtGui.QIcon("Student Editor.png"),"&Student Editor",self)
##        StudentEditor.setShortcut("Ctrl+S")
##        StudentEditor.setStatusTip("Student Editor")
##        StudentEditor.triggered.connect(self.StudentViewWindow)

        QuestionEditor = QtGui.QAction(QtGui.QIcon("Question Editor.png"),"&Question Editor",self)
        QuestionEditor.setShortcut("Ctrl+Q")
        QuestionEditor.setStatusTip("Question Editor")
        QuestionEditor.triggered.connect(self.QuestionViewWindow)

##        AttemptEditor = QtGui.QAction(QtGui.QIcon("Attempt Editor.png"),"&Attempt Editor",self)
##        AttemptEditor.setShortcut("Ctrl+A+T")
##        AttemptEditor.setStatusTip("Attempt Editor")
##        AttemptEditor.triggered.connect(self.AttemptViewWindow)
##        
##        ResponseEditor = QtGui.QAction(QtGui.QIcon("Response Editor.png"),"&Response Editor",self)
##        ResponseEditor.setShortcut("Ctrl+R")
##        ResponseEditor.setStatusTip("Response Editor")
##        ResponseEditor.triggered.connect(self.ResponseViewWindow)
##
##        TypeEditor = QtGui.QAction(QtGui.QIcon("Type Editor.png"),"&Type Editor",self)
##        TypeEditor.setShortcut("Ctrl+T+Y")
##        TypeEditor.setStatusTip("Type Editor")
##        TypeEditor.triggered.connect(self.TypeViewWindow)
##
##        AnswersEditor = QtGui.QAction(QtGui.QIcon("Answers Editor.png"),"&Answers Editor",self)
##        AnswersEditor.setShortcut("Ctrl+A+N")
##        AnswersEditor.setStatusTip("Answers Editor")
##        AnswersEditor.triggered.connect(self.AnswersViewWindow)
        
        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        SimulationMenu = menubar.addMenu("&Simulation")
        QuestionsMenu = menubar.addMenu("&Testing")
        DatabaseMenu = menubar.addMenu("&Editor")
        DatabaseMenu.addAction(TestEditor)
        DatabaseMenu.addAction(QuestionEditor)
        SimulationMenu.addAction(DisplaySimulation)
        QuestionsMenu.addAction(DisplayQuestions)
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("menu bar")
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

            
    def QuestionsMainWindow(self):
        results = Questions_Controller.Questions_Controller.Search_QuestionsNoInput()
        self.setWindowTitle('Questions Editor')
        #create table and push buttons
        self.RecordTable = QTable(results)
        self.AddRecord = QPushButton('Add')
        self.EditRecord = QPushButton('Edit')
        self.DeleteRecord = QPushButton('Delete')
        #create layout
        self.TableBox = QVBoxLayout()
        self.TableBox.addWidget(self.RecordTable)
        #create vertical layout
        self.ButtonLayout = QHBoxLayout()
        self.ButtonLayout.addWidget(self.AddRecord)
        self.ButtonLayout.addWidget(self.EditRecord)
        self.ButtonLayout.addWidget(self.DeleteRecord)
        #Final Layout
        self.QuestionsLayout = QWidget()
        self.QuestionsLayout.addLayout(self.TableBox)
        self.QuestionsLayout.addLayout(self.ButtonLayout)
        self.setCentralWidget(self.QuestionsLayout)
        #connect
        self.AddRecord.clicked.connect(self.AddQuestionDialog)
        self.EditRecord.clicked.connect(self.EditQuestionDialog)
        self.DeleteRecord.clicked.connect(self.DeleteRecord)
        
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
        self.QuestionIDinfo = QLineEdit()
        self.Questioninfo = QLineEdit()
        self.Type_IDinfo = QLineEdit()
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
        Question_ID = self.Questioninfo.textEdited()
        Question = self.Type_IDinfo.textEdited()
        Type_ID = self.Type_IDinfo.textEdited()
        return Question_ID,Question,Type_ID
        self.SubmitChanges.clicked.connect(UpdateQuestion)

    def UpdateQuestion(self,Question_ID,Question,Type_ID):
        self.Questions_Controller.Update_Question()
        
    def DeleteQuestionDialog(self):
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
        Question = Questions_Controller()
        Question.Update_Question(Question,Question_Type,Question_ID)
        
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


    def getPicturesScene(self):
        Projectile = QtGui.QPixmap('rocket.jpg')
        ProjectileExpended  = QtGui.QPixmap('ronvanderende2005pod.jpg')
        ProjectileList = [Projectile,ProjectileExpended]
        Projectileitem = []
        ProjectileScene = []
        for each in ProjectileList:
            ProjectileScene.append(QGraphicsScene())
            ProjectileScene[-1].addPixmap(each)
        for each in Projectileitem:
            Projectileitem.append(QtGui.QVector2D(400,600))
            Projectileitem.QVector2D.setX(200)
            Projectileitem.QVector2D.setY(-200)
        return ProjectileScene

    def SUVATInputs(self):
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
        if Displacement == '':
            Displacement = 0
        InitialVelocity = self.InitialvelocityLineEdit.text()
        if InitialVelocity == '':
            InitialVelocity = 0
        FinalVelocity = self.FinalLineEdit.text()
        if FinalVelocity == '':
            FinalVelocity = 0
        Acceleration = self.AccelerationLineEdit.text()
        if Acceleration == '':
            Acceleration = 0
        Time = self.TimeLineEdit.text()
        if Time == '':
            Time = 0
        InputList = [Displacement,InitialVelocity,FinalVelocity,Acceleration,Time]
        Propulsion1 = Propulsion('Spaceship',0,0,0,45,InitialVelocity,FinalVelocity,Acceleration,Displacement,Time,-9.81)
        PreSimulationResults = Propulsion1.SUVATInputs(InputList)
        Propulsion1.SUVATLink(PreSimulationResults)
        print(PreSimulationResults,'results')
        
    def SimulationWindow(self):
        QGraphicsPixmapVector1 = QGraphicsPixmapVector()
        #Image container
        print(QGraphicsPixmapVector1)
        self.ProjectileScenes = self.getPicturesScene()
        # graphics view
        self.ProjectileView = QtGui.QGraphicsView(self.ProjectileScenes[0])
        #Push Buttons
        self.ResetButton = QPushButton("ResetSimulation")
        self.MakeProjectile = QPushButton("Make a projectile")
        self.StartSim = QPushButton("Start Simulating")
        #create grid layout
        self.BottomGridLayout = QGridLayout()
        #add items to grid
        self.BottomGridLayout.addWidget(self.ResetButton,0,5)
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
        self.ResetButton.clicked.connect(self.SimulationReset)
        self.StartSim.clicked.connect(self.RunSimulation)
        

    def RunSimulation(self):
        self.SUVATInputs()
        PreSimulationResults = self.SimulationPrep()
        print(PreSimulationResults)
        print('out of loop')
        #self.SimulationWindow()
        
        
        

        

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
    def ProjectileCreator(self):
        #this will allow the user to create their own projectile
        print("Hello Programmers")

    def Retry(self):
        print('1')
        
    def SelectTestDialogBox(self,TestList):
        #Actions
        TestList = self.StudentTest.getTests()
        self.TestInput = QMenu(TestList)
        self.ConfirmAction = QPushButton("Confirm")
        self.DialogLabel = QLabel("Please Select a Test!")
        #button layout
        self.ActionBox = QGridLayout()
        self.ActionBox.addWidget(self.TestInput,0,0)
        self.ActionBox.addWidget(self.CancelAction,0,1)
        #main layout
        self.QDialogButtonBox.addWidget(self.DialogLabel)
        self.QDialogButtonBox.addLayout(self.ActionBox)
        
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
        self.InfoHold(Test_Name,Questions_ID,QuestionsOriginal,Answers)
        self.TestResponses(Test_Name,Questions_ID,QuestionsOriginal,Answers)
        

    def TestResponses(self,Test_Name,Questions_ID,QuestionsOriginal,Answers):
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
        #add grid to and label to box layout
        self.QuestionLayout.addWidget(self.QuestionMessage)
        self.QuestionLayout.addLayout(self.BottomGridLayout)
        self.QuestionLayout.addLayout(self.ButtonBoxLayout)
        #create main widget
        self.QuestionWidget = QWidget()
        self.QuestionWidget.setLayout(self.QuestionLayout)
        self.setCentralWidget(self.QuestionWidget)
        #add functions to buttons
        self.TestRetryButton.clicked.connect(self.Retry)
        self.SubmitResults.clicked.connect(self.MarkResponses)

    def InfoHold(self,Test_Name,Questions_ID,QuestionsOriginal,Answers):
        Test_NameItem = Test_Name
        Questions_IDItem = Questions_ID
        QuestionsOriginalItem = QuestionsOriginal
        AnswersItem = Answers
        return Test_NameItem,Questions_IDItem,QuestionsOriginalItem,AnswersItem

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
            self.ResponseList.append(self.QuestionResult7)
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
        self.SubmitResponses(self.ResponseList)
        NoofQuestions = len(ResponseList)
        Info = self.InfoHold()
        print('here')
        if NoofQuestions == ResponseList:
            for each in ResponseList:
                ResponseCont = Response_Controller()
                ResponseCont.add
        self.AnswersResponse(Test_Name,Questions_ID,QuestionsOriginal,Answers)



       
        








##        
##
##        def getPicturesScene(self):
##        Projectile = QtGui.QPixmap('rocket.jpg')
##        ProjectileExpended  = QtGui.QPixmap('ronvanderende2005pod.jpg')
##        ProjectileList = [Projectile,ProjectileExpended]
##        Projectileitem = []
##        ProjectileScene = []
##        for each in ProjectileList:
##            ProjectileScene.append(QtGui.QGraphicsScene())
##            ProjectileScene[-1].addPixmap(each)
##        for each in Projectileitem:
##            Projectileitem.append(QtGui.QVector2D(400,600))
##            Projectileitem.QVector2D.setX(200)
##            Projectileitem.QVector2D.setY(-200)
##        return ProjectileScene



        
if __name__ == "__main__":
    application = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    MainWindow.raise_()
    application.exec_()

    
