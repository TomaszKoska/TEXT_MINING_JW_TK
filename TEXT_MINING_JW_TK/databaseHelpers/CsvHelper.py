from databaseHelpers.AbstractDatabaseHelper import AbstractDatabaseHelper
from dataModel.Document import Document
import csv

class CsvHelper(AbstractDatabaseHelper):
    """CsvHelper - dla niego ścieżką do danych jest folder(!) w którym będzie tworzył pliki csv, każdy plik csv jest jak tabela bazy danych"""

    def __init__(self, databesePath = "D:/databases/csv/", delimiter = ","):
        #dodać obsługę, linków bez "/" na końcu
        if databesePath[-1:] != "/":
            databesePath = databesePath + "/"
        self.databasePath = databesePath
        self.delimiter = delimiter

    def setDelimiter(self, delimiter = ","):
        self.delimiter = delimiter

    def start(self):
        pass

    def close(self):
        pass

    def createDocumentTable(self,tableName="noNameGiven"):
        #dodać obsługę przypadku, że już jest taki plik
        if tableName[-4:] != ".csv":
            tableName = tableName + ".csv"
        tableName = self.databasePath + tableName
        with open(tableName, "w") as my_empty_csv:
            csv_writer = csv.DictWriter(my_empty_csv,fieldnames=["ID", "TITLE", "DATE","SOURCE", "CONTENT"], delimiter=self.delimiter,lineterminator = '\n')
            csv_writer.writeheader()

    def nextDocId(self, tableName="noNameGiven"):
        #to raczej da się zrobić lepiej
        if tableName[-4:] != ".csv":
            tableName = tableName + ".csv"
        tableName = self.databasePath + tableName

        i = 0
        f = open(tableName, "r")
        for i, line in enumerate(f):
            pass
        #print(i + 1)
        f.close()
        return i+1

    def saveDocument(self,document = Document(), tableName="noNameGiven"):
        #do poprawki na kiedyś: niech ID się zmienia
        if tableName[-4:] != ".csv":
            tableName = tableName + ".csv"
        fullTableName = self.databasePath + tableName

        with open(fullTableName, "a") as openedFile:
            csv_writer = csv.DictWriter(openedFile,fieldnames=["ID", "TITLE", "DATE","SOURCE", "CONTENT"], delimiter=self.delimiter,lineterminator = '\n') 
            csv_writer.writerow({"ID": self.nextDocId(tableName), "TITLE" : document.title, "DATE": document.date, "SOURCE" : document.source,  "CONTENT" : document.text}  )
        pass


    def getDocuments(self, tableName = "noNameGiven"):
        documents = []
        if tableName[-4:] != ".csv":
            tableName = tableName + ".csv"
        fullTableName = self.databasePath + tableName
        with open(fullTableName, 'rt') as csvfile:
            csvReader = csv.reader(csvfile, delimiter=self.delimiter, quotechar="\"")
            for row in csvReader:
                documents.append(Document(title=row[1], text=row[4], date=row[2], source=row[3]))
                #print(documents.pop().text)
            documents.remove(documents[0])
        return documents



