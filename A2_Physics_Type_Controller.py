from A2_Physics_Controller_Class import*

class Type_Controller(A2_Physics_Controller):
    """ creates a controller in which to add, delete, update Tests in A2 Physics Database"""

    def __init__(self):
        super().__init__()

    def Add_Type(self,Question_Type):        
        sql = """insert into Type(
                 Question_Type)
                 values
                 ('{0}')""".format(Question_Type)
        self._query(sql)
        
    def Delete_Type(self,Type_ID):
        sql = """ delete from Type
                  where Type_ID = '{0}'""".format(Type_ID)
        self._query(sql)

    def Update_Type(self,Type_ID,Question_Type):
        sql = """ update Type
                  set Question_Type = '{0}'
                  where Type_ID = {1}
                  """.format(Question_Type,Type_ID)
        self._query(sql)

    def Search_Type(self,Type_ID):
        sql = """ select *
                  from Type
                  where Type_ID = '{0}'""".format(Type_ID)
        results = self._select_query(sql)
        if results == []:
            print('There is no Type with that ID')
        else:
            print(results)

    def Return_TypeNoInput(self):
        sql = """ select *
                  from Type"""
        results = self._select_query(sql)
        if results == []:
            print('There is no Type with that ID')
        else:
            print(results)
        return results

    def Search_TypeSTUDENTTEST(self,Type_ID):
        DataApproved = False
        sql = """ select Type
                  from Type
                  where Type_ID = '{0}'""".format(Type_ID)
        results = self._select_query(sql)
        while DataApproved != True:
            if results == []:
                print('There is no Type with that ID')
            if results[0]== None:
                print('ahh')
            else:
                print('')
                return results

    def Return_TypebyID(self,Type_ID):
        sql = """ select *
                  from Type
                  where Type_ID = '{0}'""".format(Type_ID)   
        results = self._select_query(sql)
        if results == []:
            print('There is no Type with that ID')
        else:
            print('')
        return results

    def Return_TypebyType(self,Question_Type):
        sql = """ select *
                  from Type
                  where Question_Type = '{0}'""".format(Question_Type)   
        results = self._select_query(sql)
        if results == []:
            print('There is no Type with that ID')
        else:
            print('')
        return results
            
    def SearchForType(self,SearchItem):
        print('entered the search')
        Search = SearchItem
        IntegerSearch = False
        Questions = self.Return_TypeNoInput()
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
                results = self.Return_TypebyID(Question_ID)
                return results
            else:
                print('String')
                Question = Search
                results= self.Return_TypebyType(Question)
                return results
        else:
            print('Hah it did not work')

            
