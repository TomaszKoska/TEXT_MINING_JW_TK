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


    def test_getAllWordsIter(self):
        expectedOutcome = ["A","THE","GOAT","HERBIVORE","BIRD","SHEEP","COW","EATS","FLOWER","VEGETABLE","GRASS","PLANT","TOMATO"]
        outcome = getAllWordsIter(self.testHelper,self.tableName)
        self.assertEqual(len(list(set(outcome) - set(expectedOutcome))),0)


if __name__ == '__main__':
    unittest.main()
