from A2_Physics_Controller_Class import*

class Response_Controller(A2_Physics_Controller):
    """ creates a controller in which to add, delete, update Responses in A2 Physics Database"""

    def __init__(self):
        super().__init__()

    def Add_Response(self,Student_Response,Attempt_ID,Questions_ID):        
        sql = """insert into Responses(
                 Attempt_ID,
                 Questions_ID,
                 Student_Response)
                 values
                 ('{0}','{1}','{2}')""".format(Attempt_ID,Questions_ID,Student_Response)
        self._query(sql)
        
    def Delete_Response(self,Response_ID):
        sql = """ delete from Responses
                  where Response_ID = '{0}'""".format(Response_ID)
        self._query(sql)

    def Update_Response(self,Attempt_ID,Questions_ID,Response_ID,Student_Response):
        sql = """ update Responses
                  set Questions_ID = '{0}',
                  Attempt_ID = '{1}',
                  Student_Response = '{2}',
                  where Response_ID = {3}
                  """.format(Questions_ID,Attempt_ID,Student_Response,Response_ID)
        self._query(sql)

    def Search_Response(self,Response_ID):
        sql = """ select *
                  from Responses
                  where Response_ID = '{0}'""".format(Response_ID)
        results = self._select_query(sql)
        if results == []:
            print('There is no Responses with that ID')
        else:
            print(results)

    def Return_ResponseNoInput(self):
        sql = """ select *
                  from Responses"""
        results = self._select_query(sql)
        if results == []:
            print('There is no Question Type with that ID')
        else:
            print(results)
        return results

    def Search_ResponseSTUDENTTEST(self,Response_ID):
        DataApproved = False
        sql = """ select Question
                  from Responses
                  where Response_ID = '{0}'""".format(Response_ID)
        results = self._select_query(sql)
        while DataApproved != True:
            if results == []:
                print('There is no Response with that ID')
            if results[0]== None:
                print('ahh')
            else:
                print('')
                return results

    def Return_ResponsebyID(self,Response_ID):
        sql = """ select *
                  from Responses
                  where Response_ID = '{0}'""".format(Response_ID)   
        results = self._select_query(sql)
        if results == []:
            print('There is no test with that ID')
        else:
            print('')
        return results
    
    def Return_ResponsebyQuestion(self,Student_Response):
        sql = """ select *
                  from Responses
                  where Student_Response = '{0}'""".format(Student_Response)   
        results = self._select_query(sql)
        if results == []:
            print('There is no test with that ID')
        else:
            print('')
        return results
            
    def SearchForQuestion(self,SearchItem):
        print('entered the search')
        Search = SearchItem
        IntegerSearch = False
        Response = self.Return_ResponseNoInput()
        ItemFound = False
        row = 0 
        column = 0
        MaxItems = len(Response)
        for i in range(0,2):
            for each in Response:
                Item = Response[row][column]
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
                Question_ID = Search
                results = self.Return_ResponsebyID(Response_ID)
                return results
            else:
                print('String')
                Student_Response = Search
                results= self.Return_ResponsebyStudentResponse(Student_Response)
                return results
        else:
            print('Hah it did not work')

