def create_student(db,cursor):
    sql = """create table Student (
             Student_ID integer NOT NULL,
             First_Name text NOT NULL,
             Last_Name text NOT NULL,
             primary key (Student_ID))"""
    cursor.execute(sql)
    db.commit()
             
def create_attempt(db,cursor):
    sql = """create table Attempts (
             Attempt_ID integer NOT NULL,
             Time_in_session datetime NOT NULL,
             Date_of_Use datetime NOT NULL,
             Attempt_Score integer NOT NULL,
             Test_ID integer NOT NULL,
             Student_ID integer NOT NULL,
             primary key (Attempt_ID) ,
             foreign key (Test_ID) references Tests (Test_ID) ON UPDATE CASCADE ON DELETE RESTRICT,
             foreign key (Student_ID) references Student(Student_ID) ON UPDATE CASCADE ON DELETE RESTRICT)"""
    cursor.execute(sql)
    db.commit()
    
def create_test(db,cursor):
    sql = """create table Tests (
             Test_ID integer NOT NULL,
             Test_Name text NOT NULL,
             primary key (Test_ID))"""
    
    cursor.execute(sql)
    db.commit()
    
def create_questions(db,cursor):
    sql = """create table Questions (
             Questions_ID integer NOT NULL,
             Question text NOT NULL,
             Type_ID integer NOT NULL,
             primary key(Questions_ID),
             foreign key(Type_ID) references Type(Type_ID) ON UPDATE CASCADE ON DELETE RESTRICT)"""

    cursor.execute(sql)
    db.commit()
    
def create_type(db,cursor):
    sql = """create table Type (
             Type_ID integer NOT NULL,
             Question_Type text NOT NULL,
             primary key (Type_ID))"""

    cursor.execute(sql)
    db.commit()
    
def create_testquestions(db,cursor):
    sql = """create table TestQuestions (
             TestQuestions_ID integer NOT NULL,
             Questions_ID integer NOT NULL,
             Test_ID integer NOT NULL,
             primary key(TestQuestions_ID),
             foreign key (Questions_ID) references Questions(Questions_ID) ON UPDATE CASCADE ON DELETE RESTRICT,
             foreign key (Test_ID) references Tests(Test_ID) ON UPDATE CASCADE ON DELETE RESTRICT)"""

    cursor.execute(sql)
    db.commit()
    
def create_answer(db,cursor):
    sql = """create table Answers (
             Answer_ID integer NOT NULL,
             Correct_Answer text NOT NULL,
             Questions_ID integer NOT NULL,
             primary key(Answer_ID)
             foreign key(Questions_ID) references Questions(Questions_ID) ON UPDATE CASCADE ON DELETE RESTRICT)"""

    cursor.execute(sql)
    db.commit()
    
def create_Responses(db,cursor):
    sql = """create table Responses (
             Response_ID integer NOT NULL,
             Questions_ID integer NOT NULL,
             Attempt_ID integer NOT NULL,
             Student_Response text NOT NULL,
             primary key (Response_ID),
             foreign key(Questions_ID) references Questions(Questions_ID) ON UPDATE CASCADE ON DELETE RESTRICT,
             foreign key(Attempt_ID) references Attempts(Attempt_ID) ON UPDATE CASCADE ON DELETE RESTRICT)"""

    cursor.execute(sql)
    db.commit()
    
if __name__ == '__main__':
    
    import sqlite3

    db = sqlite3.connect("A2PhysicsSimulation")
    cursor = db.cursor()
    create_student(db,cursor)
    create_attempt(db,cursor)
    create_test(db,cursor)
    create_questions(db,cursor)
    create_type(db,cursor)
    create_testquestions(db,cursor)
    create_answer(db,cursor)
    create_Responses(db,cursor)
