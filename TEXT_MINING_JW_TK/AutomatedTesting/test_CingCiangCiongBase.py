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

    def test_getAllWordsIter(self):
        expectedOutcome = ["A","THE","GOAT","HERBIVORE","BIRD","SHEEP","COW","EATS","FLOWER","VEGETABLE","GRASS","PLANT","TOMATO"]
        outcome = getAllWordsIter(self.testHelper,self.tableName)
        self.assertEqual(len(list(set(outcome) - set(expectedOutcome))),0)
        self.assertEqual(len(list(set(expectedOutcome) - set(outcome))),0)

    def test_getWordsCountEmptyWordList(self):
        docs = self.testHelper.getDocuments(self.tableName)
        self.assertEqual(getWordsCount(documents=docs),{'A': 20, 'GOAT': 3, 'EATS': 16, 'THE': 12, 'FLOWER': 4, 'HERBIVORE': 8, 'BIRD': 1, 'VEGETABLE': 2, 'GRASS': 2, 'SHEEP': 1, 'PLANT': 7, 'COW': 3, 'TOMATO': 1})
    
    def test_getWordsCountSomeWordList(self):
        docs = self.testHelper.getDocuments(self.tableName)
        self.assertEqual(getWordsCount(documents=docs,allWords=["A","THE"]),{'A': 20, 'THE': 12})
    
    def test_getWordsCountSomeWordList2(self):
        docs = self.testHelper.getDocuments(self.tableName)
        self.assertEqual(getWordsCount(documents=docs,allWords=["A","THE","FOOOO"]),{'A': 20, 'THE': 12, 'FOOOO' : 0}) #great!!!
    
    def test_getWordsCountIterEmptyWordList(self):
        print(self.tableName)
        self.assertEqual(getWordsCountIter(dbHelper=self.testHelper,tableName=self.tableName),{'A': 20, 'GOAT': 3, 'EATS': 16, 'THE': 12, 'FLOWER': 4, 'HERBIVORE': 8, 'BIRD': 1, 'VEGETABLE': 2, 'GRASS': 2, 'SHEEP': 1, 'PLANT': 7, 'COW': 3, 'TOMATO': 1})
    
    def test_getWordsCountIterSomeWordList(self):
        self.assertEqual(getWordsCountIter(dbHelper=self.testHelper,tableName=self.tableName,allWords=["A","THE"]),{'A': 20, 'THE': 12})
    
    def test_getWordsCountIterSomeWordList2(self):
        self.assertEqual(getWordsCountIter(dbHelper=self.testHelper,tableName=self.tableName,allWords=["A","THE","FOOOO"]),{'A': 20, 'THE': 12, 'FOOOO' : 0}) #great!!!


    def test_getWordsFrequencyEmptyWordList(self):
        docs = self.testHelper.getDocuments(self.tableName)
        self.assertEqual(getWordsFrequency(documents=docs),{'A': 20/80, 'GOAT': 3/80, 'EATS': 16/80, 'THE': 12/80, 'FLOWER': 4/80, 'HERBIVORE': 8/80, 'BIRD': 1/80, 'VEGETABLE': 2/80, 'GRASS': 2/80, 'SHEEP': 1/80, 'PLANT': 7/80, 'COW': 3/80, 'TOMATO': 1/80})
    
    def test_getWordsFrequencySomeWordList(self):
        docs = self.testHelper.getDocuments(self.tableName)
        self.assertEqual(getWordsFrequency(documents=docs,allWords=["A","THE"]),{'A': 20/32, 'THE': 12/32})
    
    def test_getWordsFrequencySomeWordList2(self):
        docs = self.testHelper.getDocuments(self.tableName)
        self.assertEqual(getWordsFrequency(documents=docs,allWords=["A","THE","FOOOO"]),{'A': 20/32, 'THE': 12/32, 'FOOOO' : 0/32}) #great!!!


    def test_getWordsFrequencyIterEmptyWordList(self):
        docs = self.testHelper.getDocuments(self.tableName)
        self.assertEqual(getWordsFrequencyIter(dbHelper=self.testHelper,tableName=self.tableName),{'A': 20/80, 'GOAT': 3/80, 'EATS': 16/80, 'THE': 12/80, 'FLOWER': 4/80, 'HERBIVORE': 8/80, 'BIRD': 1/80, 'VEGETABLE': 2/80, 'GRASS': 2/80, 'SHEEP': 1/80, 'PLANT': 7/80, 'COW': 3/80, 'TOMATO': 1/80})
    
    def test_getWordsFrequencyIterSomeWordList(self):
        docs = self.testHelper.getDocuments(self.tableName)
        self.assertEqual(getWordsFrequencyIter(dbHelper=self.testHelper,tableName=self.tableName,allWords=["A","THE"]),{'A': 20/32, 'THE': 12/32})
    
    def test_getWordsFrequencyIterSomeWordList2(self):
        docs = self.testHelper.getDocuments(self.tableName)
        self.assertEqual(getWordsFrequencyIter(dbHelper=self.testHelper,tableName=self.tableName,allWords=["A","THE","FOOOO"]),{'A': 20/32, 'THE': 12/32, 'FOOOO' : 0/32}) #great!!!



    def test_getLeftContextEmptyWordList(self):
        docs = self.testHelper.getDocuments(self.tableName)
        self.assertEqual(getLeftContext(documents=docs,word="EATS",distance=1),{'GOAT': 0.1875, 'HERBIVORE': 0.5, 'BIRD': 0.0625, 'SHEEP': 0.0625, 'COW': 0.1875, 'THE': 0, 'EATS': 0, 'A': 0, 'FLOWER': 0, 'VEGETABLE': 0, 'GRASS': 0, 'TOMATO': 0, 'PLANT': 0})
        self.assertEqual(getLeftContext(documents=docs,word="THE",distance=1),{'GOAT': 0, 'HERBIVORE': 0, 'BIRD': 0, 'SHEEP': 0, 'COW': 0, 'THE': 0, 'EATS': 7/7, 'A': 0, 'FLOWER': 0, 'VEGETABLE': 0, 'GRASS': 0, 'TOMATO': 0, 'PLANT': 0})
        self.assertEqual(getLeftContext(documents=docs,word="THE",distance=2),{'GOAT': 2/14, 'HERBIVORE': 3/14, 'BIRD': 1/14, 'SHEEP': 1/14,'COW': 0, 'THE': 0, 'EATS': 7/14, 'A': 0, 'FLOWER': 0, 'VEGETABLE': 0, 'GRASS': 0, 'TOMATO': 0, 'PLANT': 0})
        self.assertEqual(getLeftContext(documents=docs,word="PUPA",distance=2),{'GOAT': 0, 'HERBIVORE': 0, 'BIRD': 0, 'SHEEP': 0,'COW': 0, 'THE': 0, 'EATS': 0, 'A': 0, 'FLOWER': 0, 'VEGETABLE': 0, 'GRASS': 0, 'TOMATO': 0, 'PLANT': 0})


    def test_getLeftContextSomeWordList(self):
        docs = self.testHelper.getDocuments(self.tableName)
        self.assertEqual(getLeftContext(documents=docs,word="EATS",distance=1,allWords=["GOAT","HERBIVORE"]),{'GOAT': 0.1875, 'HERBIVORE': 0.5})
        self.assertEqual(getLeftContext(documents=docs,word="THE",distance=1,allWords=["GOAT","HERBIVORE"]),{'GOAT': 0, 'HERBIVORE': 0})
        self.assertEqual(getLeftContext(documents=docs,word="THE",distance=2,allWords=["GOAT","HERBIVORE"]),{'GOAT': 2/14, 'HERBIVORE': 3/14})
        self.assertEqual(getLeftContext(documents=docs,word="PUPA",distance=2,allWords=["GOAT","HERBIVORE"]),{'GOAT': 0, 'HERBIVORE': 0})
        self.assertEqual(getLeftContext(documents=docs,word="PUPA",distance=2,allWords=["GOAT","HERBIVORE","PUPA"]),{'GOAT': 0, 'HERBIVORE': 0,'PUPA' : 0})


    def test_getLeftContextIterEmptyWordList(self):
        docs = self.testHelper.getDocuments(self.tableName)
        self.assertEqual(getLeftContextIter(dbHelper=self.testHelper,tableName=self.tableName,word="EATS",distance=1),{'GOAT': 0.1875, 'HERBIVORE': 0.5, 'BIRD': 0.0625, 'SHEEP': 0.0625, 'COW': 0.1875, 'THE': 0, 'EATS': 0, 'A': 0, 'FLOWER': 0, 'VEGETABLE': 0, 'GRASS': 0, 'TOMATO': 0, 'PLANT': 0})
        self.assertEqual(getLeftContextIter(dbHelper=self.testHelper,tableName=self.tableName,word="THE",distance=1),{'GOAT': 0, 'HERBIVORE': 0, 'BIRD': 0, 'SHEEP': 0, 'COW': 0, 'THE': 0, 'EATS': 7/7, 'A': 0, 'FLOWER': 0, 'VEGETABLE': 0, 'GRASS': 0, 'TOMATO': 0, 'PLANT': 0})
        self.assertEqual(getLeftContextIter(dbHelper=self.testHelper,tableName=self.tableName,word="THE",distance=2),{'GOAT': 2/14, 'HERBIVORE': 3/14, 'BIRD': 1/14, 'SHEEP': 1/14,'COW': 0, 'THE': 0, 'EATS': 7/14, 'A': 0, 'FLOWER': 0, 'VEGETABLE': 0, 'GRASS': 0, 'TOMATO': 0, 'PLANT': 0})
        self.assertEqual(getLeftContextIter(dbHelper=self.testHelper,tableName=self.tableName,word="PUPA",distance=2),{'GOAT': 0, 'HERBIVORE': 0, 'BIRD': 0, 'SHEEP': 0,'COW': 0, 'THE': 0, 'EATS': 0, 'A': 0, 'FLOWER': 0, 'VEGETABLE': 0, 'GRASS': 0, 'TOMATO': 0, 'PLANT': 0})


    def test_getLeftContextIterSomeWordList(self):
        docs = self.testHelper.getDocuments(self.tableName)
        self.assertEqual(getLeftContextIter(dbHelper=self.testHelper,tableName=self.tableName,word="EATS",distance=1,allWords=["GOAT","HERBIVORE"]),{'GOAT': 0.1875, 'HERBIVORE': 0.5})
        self.assertEqual(getLeftContextIter(dbHelper=self.testHelper,tableName=self.tableName,word="THE",distance=1,allWords=["GOAT","HERBIVORE"]),{'GOAT': 0, 'HERBIVORE': 0})
        self.assertEqual(getLeftContextIter(dbHelper=self.testHelper,tableName=self.tableName,word="THE",distance=2,allWords=["GOAT","HERBIVORE"]),{'GOAT': 2/14, 'HERBIVORE': 3/14})
        self.assertEqual(getLeftContextIter(dbHelper=self.testHelper,tableName=self.tableName,word="PUPA",distance=2,allWords=["GOAT","HERBIVORE"]),{'GOAT': 0, 'HERBIVORE': 0})
        self.assertEqual(getLeftContextIter(dbHelper=self.testHelper,tableName=self.tableName,word="PUPA",distance=2,allWords=["GOAT","HERBIVORE","PUPA"]),{'GOAT': 0, 'HERBIVORE': 0,'PUPA' : 0})
    

    
if __name__ == '__main__':
    unittest.main()
