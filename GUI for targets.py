import Base
import sys
from PyQt4.QtGui import*
from PyQt4.QtGui import*
from PyQt4 import QtGui
from A2_Physics_TestingClass import *



#MainWindow
class MainWindow(QMainWindow):
    #constructor
    def __init__(self):
        #parentconstructor
        super().__init__()
        self.setWindowTitle('MainWindow')
        self.make_menubar()

##    def CLIMainWindow(self):
##        self.WelcomeMessage = QLabel('Welcome to the AS Physics Simulation')
##        self.Help = QTextBlock('Please select an item the Simulation, where you can calculate SUVAT and view simulations.\nTo attempt a test chose the Test button.\nOr if you want to see how other people have done you can use the results editor.')
##        self.SimulationButton = QPushButton('Simulations')
##        self.TestButton = QPushButton('Tests')
##        self.DataBaseEditor = QPushButton('Results')
##        #Add elements to Layout
##        self.MessageLayout = QVBoxLayout()
##        self.MessageLayout.addWidget(self.WelcomeMessage)
##        self.MessageLayout.addWidget(self.Help)
##        #Add button Layout
##        self.ButtonLayout = QHBoxLayout()
##        self.ButtonLayout.addWidget(self.SimulationButton)
##        self.ButtonLayout.addWidget(self.TestButton)
##        self.ButtonLayout.addWidget(self.DataBaseEditor)
##        #Add H Box to V Box
##        self.MainLayout = QWidget()
##        self.MainLayout.setLayout(self.MessageLayout)
##        self.MainLayout.setLayout(self.ButtonLayout)
##        self.setCentralWidget(self.mainWidget)
##        # Connect
##        self.SimulationButton.clicked.connect(self.
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
        #add components
        self.Layout.addWidget(self.infoButtonGroupBox)
        self.Layout.addWidget(self.ContinueButton)
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

        DisplayEditor = QtGui.QAction(QtGui.QIcon("Database editor.png"),"&Database Editor", self)
        DisplayEditor.setShortcut("Ctrl+D")
        DisplayEditor.setStatusTip("Database Editor")
        DisplayEditor.triggered.connect(self.TestViewWindow)

        
        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        SimulationMenu = menubar.addMenu("&Simulation")
        QuestionsMenu = menubar.addMenu("&Testing")
        DatabaseMenu = menubar.addMenu("&Editor")
        DatabaseMenu.addAction(DisplayEditor)
        SimulationMenu.addAction(DisplaySimulation)
        QuestionsMenu.addAction(DisplayQuestions)
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("menu bar")
        self.show()

