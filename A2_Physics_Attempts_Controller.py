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
                  Attempt_ID = '{1}',
                  Time_in_session = '{2}',
                  Date_of_Use = '{3}',
                  Test_ID = '{4}',
                  Student_ID = '{5}'
                  where Attempt_ID = {6}
                  """.format(Attempt_Score,Attempt_ID,Time_in_session,Date_of_Use,Test_ID,Student_ID,Attempt_ID)
        self._query(sql)

    def Search_Attempts(self,Attempt_ID):
        sql = """ select *
                  from Attempts
                  where Attempt_ID = '{0}'""".format(Attempt_ID)
        results = self._select_query(sql)
        if results == []:
            print('There is no Attempts Type with that ID')
        else:
            print(results)

    def Search_AttemptsTESTING(self,Attempt_Score):
        DataApproved = False
        sql = """ select Attempt_ID
                  from Attempts
                  where Attempt_Score = '{0}'""".format(Attempt_Score)
        results = self._select_query(sql)
        while DataApproved != True:
            if results == []:
                print('There are no Attempts with that ID')
            if results[0]== None:
                print('ahh')
            else:
                print('')
                return results

    def Return_AttemptsNoInput(self):
        sql = """ select *
                  from Attempts"""
        results = self._select_query(sql)
        if results == []:
            print('There are no Attempts with that ID')
        else:
            print(results)
        return results

    def Return_AttemptsbyID(self,Attempts_ID):
        sql = """ select *
                  from Attempts
                  where Attempt_ID = '{0}'""".format(Attempt_ID)   
        results = self._select_query(sql)
        if results == []:
            print('There is no Attempts with that ID')
        else:
            print('')
        return results

    def Return_AttemptsbyAttempt_Score(self,Attempt_Score):
        sql = """ select *
                  from Attempts
                  where Attempt_Score = '{0}'""".format(Attempt_Score)   
        results = self._select_query(sql)
        if results == []:
            print('There is no Attempts with that ID')
        else:
            print('')
        return results
            
    def SearchForAttempts(self,SearchItem):
        print('entered the search')
        Search = SearchItem
        IntegerSearch = False
        Attempts = self.Return_AttemptsNoInput()
        ItemFound = False
        row = 0 
        column = 0
        MaxItems = len(Attempts)
        for i in range(0,2):
            for each in Attempts:
                Item = Attempts[row][column]
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
                Attempts_ID = Search
                results = self.Return_AttemptsbyID(Attempts_ID)
                return results
            else:
                print('String')
                Attempts = Search
                results = self.Return_AttemptsbyAttempt_Score(Attempts)
                return results
        else:
            print('Hah it did not work')

