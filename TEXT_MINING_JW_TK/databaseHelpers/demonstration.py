from databaseHelpers.SqliteHelper import SqliteHelper
from dataModel.Document import Document

myHelper = SqliteHelper("C:/Users/Jacek/Desktop/baza danych.db")
myHelper.start()
myHelper.createDocumentTable("MY_ARTICLE")

for i in range(1,200):
    myHelper.saveDocument(Document("Tytuł","JAKIŚ 'TEKST', JAKIŚ TEKST, JAKIŚ TEKST!!!!","2017-08-05","www.wp.pl"),"MY_ARTICLE")

myHelper.close()