##    def DatabaseEditorMenuBar(self):
##        """This creates a menu bar on which i can run the entire program """
##        #this creates the exit action
##        exitAction = QtGui.QAction(QtGui.QIcon("exit.png"),"&exit",self)
##        exitAction.setShortcut('Ctrl+E+X')
##        exitAction.setStatusTip('Exit application')
##        exitAction.triggered.connect(self.close)
##                                           
##        #This allows you to View the database editor
##
##        DisplayEditor = QtGui.QAction(QtGui.QIcon("Database editor.png"),"&Display Database Editor", self)
##        DisplayEditor.setShortcut("Ctrl+D")
##        DisplayEditor.setStatusTip("Database Editor")
##        DisplayEditor.triggered.connect(self.TestViewWindow)
##        
##        self.statusBar()
##        menubar = self.menuBar()
##        DatabaseMenu = menubar.addMenu("&Editor")
##        DatabaseMenu.addAction(DisplayEditor)
##        self.setGeometry(300, 300, 300, 200)
##        self.setWindowTitle("menu bar")
##        self.show()
        
    def TestViewWindow(self):
        test = Test_Controller()
        results = test.Return_TestsNoInput()
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
                #print(item)
                self.RecordTable.setItem(row,column,item)
                if row <= Maxrows:
                    row +=1
                    if row == Maxrows:
                        column +=1
                        row = 0
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
        self.AddQuestionLayout = QGridLayout()
        self.AddQuestionLayout.addWidget(self.TestLabel,0,0)
        self.AddQuestionLayout.addWidget(self.TestName,1,0)
        self.AddQuestionLayout.addWidget(self.SubmitChanges,2,0)
        self.FinalLayout = QVBoxLayout()
        self.FinalLayout.addLayout(self.TableLayout)
        self.FinalLayout.addLayout(self.AddQuestionLayout)
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
        try:
            Test_ID = self.TestIDinfo.text()
            test = Test_Controller()
            test.Delete_Test(Test_ID)
        except:
        
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
        
    def AddQuestionDialog(self):
        Dialog.setObjectName("Dialog")
        Dialog.resize(508, 300)
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
        self.AddQuestion = QDialog
        #something about result of line edit etc
        Question = self.Questioninfo.textEdited()
        Type_ID = self.Type_IDinfo.textEdited()
        return Question,Type_ID
        self.SubmitChanges.clicked.connect(AddQuestion)
        
    def AddQuestion(self,Question,Type_ID):
        self.Questions_Controller.Add_Question()
        
    def EditQuestionDialog(self):
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
        
    def SimulationWindow(self):
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
        #Push Buttons
        self.ResetButton = QPushButton("ResetSimulation")
        self.MakeProjectile = QPushButton("Make a projectile")
        self.StartSim = QPushButton("Start Simulating")
        #create grid layout
        self.BottomGridLayout = QGridLayout()
        #add items to grid
        self.BottomGridLayout.addWidget(self.DisplacementLabel,0,0)
        self.BottomGridLayout.addWidget(self.DisplacementLineEdit,1,0)
        self.BottomGridLayout.addWidget(self.InitialvelocityLabel,0,1)
        self.BottomGridLayout.addWidget(self.InitialvelocityLineEdit,1,1)
        self.BottomGridLayout.addWidget(self.FinalLabel,0,2)
        self.BottomGridLayout.addWidget(self.FinalLineEdit,1,2)
        self.BottomGridLayout.addWidget(self.AccelerationLabel,0,3)
        self.BottomGridLayout.addWidget(self.AccelerationLineEdit,1,3)
        self.BottomGridLayout.addWidget(self.TimeLabel,0,4)
        self.BottomGridLayout.addWidget(self.TimeLineEdit,1,4)
        self.BottomGridLayout.addWidget(self.ResetButton,0,5)
        self.BottomGridLayout.addWidget(self.StartSim,1,5)
        self.BottomGridLayout.addWidget(self.MakeProjectile,0,6)
        #create box layout
        self.SimulationBoxLayout = QVBoxLayout()
        #add grid layout and Label to Box Layout
        self.SimulationBoxLayout.addWidget(self.SimulationMessage)
        self.SimulationBoxLayout.addLayout(self.BottomGridLayout)
        #create main Widget
        self.SimulationWidget = QWidget()
        self.SimulationWidget.setLayout(self.SimulationBoxLayout)
        self.setCentralWidget(self.SimulationWidget)
        #connect
        self.ResetButton.clicked.connect(self.SimulationReset)
        self.StartQuestions.clicked.connect(self.SimulationQuestions)
        self.MakeProjectile.clicked.connect(self.ProjectileCreator)
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
        StudentTest.MarkQuestions(StudentTest,None,None,1)
        
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
        Questions = StudentTest.RetrieveQuestions(self,Questions_ID)
        print(Questions)
        for i in range(len(Questions)):
            Questions = [-1][-1]
        Answers = StudentTest.RetrieveAnswers(self,Questions_ID)
        for i in range(len(Answers)):
            Answers = [-1][0]
        print(Answers)
        self.TestQuestions(Questions,Answers,Questions_ID,Test_Name)

    def TestQuestions(self,Questions,Answers,Questions_ID,Test_Name):
        ResponseList = []
        self.setWindowTitle("TestQuestions")
        #create Line Edits and Labels
        for each in Questions_ID:
            Question = QLabel(Questions[each])
        self.QuestionMessage = QLabel("Answer all of the questions correctly!")
        # Push Buttons
        self.TestRetryButton= QPushButton("Retry?")
        self.SubmitResults = QPushButton("Submit Results")
        #create layouts
        self.BottomGridLayout = QGridLayout()
        self.ButtonBoxLayout = QVBoxLayout()
        #append items to layout
        self.BottomGridLayout.addWidget(self.Question1,0,0)
        self.BottomGridLayout.addWidget(self.QuestionAnswer1,0,1)
        self.BottomGridLayout.addWidget(self.Question2,1,0)
        self.BottomGridLayout.addWidget(self.QuestionAnswer2,1,1)
        self.BottomGridLayout.addWidget(self.Question3,2,0)
        self.BottomGridLayout.addWidget(self.QuestionAnswer3,2,1)
        self.BottomGridLayout.addWidget(self.Question4,3,0)
        self.BottomGridLayout.addWidget(self.QuestionAnswer4,3,1)
        self.BottomGridLayout.addWidget(self.Question5,4,0)
        self.BottomGridLayout.addWidget(self.QuestionAnswer5,4,1)
        self.BottomGridLayout.addWidget(self.Question6,5,0)
        self.BottomGridLayout.addWidget(self.QuestionAnswer6,5,1)
        self.BottomGridLayout.addWidget(self.Question7,6,0)
        self.BottomGridLayout.addWidget(self.QuestionAnswer7,6,1)
        self.BottomGridLayout.addWidget(self.Question8,7,0)
        self.BottomGridLayout.addWidget(self.QuestionAnswer8,7,1)
        self.BottomGridLayout.addWidget(self.Question9,8,0)
        self.BottomGridLayout.addWidget(self.QuestionAnswer9,8,1)
        self.BottomGridLayout.addWidget(self.Question10,9,0)
        self.BottomGridLayout.addWidget(self.QuestionAnswer10,9,1)
        #QVBoxlayout
        self.ButtonBoxLayout.addWidget(self.DisplayHints)
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
        self.DisplayHints.clicked.connect(self.DisplayHints)
        self.SubmitResults.clicked.connect(self.SubmitResults)
       
        







        
if __name__ == "__main__":
    
    application = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    MainWindow.raise_()
    application.exec_()
