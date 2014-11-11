import Base
import sys

from PyQt4.QtGui import*
from PyQt4.QtGui import*
from PyQt4 import QtGui

#MainWindow
class MainWindow(QMainWindow):
    #constructor
    def __init__(self):
        #parentconstructor
        super().__init__()
        self.setWindowTitle('MainWindow')
        self.make_menu()


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
            
    def make_menu(self):
        """This creates a menu bar on which i can run the entire program """
        #this creates the exit action
        
        exitAction = QtGui.QAction(QtGui.QIcon("exit.png"),"&exit", self)
        exitAction.setShortcut('Ctrl+Q+W+E+R+T+Y')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        #this runs the simulation menu

        DisplaySimulation = QtGui.QAction(QtGui.QIcon("Display Simulation.png"),"&Display Simualtion", self)
        DisplaySimulation.setShortcut("Ctrl+S")
        DisplaySimulation.setStatusTip("Displaying Simuation menu")
        DisplaySimulation.triggered.connect(self.SimulationWindow)

        #this runs the Questions Menu

        DisplayQuestions = QtGui.QAction(QtGui.QIcon("Display Questions.png"),"&Display Questions", self)
        DisplayQuestions.setShortcut("Ctrl+Q")
        DisplayQuestions.setStatusTip("Dislaying Questions Menu")
        DisplayQuestions.triggered.connect(self.SimulationQuestions)

        #this allows you to logout

        DisplayPlayerName = Qt.QAction(QtGui.QIcon("Display Questions.png"),"&Hello", self)
        DisplayPlayerName.setShortcut("Ctrl+P")
        DisplayPlayerName.setStatusTip("Dialog box for logging out")
        DisplayPlayerName.triggered.connect(self.StudentLogout)
                                           
        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        SimulationMenu = menubar.addMenu("&Simulation")
        SimulationMenu.addAction(DisplaySimulation)
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("menu bar")
        self.show()

    def TestMainWindow(self):
        test = Test_Controller()
        results = test.Search_TestNoInput()
        self.setWindowTitle('Questions Editor')
        #create table and push buttons
        self.RecordTable = QTable(results)
        self.AddTest = QPushButton('Add')
        self.EditTest = QPushButton('Edit')
        self.DeleteTest = QPushButton('Delete')
        #create layout
        self.TableBox = QVBoxLayout()
        self.TableBox.addWidget(self.RecordTable)
        #create vertical layout
        self.ButtonLayout = QHBoxLayout()
        self.ButtonLayout.addWidget(self.AddTest)
        self.ButtonLayout.addWidget(self.EditTest)
        self.ButtonLayout.addWidget(self.DeleteTest)
        #Final Layout
        self.TestLayout = QWidget()
        self.TestLayout.addLayout(self.TableBox)
        self.TestLayout.addLayout(self.ButtonLayout)
        self.setCentralWidget(self.TestLayout)
        #connect
        self.AddTest.clicked.connect(self.AddQuestionDialog)
        self.EditTest.clicked.connect(self.EditQuestionDialog)

    def AddTestDialog(self):
        Dialog.setObjectName("Dialog")
        Dialog.resize(508, 300)
        results = Test_Controller.Return_TestsNoInput()
        self.setWindowTitle('Questions Editor')
        #create table and push buttons
        self.RecordTable = QTable(results)
        self.TestLabel = QLabel('Enter an appropriate Test here!')
        self.Testinfo = QLineEdit('')
        self.SubmitChanges = QPushButton()
        #create layout
        self.AddQuestionLayout = QGridLayout()
        self.AddQuestionLayout.addWidget(self.TestLabel,0,0)
        self.AddQuestionLayout.addWidget(self.Testinfo,1,0)
        self.AddQuestionLayout.addWidget(self.SubmitChanges,2,0)
        self.AddQuestion = QDialog
        #something about result of line edit etc
        Test_Name = self.Testinfo.textEdited()
        return Test_Name
        self.SubmitChanges.clicked.connect(AddTest)
        
    def AddTest(self,Test_Name):
        self.Test_Controller.Add_Test(Test_Name)
        
    def EditQuestionDialog(self):
        results = Test_Controller.Search_TestNoInput()
        self.setWindowTitle('Test Editor')
        #create table and push buttons
        self.RecordTable = QTable(results)
        self.Test_IDLabel = QLabel('enter an appropriate Test ID')
        self.Test_NameLabel = QLabel('Enter an appropriate Test')
        self.Test_ID = QLineEdit()
        self.Testinfo = QLineEdit()
        self.SubmitChanges = QPushButton()
        #create layout for labels and line edits
        self.InputLayout = QGridLayout
        self.InputLayout.addWidget(self.Test_IDLabel,0,0)
        self.InputLayout.addWidget(self.Test_NameLabel,0,1)
        self.InputLayout.addWidget(self.Test_NameLabel,1,1)
        self.InputLayout.addWidget(self.Testinfo,2,0)
        self.InputLayout.addWidget(self.SubmitChanges,2,2)
        #mainWidget
        self.QuestionLayout =QVBoxLayout()
        self.QuestionLayout.addLayout(self.RecordTable)
        self.QuestionLayout.addLayout(self.InputLayout)
        self.EditQuestion = QWidget()
        self.EditQuestion.addLayout(QuestionLayout)
        self.setCentralWidget(self.CentralWidget)
        #connections
        Test_ID = self.Testinfo.textEdited()
        Test_Name = self.Testinfo.textEdited()
        return Test_ID,Test_Name
        self.SubmitChanges.clicked.connect(UpdateTest)

    def UpdateTest(self,Test_ID,Test_Name):
        self.Test_Controller.Update_Test(Test_ID,Test_Name)
        
    def DeleteQuestionDialog(self):
        results = Test_Controller.Search_TestNoInput()
        self.setWindowTitle('Questions Editor')
        #create table and push buttons
        self.RecordTable = QTable(results)
        self.TestIDLabel = QLabel('enter an appropriate Test ID')
        self.TestIDinfo = QLineEdit()
        self.SubmitChanges = QPushButton()
        #create layout for labels and line edits
        self.InputLayout = QGridLayout
        self.InputLayout.addWidget(self.QuestionIDLabel,0,0)
        self.InputLayout.addWidget(self.TestIDinfo,0,1)
        self.InputLayout.addWidget(self.SubmitChanges,1,0)
        #mainWidget
        self.QuestionLayout =QVBoxLayout()
        self.QuestionLayout.addLayout(self.RecordTable)
        self.QuestionLayout.addLayout(self.InputLayout)
        self.EditQuestion = QWidget()
        self.EditQuestion.addLayout(QuestionLayout)
        self.setCentralWidget(self.CentralWidget)
        #connections
        Test_ID = self.TestIDinfo.textEdited()
        return Test_ID
        self.SubmitChanges.clicked.connect(DeleteQuestion)
        
    def DeleteQuestion(self,Test_ID):
        self.Test_Controller.Delete_Test()
        
    def QuestionsMainWindow(self):
        results = Questions_Controller.Search_QuestionsNoInput()
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
        results = Questions_Controller.Search_QuestionsNoInput()
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
        results = Questions_Controller.Search_QuestionsNoInput()
        self.setWindowTitle('Questions Editor')
        #create table and push buttons
        self.RecordTable = QTable(results)
        self.QuestionIDLabel = QLabel('enter an appropriate Question ID')
        self.QuestionLabel = QLabel('Enter an appropriate Question')
        self.Type_IDLabel  = QLabel('Question Type ID')
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
        results = Questions_Controller.Search_QuestionsNoInput()
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

    def SimulationQuestions(self):
        self.setWindowTitle("TestQuestions")
        #create Line Edits and Labels
        self.Question1 = QLabel("Question1")
        self.QuestionAnswer1 = QLineEdit()
        self.Question2 = QLabel("Question2")
        self.QuestionAnswer2 = QLineEdit()
        self.Question3 = QLabel("Question3")
        self.QuestionAnswer3 = QLineEdit()
        self.Question4 = QLabel("Question4")
        self.QuestionAnswer4 = QLineEdit()
        self.Question5 = QLabel("Question5")
        self.QuestionAnswer5 = QLineEdit()
        self.Question6 = QLabel("Question6")
        self.QuestionAnswer6 = QLineEdit()
        self.Question7 = QLabel("Question7")
        self.QuestionAnswer7 = QLineEdit()
        self.Question8 = QLabel("Question8")
        self.QuestionAnswer8 = QLineEdit()
        self.Question9 = QLabel("Question9")
        self.QuestionAnswer9 = QLineEdit()
        self.Question10 = QLabel("Question10")
        self.QuestionAnswer10 = QLineEdit()
        self.QuestionMessage = QLabel("Answer all of the questions correctly!")
        # Push Buttons
        self.DisplayHints = QPushButton("Display Hints")
        self.SubmitResults = QPushButton("Submit Results")
        #create layouts
        self.BottomGridLayout = QGridLayout()
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
        #create box layout
        self.QuestionLayout = QVBoxLayout()
        #add grid to and label to box layout
        self.QuestionLayout.addWidget(self.QuestionMessage)
        self.QuestionLayout.addLayout(self.BottomGridLayout)
        #create main widget
        self.QuestionWidget = QWidget()
        self.QuestionWidget.setLayout(self.QuestionLayout)
        self.setCentralWidget(self.QuestionWidget)
       
        







        
if __name__ == "__main__":
    
    application = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    MainWindow.raise_()
    application.exec_()
