from A2_Physics_Controller_Class import*

class Attempts_Controller(A2_Physics_Controller):
    """ creates a controller in which to add, delete, update Attempts in A2 Physics Database"""

    def __init__(self):
        super().__init__()

    def Add_Attempts(self,Attempt_Score,Time_in_session,Date_of_Use,Test_ID,Student_ID):        
        sql = """insert into Attempts(
                 Attempt_Score,
                 Time_in_session,
                 Date_of_Use,
                 Test_ID,
                 Student_ID)
                 values
                 ('{0}','{1}','{2}','{3}','{4}')""".format(Attempt_Score,Time_in_session,Date_of_Use,Test_ID,Student_ID)
        self._query(sql)
        
    def Delete_Attempts(self,Attempt_ID):
        sql = """ delete from Attempts
                  where Attempt_ID = '{0}'""".format(Attempt_ID)
        self._query(sql)

    def Update_Attempts(self,Attempt_ID,Attempt_Score,Time_in_session,Date_of_Use,Test_ID,Student_ID):
        sql = """ update Attempts
                  set Attempt_Score = '{0}',
                  Time_in_session = '{1}',
                  Date_of_Use = '{2}',
                  Test_ID = '{3}',
                  Student_ID = '{4}'
                  where Attempt_ID = {5}
                  """.format(Attempt_Score,Time_in_session,Date_of_Use,Test_ID,Student_ID,Attempt_ID)
        self._query(sql)

    def Search_Attempts(self,Attempts_ID):
        sql = """ select *
                  from Attempts
                  where Attempt_ID = '{0}'""".format(Attempts_ID)
        results = self._select_query(sql)
        if results == []:
            print('There is no Attempts Type with that ID')
        else:
            print(results)

    def Return_AttemptNoInput(self):
        sql = """ select *
                  from Attempts"""
        results = self._select_query(sql)
        if results == []:
            print('There is no Correct_Attempt Questions with that ID')
        else:
            print(results)
        return results

    def Search_AttemptSTUDENTTEST(self,Attempt_ID):
        DataApproved = False
        sql = """ select Correct_Attempt
                  from Attempts
                  where Attempt_ID = '{0}'""".format(Attempt_ID)
        results = self._select_query(sql)
        while DataApproved != True:
            if results == []:
                print('There is no Attempt with that ID')
            if results[0]== None:
                print('ahh')
            else:
                print('')
                return results

    def Return_AttemptbyID(self,Attempt_ID):
        sql = """ select *
                  from Attempts
                  where Attempt_ID = '{0}'""".format(Attempt_ID)   
        results = self._select_query(sql)
        if results == []:
            print('There is no test with that ID')
        else:
            print('')
        return results
    
    def Return_AttemptbyAttempt(self,Attempt_Score):
        sql = """ select *
                  from Attempts
                  where Attempt_Score = '{0}'""".format(Attempt_Score)   
        results = self._select_query(sql)
        if results == []:
            print('There is no test with that ID')
        else:
            print('')
        return results
            
    def SearchForAttempt(self,SearchItem):
        print('entered the search')
        Search = SearchItem
        IntegerSearch = False
        Attempt = self.Return_AttemptNoInput()
        ItemFound = False
        row = 0 
        column = 0
        MaxItems = len(Attempt)
        for i in range(0,2):
            for each in Attempt:
                Item = Attempt[row][column]
                if Item == Search:
                    ItemFound = True
                if row <= MaxItems:
                    row += 1
                if row == MaxItems:
                    column += 1
                    row = 0
        if ItemFound == True:
            if type(Search) == int:
                print('Integer')
                IntegerSearch = True
                Attempt_ID = Search
                results = self.Return_AttemptbyID(Attempt_ID)
                return results
            else:
                print('String')
                Attempt_Score = Search
                results= self.Return_AttemptbyAttempt(Attempt_Score)
                return results
       # else:
           # print('Hah it did not work')
