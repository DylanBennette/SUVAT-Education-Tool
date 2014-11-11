def create_student(db,cursor):
    sql = """create table Student (
             Student_ID integer,
             First_Name text,
             Last_Name text,
             primary key (Student_ID))"""
    
    cursor.execute(sql)
    db.commit()
             
def create_attempt(db,cursor):
    sql = """create table Attempts (
             Attempt_ID integer,
             Time_in_session datetime,
             Date_of_Use datetime,
             Attempt_Score integer,
             Test_ID integer,
             Student_ID integer,
             primary key (Attempt_ID),
             foreign key (Test_ID) references Tests(Test_ID),
             foreign key (Student_ID)references Students(Student_ID))"""

    cursor.execute(sql)
    db.commit()
    
def create_test(db,cursor):
    sql = """create table Tests (
             Test_ID integer,
             Test_Name text,
             primary key (Test_ID))"""
    
    cursor.execute(sql)
    db.commit()
    
def create_questions(db,cursor):
    sql = """create table Questions (
             Questions_ID integer,
             Question text,
             Type_ID integer,
             primary key(Questions_ID),
             foreign key(Type_ID) references Type(Type_ID))"""

    cursor.execute(sql)
    db.commit()
    
def create_type(db,cursor):
    sql = """create table Type (
             Type_ID integer,
             Question_Type text,
             primary key (Type_ID))"""

    cursor.execute(sql)
    db.commit()
    
def create_testquestions(db,cursor):
    sql = """create table TestQuestions (
             TestQuestions_ID integer,
             Questions_ID integer,
             Test_ID integer,
             primary key(TestQuestions_ID),
             foreign key (Questions_ID) references Questions(Questions_ID),
             foreign key (Test_ID) references Tests(Test_ID))"""

    cursor.execute(sql)
    db.commit()
    
def create_answer(db,cursor):
    sql = """create table Answers (
             Answer_ID integer,
             Correct_Answer text,
             Questions_ID integer,
             primary key(Answer_ID)
             foreign key(Questions_ID) references Questions(Questions_ID))"""

    cursor.execute(sql)
    db.commit()
    
def create_Responses(db,cursor):
    sql = """create table Responses (
             Response_ID integer,
             Questions_ID integer,
             Attempt_ID integer,
             Student_Response text,
             primary key (Response_ID),
             foreign key(Questions_ID) references Questions(Questions_ID)
             foreign key(Attempt_ID) references Attempts(Attempt_ID))"""

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
