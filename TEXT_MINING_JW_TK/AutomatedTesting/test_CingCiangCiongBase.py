import unittest
from cingCiangCiong.Base import *
from databaseHelpers.CsvHelper import CsvHelper
import tempfile


class Test_CingCiangCiongBase(unittest.TestCase):

    def setUp(self):
        self.testHelper = CsvHelper(tempfile.gettempdir())
        self.tableName = "someTestNameThatYouShouldNOTUse"
        self.testHelper.createDocumentTable(self.tableName)
        
        self.docs = []
        self.docs.append(Document(title="TEST!", text="A GOAT EATS THE FLOWER", date="", source=""))
        self.docs.append(Document(title="TEST!", text="A HERBIVORE EATS THE FLOWER", date="", source=""))
        self.docs.append(Document(title="TEST!", text="A BIRD EATS THE VEGETABLE", date="", source=""))
        self.docs.append(Document(title="TEST!", text="A GOAT EATS THE VEGETABLE", date="", source=""))
        self.docs.append(Document(title="TEST!", text="A HERBIVORE EATS A GRASS", date="", source=""))
        self.docs.append(Document(title="TEST!", text="THE GOAT EATS A FLOWER", date="", source=""))
        self.docs.append(Document(title="TEST!", text="THE SHEEP EATS THE PLANT", date="", source=""))
        self.docs.append(Document(title="TEST!", text="A COW EATS A GRASS", date="", source=""))
        self.docs.append(Document(title="TEST!", text="THE HERBIVORE EATS A PLANT", date="", source=""))
        self.docs.append(Document(title="TEST!", text="A COW EATS A PLANT", date="", source=""))
        self.docs.append(Document(title="TEST!", text="THE HERBIVORE EATS A FLOWER", date="", source=""))
        self.docs.append(Document(title="TEST!", text="THE HERBIVORE EATS THE PLANT", date="", source=""))
        self.docs.append(Document(title="TEST!", text="A HERBIVORE EATS A PLANT", date="", source=""))
        self.docs.append(Document(title="TEST!", text="A HERBIVORE EATS A PLANT", date="", source=""))
        self.docs.append(Document(title="TEST!", text="A HERBIVORE EATS THE TOMATO", date="", source=""))
        self.docs.append(Document(title="TEST!", text="A COW EATS A PLANT", date="", source=""))

        for d in self.docs:
            self.testHelper.saveDocument(d,self.tableName)

    def tearDown(self):
        self.testHelper.close()


    def test_getAllWords(self):
        docs = []
        docs.append(Document(title="TEST!", text="A GOAT EATS THE FLOWER", date="", source=""))
        docs.append(Document(title="TEST!", text="A HERBIVORE EATS THE FLOWER", date="", source=""))
        docs.append(Document(title="TEST!", text="A BIRD EATS THE VEGETABLE", date="", source=""))
        docs.append(Document(title="TEST!", text="A GOAT EATS THE VEGETABLE", date="", source=""))
        docs.append(Document(title="TEST!", text="A HERBIVORE EATS A GRASS", date="", source=""))
        docs.append(Document(title="TEST!", text="THE GOAT EATS A FLOWER", date="", source=""))
        docs.append(Document(title="TEST!", text="THE SHEEP EATS THE PLANT", date="", source=""))
        docs.append(Document(title="TEST!", text="A COW EATS A GRASS", date="", source=""))
        docs.append(Document(title="TEST!", text="THE HERBIVORE EATS A PLANT", date="", source=""))
        docs.append(Document(title="TEST!", text="A COW EATS A PLANT", date="", source=""))
        docs.append(Document(title="TEST!", text="THE HERBIVORE EATS A FLOWER", date="", source=""))
        docs.append(Document(title="TEST!", text="THE HERBIVORE EATS THE PLANT", date="", source=""))
        docs.append(Document(title="TEST!", text="A HERBIVORE EATS A PLANT", date="", source=""))
        docs.append(Document(title="TEST!", text="A HERBIVORE EATS A PLANT", date="", source=""))
        docs.append(Document(title="TEST!", text="A HERBIVORE EATS THE TOMATO", date="", source=""))
        docs.append(Document(title="TEST!", text="A COW EATS A PLANT", date="", source=""))

        expectedOutcome = ["A","THE","GOAT","HERBIVORE","BIRD","SHEEP","COW","EATS","FLOWER","VEGETABLE","GRASS","PLANT","TOMATO"]
        outcome = getAllWords(docs)
        self.assertEqual(len(list(set(outcome) - set(expectedOutcome))),0)
        self.assertEqual(len(list(set(expectedOutcome) - set(outcome))),0)
        expectedOutcome = ["A","THE","GOAT"]
        outcome = getAllWords(Document(title="TEST!", text="A THE GOAT", date="", source=""))
        self.assertEqual(len(list(set(outcome) - set(expectedOutcome))),0)
        self.assertEqual(len(list(set(expectedOutcome) - set(outcome))),0)

    def test_getAllWordsIter(self):
        expectedOutcome = ["A","THE","GOAT","HERBIVORE","BIRD","SHEEP","COW","EATS","FLOWER","VEGETABLE","GRASS","PLANT","TOMATO"]
        outcome = getAllWordsIter(self.testHelper,self.tableName)
        self.assertEqual(len(list(set(outcome) - set(expectedOutcome))),0)
        self.assertEqual(len(list(set(expectedOutcome) - set(outcome))),0)

    def test_getWordsCount(self):
        docs = self.testHelper.getDocuments(self.tableName)
        self.assertEqual(getWordsCount(documents=docs),{'A': 20, 'GOAT': 3, 'EATS': 16, 'THE': 12, 'FLOWER': 4, 'HERBIVORE': 8, 'BIRD': 1, 'VEGETABLE': 2, 'GRASS': 2, 'SHEEP': 1, 'PLANT': 7, 'COW': 3, 'TOMATO': 1})
        docs = self.testHelper.getDocuments(self.tableName)
        self.assertEqual(getWordsCount(documents=docs,allWords=["A","THE"]),{'A': 20, 'THE': 12})
        docs = self.testHelper.getDocuments(self.tableName)
        self.assertEqual(getWordsCount(documents=docs,allWords=["A","THE","FOOOO"]),{'A': 20, 'THE': 12, 'FOOOO' : 0}) #great!!!
    
    def test_getWordsCountIter(self):
        #print(self.tableName)
        self.assertEqual(getWordsCountIter(dbHelper=self.testHelper,tableName=self.tableName),{'A': 20, 'GOAT': 3, 'EATS': 16, 'THE': 12, 'FLOWER': 4, 'HERBIVORE': 8, 'BIRD': 1, 'VEGETABLE': 2, 'GRASS': 2, 'SHEEP': 1, 'PLANT': 7, 'COW': 3, 'TOMATO': 1})
        self.assertEqual(getWordsCountIter(dbHelper=self.testHelper,tableName=self.tableName,allWords=["A","THE"]),{'A': 20, 'THE': 12})
        self.assertEqual(getWordsCountIter(dbHelper=self.testHelper,tableName=self.tableName,allWords=["A","THE","FOOOO"]),{'A': 20, 'THE': 12, 'FOOOO' : 0}) #great!!!


    def test_getWordsFrequency(self):
        docs = self.testHelper.getDocuments(self.tableName)
        self.assertEqual(getWordsFrequency(documents=docs),{'A': 20/80, 'GOAT': 3/80, 'EATS': 16/80, 'THE': 12/80, 'FLOWER': 4/80, 'HERBIVORE': 8/80, 'BIRD': 1/80, 'VEGETABLE': 2/80, 'GRASS': 2/80, 'SHEEP': 1/80, 'PLANT': 7/80, 'COW': 3/80, 'TOMATO': 1/80})
        docs = self.testHelper.getDocuments(self.tableName)
        self.assertEqual(getWordsFrequency(documents=docs,allWords=["A","THE"]),{'A': 20/32, 'THE': 12/32})
        docs = self.testHelper.getDocuments(self.tableName)
        self.assertEqual(getWordsFrequency(documents=docs,allWords=["A","THE","FOOOO"]),{'A': 20/32, 'THE': 12/32, 'FOOOO' : 0/32}) #great!!!


    def test_getWordsFrequencyIterEmptyWordList(self):
        docs = self.testHelper.getDocuments(self.tableName)
        self.assertEqual(getWordsFrequencyIter(dbHelper=self.testHelper,tableName=self.tableName),{'A': 20/80, 'GOAT': 3/80, 'EATS': 16/80, 'THE': 12/80, 'FLOWER': 4/80, 'HERBIVORE': 8/80, 'BIRD': 1/80, 'VEGETABLE': 2/80, 'GRASS': 2/80, 'SHEEP': 1/80, 'PLANT': 7/80, 'COW': 3/80, 'TOMATO': 1/80})
        docs = self.testHelper.getDocuments(self.tableName)
        self.assertEqual(getWordsFrequencyIter(dbHelper=self.testHelper,tableName=self.tableName,allWords=["A","THE"]),{'A': 20/32, 'THE': 12/32})
        docs = self.testHelper.getDocuments(self.tableName)
        self.assertEqual(getWordsFrequencyIter(dbHelper=self.testHelper,tableName=self.tableName,allWords=["A","THE","FOOOO"]),{'A': 20/32, 'THE': 12/32, 'FOOOO' : 0/32}) #great!!!



    def test_getLeftContext(self):
        docs = self.testHelper.getDocuments(self.tableName)
        self.assertEqual(getLeftContext(documents=docs,word="EATS",distance=1,freq=True),{'GOAT': 0.1875, 'HERBIVORE': 0.5, 'BIRD': 0.0625, 'SHEEP': 0.0625, 'COW': 0.1875, 'THE': 0, 'EATS': 0, 'A': 0, 'FLOWER': 0, 'VEGETABLE': 0, 'GRASS': 0, 'TOMATO': 0, 'PLANT': 0})
        self.assertEqual(getLeftContext(documents=docs,word="THE",distance=1,freq=True),{'GOAT': 0, 'HERBIVORE': 0, 'BIRD': 0, 'SHEEP': 0, 'COW': 0, 'THE': 0, 'EATS': 7/7, 'A': 0, 'FLOWER': 0, 'VEGETABLE': 0, 'GRASS': 0, 'TOMATO': 0, 'PLANT': 0})
        self.assertEqual(getLeftContext(documents=docs,word="THE",distance=2,freq=True),{'GOAT': 2/14, 'HERBIVORE': 3/14, 'BIRD': 1/14, 'SHEEP': 1/14,'COW': 0, 'THE': 0, 'EATS': 7/14, 'A': 0, 'FLOWER': 0, 'VEGETABLE': 0, 'GRASS': 0, 'TOMATO': 0, 'PLANT': 0})
        self.assertEqual(getLeftContext(documents=docs,word="PUPA",distance=2,freq=True),{'GOAT': 0, 'HERBIVORE': 0, 'BIRD': 0, 'SHEEP': 0,'COW': 0, 'THE': 0, 'EATS': 0, 'A': 0, 'FLOWER': 0, 'VEGETABLE': 0, 'GRASS': 0, 'TOMATO': 0, 'PLANT': 0})
        docs = self.testHelper.getDocuments(self.tableName)
        self.assertEqual(getLeftContext(documents=docs,word="EATS",distance=1,allWords=["GOAT","HERBIVORE"],freq=True),{'GOAT': 0.1875, 'HERBIVORE': 0.5})
        self.assertEqual(getLeftContext(documents=docs,word="THE",distance=1,allWords=["GOAT","HERBIVORE"],freq=True),{'GOAT': 0, 'HERBIVORE': 0})
        self.assertEqual(getLeftContext(documents=docs,word="THE",distance=2,allWords=["GOAT","HERBIVORE"],freq=True),{'GOAT': 2/14, 'HERBIVORE': 3/14})
        self.assertEqual(getLeftContext(documents=docs,word="PUPA",distance=2,allWords=["GOAT","HERBIVORE"],freq=True),{'GOAT': 0, 'HERBIVORE': 0})
        self.assertEqual(getLeftContext(documents=docs,word="PUPA",distance=2,allWords=["GOAT","HERBIVORE","PUPA"],freq=True),{'GOAT': 0, 'HERBIVORE': 0,'PUPA' : 0})


    def test_getLeftContextIter(self):
        docs = self.testHelper.getDocuments(self.tableName)
        self.assertEqual(getLeftContextIter(dbHelper=self.testHelper,tableName=self.tableName,word="EATS",distance=1,freq=True),{'GOAT': 0.1875, 'HERBIVORE': 0.5, 'BIRD': 0.0625, 'SHEEP': 0.0625, 'COW': 0.1875, 'THE': 0, 'EATS': 0, 'A': 0, 'FLOWER': 0, 'VEGETABLE': 0, 'GRASS': 0, 'TOMATO': 0, 'PLANT': 0})
        self.assertEqual(getLeftContextIter(dbHelper=self.testHelper,tableName=self.tableName,word="THE",distance=1,freq=True),{'GOAT': 0, 'HERBIVORE': 0, 'BIRD': 0, 'SHEEP': 0, 'COW': 0, 'THE': 0, 'EATS': 7/7, 'A': 0, 'FLOWER': 0, 'VEGETABLE': 0, 'GRASS': 0, 'TOMATO': 0, 'PLANT': 0})
        self.assertEqual(getLeftContextIter(dbHelper=self.testHelper,tableName=self.tableName,word="THE",distance=2,freq=True),{'GOAT': 2/14, 'HERBIVORE': 3/14, 'BIRD': 1/14, 'SHEEP': 1/14,'COW': 0, 'THE': 0, 'EATS': 7/14, 'A': 0, 'FLOWER': 0, 'VEGETABLE': 0, 'GRASS': 0, 'TOMATO': 0, 'PLANT': 0})
        self.assertEqual(getLeftContextIter(dbHelper=self.testHelper,tableName=self.tableName,word="PUPA",distance=2,freq=True),{'GOAT': 0, 'HERBIVORE': 0, 'BIRD': 0, 'SHEEP': 0,'COW': 0, 'THE': 0, 'EATS': 0, 'A': 0, 'FLOWER': 0, 'VEGETABLE': 0, 'GRASS': 0, 'TOMATO': 0, 'PLANT': 0})
        docs = self.testHelper.getDocuments(self.tableName)
        self.assertEqual(getLeftContextIter(dbHelper=self.testHelper,tableName=self.tableName,word="EATS",distance=1,allWords=["GOAT","HERBIVORE"],freq=True),{'GOAT': 0.1875, 'HERBIVORE': 0.5})
        self.assertEqual(getLeftContextIter(dbHelper=self.testHelper,tableName=self.tableName,word="THE",distance=1,allWords=["GOAT","HERBIVORE"],freq=True),{'GOAT': 0, 'HERBIVORE': 0})
        self.assertEqual(getLeftContextIter(dbHelper=self.testHelper,tableName=self.tableName,word="THE",distance=2,allWords=["GOAT","HERBIVORE"],freq=True),{'GOAT': 2/14, 'HERBIVORE': 3/14})
        self.assertEqual(getLeftContextIter(dbHelper=self.testHelper,tableName=self.tableName,word="PUPA",distance=2,allWords=["GOAT","HERBIVORE"],freq=True),{'GOAT': 0, 'HERBIVORE': 0})
        self.assertEqual(getLeftContextIter(dbHelper=self.testHelper,tableName=self.tableName,word="PUPA",distance=2,allWords=["GOAT","HERBIVORE","PUPA"],freq=True),{'GOAT': 0, 'HERBIVORE': 0,'PUPA' : 0})
    
    def test_getRightContext(self):
        docs = self.testHelper.getDocuments(self.tableName)
        self.assertEqual(getRightContext(documents=docs,word="EATS",distance=1,freq=True),{'GOAT': 0, 'HERBIVORE': 0, 'BIRD': 0, 'SHEEP': 0, 'COW': 0, 'THE': 7/16, 'EATS': 0, 'A': 9/16, 'FLOWER': 0, 'VEGETABLE': 0, 'GRASS': 0, 'TOMATO': 0, 'PLANT': 0})
        self.assertEqual(getRightContext(documents=docs,word="EATS",distance=2,freq=True),{'GOAT': 0, 'HERBIVORE': 0, 'BIRD': 0, 'SHEEP': 0,'COW': 0, 'THE': 7/32, 'EATS': 0, 'A': 9/32, 'FLOWER': 4/32, 'VEGETABLE': 2/32, 'GRASS': 2/32, 'TOMATO': 1/32, 'PLANT': 7/32})
        self.assertEqual(getRightContext(documents=docs,word="PUPA",distance=2,freq=True),{'GOAT': 0, 'HERBIVORE': 0, 'BIRD': 0, 'SHEEP': 0,'COW': 0, 'THE': 0, 'EATS': 0, 'A': 0, 'FLOWER': 0, 'VEGETABLE': 0, 'GRASS': 0, 'TOMATO': 0, 'PLANT': 0})
        docs = self.testHelper.getDocuments(self.tableName)
        self.assertEqual(getRightContext(documents=docs,word="EATS",distance=1,allWords=["A","THE"],freq=True),{'A': 9/16, 'THE': 7/16})
        self.assertEqual(getRightContext(documents=docs,word="THE",distance=1,allWords=["A","THE"],freq=True),{'A': 0, 'THE': 0})
        self.assertEqual(getRightContext(documents=docs,word="EATS",distance=2,allWords=["A","THE"],freq=True),{'A': 9/32, 'THE': 7/32})
        self.assertEqual(getRightContext(documents=docs,word="PUPA",distance=2,allWords=["A","THE"],freq=True),{'A': 0, 'THE': 0})
        self.assertEqual(getRightContext(documents=docs,word="PUPA",distance=2,allWords=["A","THE","PUPA"],freq=True),{'A': 0, 'THE': 0,'PUPA' : 0})

    def test_getRightContextIter(self):
        docs = self.testHelper.getDocuments(self.tableName)
        self.assertEqual(getRightContextIter(dbHelper=self.testHelper,tableName=self.tableName,word="EATS",distance=1,freq=True),{'GOAT': 0, 'HERBIVORE': 0, 'BIRD': 0, 'SHEEP': 0, 'COW': 0, 'THE': 7/16, 'EATS': 0, 'A': 9/16, 'FLOWER': 0, 'VEGETABLE': 0, 'GRASS': 0, 'TOMATO': 0, 'PLANT': 0})
        self.assertEqual(getRightContextIter(dbHelper=self.testHelper,tableName=self.tableName,word="EATS",distance=2,freq=True),{'GOAT': 0, 'HERBIVORE': 0, 'BIRD': 0, 'SHEEP': 0,'COW': 0, 'THE': 7/32, 'EATS': 0, 'A': 9/32, 'FLOWER': 4/32, 'VEGETABLE': 2/32, 'GRASS': 2/32, 'TOMATO': 1/32, 'PLANT': 7/32})
        self.assertEqual(getRightContextIter(dbHelper=self.testHelper,tableName=self.tableName,word="PUPA",distance=2,freq=True),{'GOAT': 0, 'HERBIVORE': 0, 'BIRD': 0, 'SHEEP': 0,'COW': 0, 'THE': 0, 'EATS': 0, 'A': 0, 'FLOWER': 0, 'VEGETABLE': 0, 'GRASS': 0, 'TOMATO': 0, 'PLANT': 0})
        docs = self.testHelper.getDocuments(self.tableName)
        self.assertEqual(getRightContextIter(dbHelper=self.testHelper,tableName=self.tableName,word="EATS",distance=1,allWords=["A","THE"],freq=True),{'A': 9/16, 'THE': 7/16})
        self.assertEqual(getRightContextIter(dbHelper=self.testHelper,tableName=self.tableName,word="THE",distance=1,allWords=["A","THE"],freq=True),{'A': 0, 'THE': 0})
        self.assertEqual(getRightContextIter(dbHelper=self.testHelper,tableName=self.tableName,word="EATS",distance=2,allWords=["A","THE"],freq=True),{'A': 9/32, 'THE': 7/32})
        self.assertEqual(getRightContextIter(dbHelper=self.testHelper,tableName=self.tableName,word="PUPA",distance=2,allWords=["A","THE"],freq=True),{'A': 0, 'THE': 0})
        self.assertEqual(getRightContextIter(dbHelper=self.testHelper,tableName=self.tableName,word="PUPA",distance=2,allWords=["A","THE","PUPA"],freq=True),{'A': 0, 'THE': 0,'PUPA' : 0})

    def test_getWindowContext(self):
        docs = self.testHelper.getDocuments(self.tableName)
        self.assertEqual(getWindowContext(documents=docs,word="EATS",distance=1,freq=True),{'GOAT' : 3/32 , 'HERBIVORE' : 8/32 , 'BIRD' : 1/32 , 'SHEEP' : 1/32 ,'COW' : 3/32 ,'EATS' : 0/32 ,'THE' : 7/32 ,'A' : 9/32 ,'FLOWER' : 0/32 ,'VEGETABLE' : 0/32 ,'GRASS' : 0/32 ,'PLANT' : 0/32 ,'TOMATO' : 0/32})
        self.assertEqual(getWindowContext(documents=docs,word="EATS",distance=2,freq=True),{'GOAT' : 3/64 , 'HERBIVORE' : 8/64 , 'BIRD' : 1/64 , 'SHEEP' : 1/64 , 'COW' : 3/64 , 'EATS' : 0/64 , 'THE' : 12/64 , 'A' : 20/64 , 'FLOWER' : 4/64 , 'VEGETABLE' : 2/64 , 'GRASS' : 2/64 , 'PLANT' : 7/64 , 'TOMATO' : 1/64 })
        self.assertEqual(getWindowContext(documents=docs,word="PUPA",distance=2,freq=True),{'GOAT': 0, 'HERBIVORE': 0, 'BIRD': 0, 'SHEEP': 0,'COW': 0, 'THE': 0, 'EATS': 0, 'A': 0, 'FLOWER': 0, 'VEGETABLE': 0, 'GRASS': 0, 'TOMATO': 0, 'PLANT': 0})
        #docs = self.testHelper.getDocuments(self.tableName)
        self.assertEqual(getWindowContext(documents=docs,word="EATS",distance=2,allWords=["A","THE"],freq=True),{'A': 20/32, 'THE': 12/32})
        self.assertEqual(getWindowContext(documents=docs,word="EATS",distance=1,allWords=["EATS"],freq=True),{'EATS': 0})
        self.assertEqual(getWindowContext(documents=docs,word="PUPA",distance=2,allWords=["A","THE"],freq=True),{'A': 0, 'THE': 0})
        self.assertEqual(getWindowContext(documents=docs,word="PUPA",distance=2,allWords=["A","THE","PUPA"],freq=True),{'A': 0, 'THE': 0,'PUPA' : 0})


    def test_getWindowContextIter(self):
        docs = self.testHelper.getDocuments(self.tableName)
        self.assertEqual(getWindowContextIter(dbHelper=self.testHelper,tableName=self.tableName,word="EATS",distance=1,freq=True),{'GOAT' : 3/32 , 'HERBIVORE' : 8/32 , 'BIRD' : 1/32 , 'SHEEP' : 1/32 ,'COW' : 3/32 ,'EATS' : 0/32 ,'THE' : 7/32 ,'A' : 9/32 ,'FLOWER' : 0/32 ,'VEGETABLE' : 0/32 ,'GRASS' : 0/32 ,'PLANT' : 0/32 ,'TOMATO' : 0/32})
        self.assertEqual(getWindowContextIter(dbHelper=self.testHelper,tableName=self.tableName,word="EATS",distance=2,freq=True),{'GOAT' : 3/64 , 'HERBIVORE' : 8/64 , 'BIRD' : 1/64 , 'SHEEP' : 1/64 , 'COW' : 3/64 , 'EATS' : 0/64 , 'THE' : 12/64 , 'A' : 20/64 , 'FLOWER' : 4/64 , 'VEGETABLE' : 2/64 , 'GRASS' : 2/64 , 'PLANT' : 7/64 , 'TOMATO' : 1/64 })
        self.assertEqual(getWindowContextIter(dbHelper=self.testHelper,tableName=self.tableName,word="PUPA",distance=2,freq=True),{'GOAT': 0, 'HERBIVORE': 0, 'BIRD': 0, 'SHEEP': 0,'COW': 0, 'THE': 0, 'EATS': 0, 'A': 0, 'FLOWER': 0, 'VEGETABLE': 0, 'GRASS': 0, 'TOMATO': 0, 'PLANT': 0})
        #docs = self.testHelper.getDocuments(self.tableName)
        self.assertEqual(getWindowContextIter(dbHelper=self.testHelper,tableName=self.tableName,word="EATS",distance=2,allWords=["A","THE"],freq=True),{'A': 20/32, 'THE': 12/32})
        self.assertEqual(getWindowContextIter(dbHelper=self.testHelper,tableName=self.tableName,word="EATS",distance=1,allWords=["EATS"],freq=True),{'EATS': 0})
        self.assertEqual(getWindowContextIter(dbHelper=self.testHelper,tableName=self.tableName,word="PUPA",distance=2,allWords=["A","THE"],freq=True),{'A': 0, 'THE': 0})
        self.assertEqual(getWindowContextIter(dbHelper=self.testHelper,tableName=self.tableName,word="PUPA",distance=2,allWords=["A","THE","PUPA"],freq=True),{'A': 0, 'THE': 0,'PUPA' : 0})

    
if __name__ == '__main__':
    unittest.main()
