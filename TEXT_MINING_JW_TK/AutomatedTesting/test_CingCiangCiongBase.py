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
    
    def test_getWordsCountSomeWordList(self):
        docs = self.testHelper.getDocuments(self.tableName)
        self.assertEqual(getWordsCount(documents=docs,allWords=["A","THE","FOOOO"]),{'A': 20, 'THE': 12, 'FOOOO' : 0}) #great!!!
    
    def test_getWordsCountIterEmptyWordList(self):
        print(self.tableName)
        self.assertEqual(getWordsCountIter(dbHelper=self.testHelper,tableName=self.tableName),{'A': 20, 'GOAT': 3, 'EATS': 16, 'THE': 12, 'FLOWER': 4, 'HERBIVORE': 8, 'BIRD': 1, 'VEGETABLE': 2, 'GRASS': 2, 'SHEEP': 1, 'PLANT': 7, 'COW': 3, 'TOMATO': 1})
    
    def test_getWordsCountIterSomeWordList(self):
        self.assertEqual(getWordsCountIter(dbHelper=self.testHelper,tableName=self.tableName,allWords=["A","THE"]),{'A': 20, 'THE': 12})
    
    def test_getWordsCountIterSomeWordList(self):
        self.assertEqual(getWordsCountIter(dbHelper=self.testHelper,tableName=self.tableName,allWords=["A","THE","FOOOO"]),{'A': 20, 'THE': 12, 'FOOOO' : 0}) #great!!!

if __name__ == '__main__':
    unittest.main()
