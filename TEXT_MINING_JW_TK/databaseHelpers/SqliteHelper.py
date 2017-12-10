from databaseHelpers.AbstractDatabaseHelper import AbstractDatabaseHelper
from dataModel.Document import Document
from dataModel.TextTopic import TextTopic

import re
import sqlite3

class SqliteHelper(AbstractDatabaseHelper):
    """description of class"""
    def __init__(self, databesePath):
        self.databasePath = databesePath
        self.connection = None
        
        #dla iteratora
        self.currentRowId = 0
        self.iteratorTablename = ""


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
        'TITLE' : "TEXT",
        'CONTENT' : "TEXT",
        'DATE' : "TEXT",
        'SOURCE': "TEXT",
        'LABEL' : "TEXT"
        }
        self.createSimpleTable(tableName,listOfFields)

    def saveDocument(self,document = Document(), tableName = ""):
        #print("I tutaj Jacku dochodzi do zapiania dokumentu w bazie danych (tzn zaimplementuję to jak wrócę)")
        #print("argument numer 1 to dokument typu Document (zmieniłem ArticleClass na Document) a to drugie to nazwa tabeli jako string")
        

        #query = "INSERT INTO " + tableName + " (TITLE, CONTENT, DATE, SOURCE) \
        #  VALUES ('"+str(document.title) +"','"+documentContentToSave+"','"+ str(document.date)+"','"+str(document.source)+"')"
        
        query = "INSERT INTO "+tableName+" (TITLE, CONTENT, DATE, SOURCE, LABEL) VALUES (?, ? , ? , ? , ?)"
        #print(query)
        self.connection.execute(query,(str(document.title),str(document.text),str(document.date),str(document.source),str(document.label)));
        self.connection.commit()

    
    def getDocuments(self, tableName = "noNameGiven"):
        documents = []
        cursor = self.connection.execute("SELECT ID, TITLE, CONTENT, DATE, SOURCE, LABEL  from " + tableName)
        for row in cursor:
           print ("TITLE = ", row[1])
           print ("CONTENT = ", row[2])
           print ("DATE = ", row[3])
           print ("SOURCE = ", row[4], "\n")
           documents.append(Document(title=row[1], text=row[2], date=row[3], source=row[4], label = row[5]))

        return documents;


    def startIterator(self, tableName = "noNameGiven"):
        self.currentRowId = 0
        self.iteratorTablename = tableName
        #select * from  pozdro where id > 10 limit 1


    def getNextDocument(self):
        cursor = self.connection.execute("SELECT ID, TITLE, CONTENT, DATE, SOURCE, LABEL  from " + self.iteratorTablename + " WHERE ID > " + str(self.currentRowId) + " LIMIT 1;")
        for row in cursor:
            self.currentRowId = int(row[0])
            #print("Coś do zwrócenia!")
            return Document(title=row[1], text=row[2], date=row[3], source=row[4], label = row[5])
        #print("Nic do zwrócenia! " + self.iteratorTablename + "   " + str(self.currentRowId))
        raise StopIteration #to jest tak: jeśli jest jeden wiersz w kursorze, to wykona się return (funkcja się skończy)
                            #jeśli dojdzie aż tu, to znacy, że nie było ani jednego wiersza = skończyły się dane

    def stopIterator(self):
        pass

    def createTopicTable(self,tableName=""):
        listOfFields = {'ID' : "INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE",
        'TOPIC_NAME' : "TEXT",
        'WORD' : "TEXT",
        'COUNT' : "INTEGER"
        }
        self.createSimpleTable(tableName,listOfFields)


    def saveTopic(self,topic = TextTopic(), tableName = ""):
        query = "INSERT INTO "+tableName+" (TOPIC_NAME, WORD, COUNT) VALUES (?, ? , ? )"
        #print(query)
        for w,c in topic.wordDistributions.items():
            self.connection.execute(query,(str(topic.name),str(w),c));
        self.connection.commit()


    def getTopics(self, tableName = ""):
        topics = {}
        topicCursor = self.connection.execute("SELECT DISTINCT TOPIC_NAME from " + tableName)

        for t in topicCursor:
           topics[t[0]]={}
           cursor = self.connection.execute("SELECT TOPIC_NAME, WORD, COUNT  from " + tableName + " WHERE TOPIC_NAME = ?;",(t[0],))
           dist = {}
           for row in cursor:
               dist[row[1]]=row[2]
           topics[t[0]]=TextTopic(name=t[0],wordDistributions=dist)

        return topics;





if __name__ == '__main__':
    pass