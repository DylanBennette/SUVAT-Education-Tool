import sqlite3

class A2_Physics_controller:

    def __init__(self):
        self.dbtext = "A2_Physics_Database.db"
        
    def _query(self,sql):
        self.db = sqlite3.connect(self.dbtext)
        self.cursor = self.db.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON")
        self.cursor.execute(sql)
        self.db.commit()
        self.cursor.close()

    def _select_query(self,sql):
        self.db = sqlite3.connect(self.dbtext)
        self.cursor = self.db.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON")
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        self.cursor.close()
        return results

        
