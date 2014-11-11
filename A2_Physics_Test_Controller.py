from A2_Physics_Controller_Class import*

class Test_Controller(A2_Physics_Controller):
    """ creates a controller in which to add, delete, update Tests in A2 Physics Database"""

    def __init__(self):
        super().__init__()

    def Add_Test(self,Test_Name):        
        sql = """insert into Tests(
                 Test_Name)
                 Values
                 ('{0}')""".format(Test_Name)
        self._query(sql)
        
    def Delete_Test(self,Test_ID):
        sql = """ delete from Tests
                  where Test_ID = '{0}'""".format(Test_ID)
        self._query(sql)

    def Update_Test(self,Test_ID,Test_Name):
        sql = """ update Tests
                  set Test_Name = '{0}'
                  where Test_ID = {1}
                  """.format(Test_Name,Test_ID)
        self._query(sql)

    def Return_TestsbyID(self,Test_ID):
        sql = """ select *
                  from Tests
                  where Test_ID = '{0}'""".format(Test_ID)   
        results = self._select_query(sql)
        if results == []:
            print('There is no test with that ID')
        else:
            print('')
        return results
    
    def Return_TestsbyName(self,Test_Name):
        sql = """ select *
                  from Tests
                  where Test_Name = '{0}'""".format(Test_Name)   
        results = self._select_query(sql)
        if results == []:
            print('There is no test with that ID')
        else:
            print('')
        return results

    def Return_TestsNoInput(self):
        sql = """ select *
                  from Tests"""
        results = self._select_query(sql)
        if results == []:
            print('There is no test with that ID')
        else:
            print('')
        return results
    
    def QComboBox_Tests(self):
        sql = """ select Test_Name
                  from Tests """  
        results = self._select_query(sql)
        return results

    def QComboBox_Retrieve_ID(self,Test_Name):
        sql= """ select Test_ID
                 from Tests
                 where Test_Name = '{0}'""".format(Test_Name)
        results = self._select_query(sql)
        if results ==[]:
            print('There are no tests')
        else:
            print('')
        return results
    
if __name__ == "__main__":
    test = Test_Controller()
    test.Update_Test(1,'name')
    returned = test.Return_TestsbyID('1')
    print(returned)
