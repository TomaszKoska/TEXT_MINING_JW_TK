import unittest
from databaseHelpers.SqliteHelper import SqliteHelper

class Test_SqliteHelper(unittest.TestCase):

    def setUp(self):
        self.databasePath = "D:/databases/SomeTestDbBetterDontUseThisNameEverEverEverAgain.db"
        #self.databasePath = "D:/databases/test_db.db"
        self.testHelper = SqliteHelper(self.databasePath)
        self.listOfFields = {'NAME1' : "INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE",
        'NAME2' : "INTEGER",
        'NAME3' : "TEXT"}
        self.tableName = "SOME_TABLE"
        self.articleTableName = "TEST_ART_TABLE"
        self.testHelper.start()


    def tearDown(self):
        self.testHelper.close()


    def test_turnlistOfFieldsToQuery(self):
        outputQuery = "CREATE TABLE 'SOME_TABLE' ('NAME1' INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,'NAME2' INTEGER,'NAME3' TEXT);"
        self.assertEqual(self.testHelper.turnlistOfFieldsToQuery(self.tableName,self.listOfFields),outputQuery)
    
    def test_createSimpleTable(self):
        self.testHelper.createSimpleTable(self.tableName,self.listOfFields)
        outcome = self.testHelper.checkIfTableExists(self.tableName)
        self.testHelper.deleteTable(self.tableName)
        self.assertEqual(outcome,True)
    
    def test_createDocumentTable(self):
        name = self.articleTableName
        self.testHelper.createDocumentTable(name)
        outcome = self.testHelper.checkIfTableExists(name)
        self.testHelper.deleteTable(self.articleTableName)
        self.assertEqual(outcome,True)


if __name__ == '__main__':
    unittest.main()
