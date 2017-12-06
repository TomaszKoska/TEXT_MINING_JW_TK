from cingCiangCiong.Base import *
from dataModel.Document import Document
from databaseHelpers.SqliteHelper import SqliteHelper

helper = SqliteHelper("D:/databases/bazka1.db")
helper.start()
table = " pozdro"
docs = helper.getDocuments(table)
#for d in docs:
#    print(d.text)

a = getAllWords(docs)
print(a)

b= getWordsCount(docs)
print(b)

c= getWordsFrequency(docs, allWords=["PLANACH",'1'])
print(c)

d = getLeftContext(docs,"i",3)
for k,v in d.items():
    if(v>0):
        print(k + "     " + str(v))

