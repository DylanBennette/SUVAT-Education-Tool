from A2_Physics_Controller_Class import*

class Answers_Controller(A2_Physics_Controller):
    """ creates a controller in which to add, delete, update Tests in A2 Physics Database"""

    def __init__(self):
        super().__init__()

    def Add_Answer(self,Correct_Answer,Questions_ID):        
        sql = """insert into Answers(
                 Correct_Answer,
                 Questions_ID)
                 values
                 ('{0}','{1}')""".format(Correct_Answer,Questions_ID)
        self._query(sql)
        
    def Delete_Answer(self,Answers_ID):
        sql = """ delete from Answers
                  where Answer_ID = '{0}'""".format(Answers_ID)
        self._query(sql)

    def Update_Answer(self,Correct_Answer,Questions_ID,Answer_ID):
        sql = """ update Answers
                  set Correct_Answer = '{0}',
                  Questions_ID = '{1}'
                  where Answer_ID = {2}
                  """.format(Correct_Answer,Questions_ID,Answer_ID)
        self._query(sql)

    def Search_Answers(self,Answer_ID):
        sql = """ select *
                  from Answers
                  where Answer_ID = '{0}'""".format(Answer_ID)
        results = self._select_query(sql)
        if results == []:
            print('There is no Correct_Answer Questions with that ID')
        else:
            print(results)

    def Return_AnswersNoInput(self):
        sql = """ select *
                  from Answers"""
        results = self._select_query(sql)
        if results == []:
            print('There is no Correct_Answer Questions with that ID')
        else:
            print(results)
        return results

    def Search_AnswersSTUDENTTEST(self,Answer_ID):
        DataApproved = False
        sql = """ select Correct_Answer
                  from Answers
                  where Answer_ID = '{0}'""".format(Answer_ID)
        results = self._select_query(sql)
        while DataApproved != True:
            if results == []:
                print('There is no Answer with that ID')
            if results== None or []:
                print('ahh')
            else:
                print('')
                return results

    def Return_AnswersbyID(self,Answer_ID):
        sql = """ select *
                  from Answers
                  where Answer_ID = '{0}'""".format(Answer_ID)   
        results = self._select_query(sql)
        if results == []:
            print('There is no test with that ID')
        else:
            print('')
        return results
    
    def Return_AnswersbyAnswer(self,Correct_Answer):
        sql = """ select *
                  from Answers
                  where Correct_Answer = '{0}'""".format(Correct_Answer)   
        results = self._select_query(sql)
        if results == []:
            print('There is no test with that ID')
        else:
            print('')
        return results
            
    def SearchForCorrect_Answer(self,SearchItem):
        print('entered the search')
        Search = SearchItem
        IntegerSearch = False
        Answers = self.Search_AnswersNoInput()
        ItemFound = False
        row = 0 
        column = 0
        MaxItems = len(Answers)
        for i in range(0,2):
            for each in Answers:
                Item = Answers[row][column]
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
                Correct_Answer_ID = Search
                results = self.Return_AnswersbyID(Correct_Answer)
                return results
            else:
                print('String')
                Correct_Answer = Search
                results= self.Return_AnswersbyAnswer(Correct_Answer)
                return results
        else:
            print('Hah it did not work')
