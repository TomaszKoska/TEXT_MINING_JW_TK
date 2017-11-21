from databaseHelpers.AbstractDatabaseHelper import AbstractDatabaseHelper
from dataModel.Document import Document

import re
import sqlite3

class SqliteHelper(AbstractDatabaseHelper):
    """description of class"""
    def __init__(self, databesePath):
        self.databasePath = databesePath
        self.connection = None

    def start(self):
        self.connection = sqlite3.connect( self.databasePath)

    def close(self):
        self.connection.close()

    def createSimpleTable(self, tableName, listOfFields):
        self.connection.execute(self.turnlistOfFieldsToQuery(tableName, listOfFields))
        self.connection.commit()
    
    def deleteTable(self, tableName):
        self.connection.execute("DROP TABLE "+tableName+";")
        self.connection.commit()


    def checkIfTableExists(self, tableName):
        cursor = self.connection.execute("SELECT count(1) FROM sqlite_master WHERE type='table' AND name='" + tableName + "';")
        for row in cursor:
            return int(row[0]) > 0
        

    def turnlistOfFieldsToQuery(self, tableName, listOfFields):
        """
        It should go like this:
        {'NAME1' : "INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE",
        'NAME2' : "INTEGER",
        'NAME3' : "TEXT"}
        
        CREATE TABLE `SOME_TABLE` (
	        `NAME1`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	        `NAME2`	INTEGER,
	        `NAME3`	TEXT
        );
        
        """
        output = "CREATE TABLE '" + tableName + "' ("

        fieldInfo = []
        for fieldName, fieldAttributes in listOfFields.items():
            fieldInfo.append("'" + fieldName + "' " + fieldAttributes)
            #print("'" + fieldName + "' " + fieldAttributes)
            #print(",".join(fieldInfo))

        output = output + ",".join(fieldInfo)


        output = output + ");"
        return output

    def createDocumentTable(self, tableName):
        listOfFields = {'ID' : "INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE",
        'TITLE' : "INTEGER",
        'CONTENT' : "TEXT",
        'DATE' : "TEXT",
        'SOURCE': "TEXT"
        }
        self.createSimpleTable(tableName,listOfFields)

    def saveDocument(self,document = Document(), tableName = ""):
        #print("I tutaj Jacku dochodzi do zapiania dokumentu w bazie danych (tzn zaimplementuję to jak wrócę)")
        #print("argument numer 1 to dokument typu Document (zmieniłem ArticleClass na Document) a to drugie to nazwa tabeli jako string")
        

        #query = "INSERT INTO " + tableName + " (TITLE, CONTENT, DATE, SOURCE) \
        #  VALUES ('"+str(document.title) +"','"+documentContentToSave+"','"+ str(document.date)+"','"+str(document.source)+"')"
        
        query = "INSERT INTO "+tableName+" (TITLE, CONTENT, DATE, SOURCE) VALUES (?, ? , ? , ? )"
        print(query)
        self.connection.execute(query,(str(document.title),str(document.text),str(document.date),str(document.source)));
        print("coś tam wrzucam...")
        self.connection.commit()




if __name__ == '__main__':
    pass
