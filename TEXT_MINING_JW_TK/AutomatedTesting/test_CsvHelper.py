import unittest
from dataModel.Document import Document
from databaseHelpers.CsvHelper import CsvHelper

class Test_CsvHelper(unittest.TestCase):
    def setUp(self):
        self.testHelper = CsvHelper("D:/databases/csv")
        self.tableName = "someTestNameThatYouShouldNOTUse"
        self.testHelper.createDocumentTable(self.tableName)
        
        self.testDocs = []
        for i in range(1,10):
            self.testDocs.append(Document("TESTOWY TYTUŁ "+str(i),"TESTOWY CONTENT! "+str(i),"2017-08-05","www.wp.pl"))

        self.testDocs.append(Document("TESTOWY TYTUŁ!@#$%^&*(),_./\'\"","TESTOWY CONTENT!!@#$%^&,*()_./\'\"","2017-08-05!@#$%,^&*()_./\'\"","www.wp.pl!@#$%^&*()_./,\'\""))
        
        for d in self.testDocs:
            self.testHelper.saveDocument(d,self.tableName)

    def tearDown(self):
        self.testHelper.close()

    def test_CsvHelper(self):
        pass

    def test_eq(self):
        d1 = Document("1","2","3","4")
        d2 = Document("1","2","3","4")

        self.assertEqual(d1== d2,True)

    def test_getDocuments(self):
        docsExtracted = self.testHelper.getDocuments(self.tableName)
        
        print(docsExtracted.count)
        print(self.testDocs.count)

        for i in range(0,len(docsExtracted)):
            self.assertEqual(docsExtracted[i]== self.testDocs[i],True)
    
    def test_Iterator(self):
        self.testHelper.startIterator(self.tableName)
        docsExtracted = []
        try:
            while(True):
                docsExtracted.append(self.testHelper.getNextDocument())
        except StopIteration:
            self.testHelper.stopIterator()

        for i in range(0,len(docsExtracted)):
            self.assertEqual(docsExtracted[i]== self.testDocs[i],True)

    def test_IteratorOnEmptyFile(self):
        emptyHelper = CsvHelper("D:/databases/csv")
        emptyName = "emptyTestDatabase"
        emptyHelper.createDocumentTable(emptyName)
        emptyHelper.startIterator(emptyName)

        docsExtracted = []
        try:
            while(True):
                docsExtracted.append(emptyHelper.getNextDocument())
        except StopIteration:
            emptyHelper.stopIterator()
        self.assertEqual(len(docsExtracted),0)

if __name__ == '__main__':
    unittest.main()
