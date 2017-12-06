import unittest
from databaseHelpers.CsvHelper import CsvHelper
from cingCiangCiong.Similarity import *

class test_CingCiangCiongSimilarity(unittest.TestCase):

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
    
    #def test_basicSimilarity(self):
    #    raise NotImplementedError

    #def test_BM25Similarity(self):
    #    raise NotImplementedError

    #def test_getIDF(self):
    #    docs = self.testHelper.getDocuments(self.tableName)
    #    print(getIDF(docs))
    #    raise NotImplementedError
    
    def test_getIDFSimilarity(self):
        docs = self.testHelper.getDocuments(self.tableName)
        allWords = getAllWords(docs)
        idf = getIDF(documents = docs,allWords=allWords)
        
        wcs = []
        for d in docs:
            wcs.append(getWordsCount(documents = d, allWords=allWords))
        
        i=0
        for x in wcs:
            j=0
            for y in wcs:
                a =getIDFSimilarity(wordCountList = x, wordCountList2=y, idf=idf)
                print("checked doc :" +str(i) + " vs :" +str(j))
                print(x)
                print(y)
                print(a)
                j=j+1
            i=i+1
            self.assertEquals(1,0)

if __name__ == '__main__':
    unittest.main()
