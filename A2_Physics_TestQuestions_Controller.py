from A2_Physics_Controller_Class import*

class TestQuestions_Controller(A2_Physics_Controller):
    """ creates a controller in which to add, delete, update TestQuestionss records in A2 Physics Database"""

    def __init__(self):
        super().__init__()

    def Add_TestQuestions(self,Test_ID,Questions_ID):
        sql ="""insert into TestQuestions(
                Test_ID,
                Questions_ID)
                Values
                ('{0}','{1}')""".format(Test_ID,Questions_ID)
        self._query(sql)

    def Delete_TestQuestions(self,TestQuestions_ID):
        sql = """ delete from TestQuestions
                  where TestQuestions_ID = '{0}'""".format(TestQuestions_ID)
        self._query(sql)

    def Update_TestQuestions(self,Test_ID,Questions_ID,TestQuestions_ID):  
        sql = """ update TestQuestions
                  set Test_ID = '{0}',
                  Questions_ID = '{1}'
                  where TestQuestions_ID = {2}
                  """.format(Test_ID,Questions_ID,TestQuestions_ID)
        self._query(sql)

    def Search_TestQuestions(self,TestQuestions_ID):
        sql = """ select *
                  from TestQuestions
                  where TestQuestions_ID = '{0}'""".format(TestQuestions_ID)
        results = self._select_query(sql)
        if results == []:
            print('There is no TestQuestions with that ID')
        else:
            print(results)
            return results
        
    def Search_TestQuestionsSTUDENTTESTING(self,Test_ID):
        DataApproved = False
        sql = """ select Questions_ID
                  from TestQuestions
                  where Test_ID = '{0}'""".format(Test_ID)
        results = self._select_query(sql)
        while DataApproved != True:
            if results == []:
                print('There is no TestQuestions with that ID')
            if results[0]== None:
                print('ahh')
            else:
                print('')
                return results

    def Return_TestQuestionsNoInput(self):
        sql = """ select *
                  from TestQuestions"""
        results = self._select_query(sql)
        if results == []:
            print('There is no Correct_Test_Questions Questions with that ID')
        else:
            print(results)
        return results

    def Search_TestQuestionsSTUDENTTEST(self,TestQuestions_ID):
        DataApproved = False
        sql = """ select Correct_Test_Questions
                  from TestQuestions
                  where TestQuestions_ID = '{0}'""".format(TestQuestions_ID)
        results = self._select_query(sql)
        while DataApproved != True:
            if results == []:
                print('There is no Test_Questions with that ID')
            if results[0]== None:
                print('ahh')
            else:
                print('')
                return results

    def Return_TestQuestionsbyTest_ID(self,Test_ID):
        sql = """ select *
                  from TestQuestions
                  where Test_ID = '{0}'""".format(Test_ID)   
        results = self._select_query(sql)
        if results == []:
            print('There is no test with that ID')
        else:
            print('')
        return results
    
    def Return_TestQuestionsbyTestQuestions_ID(self,TestQuestions_ID):
        sql = """ select *
                  from TestQuestions
                  where TestQuestions_ID = '{0}'""".format(TestQuestions_ID)   
        results = self._select_query(sql)
        if results == []:
            print('There is no test with that ID')
        else:
            print('')
        return results
            
    def SearchForTestQuestions(self,SearchItem):
        print('entered the search')
        Search = SearchItem
        IntegerSearch = False
        Test_Questions = self.Return_TestQuestionsNoInput()
        ItemFound = False
        row = 0 
        column = 0
        MaxItems = len(Test_Questions)
        for i in range(0,3):
            for each in Test_Questions:
                Item = Test_Questions[row][column]
                if Item == Search:
                    ItemFound = True
                if row <= MaxItems:
                    row += 1
                if row == MaxItems:
                    column += 1
                    row = 0
        if ItemFound == True:
            if type(Search) == int:
                IntegerSearch = True
                Questions_ID = Search
                results = self.Return_TestQuestionsbyTest_ID(Questions_ID)
                return results
            else:
                TestQuestions_ID = Search
                results = self.Return_TestQuestionsbyTestQuestions_ID(TestQuestions_ID)
                return results
       # else:
      #      print('Hah it did not work')


