from A2_Physics_Controller_Class import*

class Student_Controller(A2_Physics_Controller):
    """ creates a controller in which to add, delete, update students records in A2 Physics Database"""

    def __init__(self):
        super().__init__()

    def Add_Student(self,FirstName,LastName):
        sql ="""insert into Student(
                First_Name,
                Last_Name)
                Values
                ('{0}','{1}')""".format(FirstName,LastName)
        self._query(sql)

    def Delete_Student(self,Student_ID):
        sql = """ delete from Student
                  where Student_ID = '{0}'""".format(Student_ID)
        self._query(sql)

    def Update_Student(self,FirstName,LastName,Student_ID):  
        sql = """ update Student
                  set First_Name = '{0}',
                  Last_Name = '{1}'
                  where Student_ID = {2}
                  """.format(FirstName,LastName,Student_ID)
        self._query(sql)

    def Search_Student(self,Student_ID):
        sql = """ select *
                  from Student
                  where Student_ID = '{0}'""".format(Student_ID)
        results = self._select_query(sql)
        if results == []:
            print('There is no student with that ID')
        else:
            print(results)

    def Return_StudentNoInput(self):
        sql = """ select *
                  from Student"""
        results = self._select_query(sql)
        if results == []:
            print('There is no Student with that ID')
        else:
            print(results)
        return results

    def Search_StudentSTUDENTTEST(self,Student_ID):
        DataApproved = False
        sql = """ select Student
                  from Student
                  where Student_ID = '{0}'""".format(Student_ID)
        results = self._select_query(sql)
        while DataApproved != True:
            if results == []:
                print('There is no Student with that ID')
            if results[0]== None:
                print('ahh')
            else:
                print('')
                return results

    def Return_StudentbyID(self,Student_ID):
        sql = """ select *
                  from Student
                  where Student_ID = '{0}'""".format(Student_ID)   
        results = self._select_query(sql)
        if results == []:
            print('There is no Student with that ID')
        else:
            print('')
        return results

    def Return_StudentbyStudent(self,First_Name):
        sql = """ select *
                  from Student
                  where First_Name = '{0}'""".format(First_Name)   
        results = self._select_query(sql)
        if results == []:
            print('There is no Student with that ID')
        else:
            print('')
        return results
            
    def SearchForStudent(self,SearchItem):
        print('entered the search')
        Search = SearchItem
        IntegerSearch = False
        StudentInfo = self.Return_StudentNoInput()
        ItemFound = False
        row = 0 
        column = 0
        MaxItems = len(StudentInfo)
        for i in range(0,2):
            for each in StudentInfo:
                Item = StudentInfo[row][column]
                if Item == Search:
                    ItemFound = True
                if row <= MaxItems:
                    row += 1
                if row == MaxItems:
                    column += 1
                    row = 0
        if ItemFound == True:      
            print(ItemFound)
        if ItemFound == True:
            if type(Search) == int:
                print('Integer')
                IntegerSearch = True
                Student_ID = Search
                results = self.Return_StudentbyID(Student_ID)
                return results
            else:
                print('String')
                Student = Search
                results = self.Return_StudentbyStudent(Student)
                return results
        else:
            print('Hah it did not work')
