from A2_Physics_Controller_Class import*

class Questions_Controller(A2_Physics_Controller):
    """ creates a controller in which to add, delete, update Tests in A2 Physics Database"""

    def __init__(self):
        super().__init__()

    def Add_Question(self,Question,Type_ID):        
        sql = """insert into Questions(
                 Question,
                 Type_ID)
                 values
                 ('{0}','{1}')""".format(Question,Type_ID)
        self._query(sql)
        
    def Delete_Question(self,Questions_ID):
        sql = """ delete from Questions
                  where Questions_ID = '{0}'""".format(Questions_ID)
        self._query(sql)

    def Update_Question(self,Question,Type_ID,Questions_ID):
        sql = """ update Questions
                  set Question = '{0}',
                  Type_ID = '{1}'
                  where Questions_ID = {2}
                  """.format(Question,Type_ID,Questions_ID)
        self._query(sql)

    def Search_Questions(self,Question_ID):
        sql = """ select *
                  from Questions
                  where Questions_ID = '{0}'""".format(Question_ID)
        results = self._select_query(sql)
        if results == []:
            print('There is no Question Type with that ID')
        else:
            print(results)

    def Search_QuestionsNoInput(self):
        sql = """ select *
                  from Questions"""
        results = self._select_query(sql)
        if results == []:
            print('There is no Question Type with that ID')
        else:
            print(results)
        return results

    def Search_QuestionsSTUDENTTEST(self,Question_ID):
        DataApproved = False
        sql = """ select Question
                  from Questions
                  where Questions_ID = '{0}'""".format(Question_ID)
        results = self._select_query(sql)
        while DataApproved != True:
            if results == []:
                print('There is no Question with that ID')
            if results[0]== None:
                print('ahh')
            else:
                print('')
                return results

    def Return_QuestionsbyID(self,Question_ID):
        sql = """ select *
                  from Questions
                  where Questions_ID = '{0}'""".format(Question_ID)   
        results = self._select_query(sql)
        if results == []:
            print('There is no test with that ID')
        else:
            print('')
        return results
    
    def Return_QuestionsbyQuestion(self,Question):
        sql = """ select *
                  from Questions
                  where Question = '{0}'""".format(Question)   
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
        Questions = self.Search_QuestionsNoInput()
        ItemFound = False
        row = 0 
        column = 0
        MaxItems = len(Questions)
        for i in range(0,2):
            for each in Questions:
                Item = Questions[row][column]
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
                Question_ID = Search
                results = self.Return_QuestionsbyID(Question_ID)
                return results
            else:
                print('String')
                Question = Search
                results= self.Return_QuestionsbyQuestion(Question)
                return results
        else:
            print('Hah it did not work')
