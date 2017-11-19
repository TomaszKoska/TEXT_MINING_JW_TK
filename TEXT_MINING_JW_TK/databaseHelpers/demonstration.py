from databaseHelpers.SqliteHelper import SqliteHelper
from dataModel.Document import Document

myHelper = SqliteHelper("D:/databases/testDlaJacka.db")
myHelper.start()
myHelper.createDocumentTable("MY_ARTICLE")
myHelper.createDocumentTable("MY_ARTICLE2")
myHelper.createDocumentTable("MY_ARTICLE3")
for i in range(1,200):
    myHelper.saveDocument(Document("Tytuł","JAKIŚ TEKST, JAKIŚ TEKST, JAKIŚ TEKST!!!!","2017-08-05","www.wp.pl"),"MY_ARTICLE")

myHelper.close()
