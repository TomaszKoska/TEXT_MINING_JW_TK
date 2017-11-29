import unittest
from databaseHelpers.SqliteHelper import SqliteHelper
from dataModel.Document import Document
import os
import tempfile


class Test_SqliteHelper2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        try:
            os.remove(tempfile.gettempdir() + "/SomeTestDbBetterDontUseThisNameEverEverEverAgain.db")
        except:
            pass

        testHelper = SqliteHelper("D:/databases/SomeTestDbBetterDontUseThisNameEverEverEverAgain.db")
        tableName = "someTestNameThatYouShouldNOTUse"
        testHelper.start()
        testHelper.createDocumentTable(tableName)
        testDocs = []
        for i in range(1,10):
            testDocs.append(Document(title="TESTOWY TYTUŁ "+str(i),text="TESTOWY CONTENT! "+str(i),date="2017-08-05",source="www.wp.pl"))
        testDocs.append(Document(title="TESTOWY TYTUŁ!@#$%^&*(),_./\'\"",text="TESTOWY CONTENT!!@#$%^&,*()_./\'\"",date="2017-08-05!@#$%,^&*()_./\'\"",source="www.wp.pl!@#$%^&*()_./,\'\""))
        
        for d in testDocs:
            testHelper.saveDocument(d,tableName)


        testHelper.close()
    @classmethod
    def tearDownClass(cls):
        os.remove("D:/databases/SomeTestDbBetterDontUseThisNameEverEverEverAgain.db")


    def setUp(self):
        self.testHelper = SqliteHelper("D:/databases/SomeTestDbBetterDontUseThisNameEverEverEverAgain.db")
        self.tableName = "someTestNameThatYouShouldNOTUse"
        self.testHelper.start()

    def tearDown(self):
        self.testHelper.close()

    def test_SqliteHelp(self):
        pass

    #def test_SaveDocument(self):
    #    testDocs = []
    #    for i in range(1,10):
    #        testDocs.append(Document(title="TESTOWY TYTUŁ "+str(i),text="TESTOWY CONTENT! "+str(i),date="2017-08-05",source="www.wp.pl"))
    #    testDocs.append(Document(title="TESTOWY TYTUŁ!@#$%^&*(),_./\'\"",text="TESTOWY CONTENT!!@#$%^&,*()_./\'\"",date="2017-08-05!@#$%,^&*()_./\'\"",source="www.wp.pl!@#$%^&*()_./,\'\""))
        
    #    for d in testDocs:
    #        self.testHelper.saveDocument(d,self.tableName)

    def test_getDocuments(self):
        testDocs = []
        for i in range(1,10):
            testDocs.append(Document(title="TESTOWY TYTUŁ "+str(i),text="TESTOWY CONTENT! "+str(i),date="2017-08-05",source="www.wp.pl"))
        testDocs.append(Document(title="TESTOWY TYTUŁ!@#$%^&*(),_./\'\"",text="TESTOWY CONTENT!!@#$%^&,*()_./\'\"",date="2017-08-05!@#$%,^&*()_./\'\"",source="www.wp.pl!@#$%^&*()_./,\'\"")) 
        docsExtracted = self.testHelper.getDocuments(self.tableName)

        print(len(docsExtracted))
        print(len(testDocs))

        self.assertEqual(len(docsExtracted),len(testDocs))

        for i in range(0,len(docsExtracted)):
        #    print(testDocs[i].title)
        #    print(testDocs[i].text)
        #    print(testDocs[i].date)
        #    print(testDocs[i].source)
        #    print("\n\n\n")
        #    print(docsExtracted[i].title)
        #    print(docsExtracted[i].text)
        #    print(docsExtracted[i].date)
        #    print(docsExtracted[i].source)

            self.assertEqual(docsExtracted[i] == testDocs[i],True)
    
    def test_Iterator(self):
        testDocs = []
        for i in range(1,10):
            testDocs.append(Document(title="TESTOWY TYTUŁ "+str(i),text="TESTOWY CONTENT! "+str(i),date="2017-08-05",source="www.wp.pl"))
        testDocs.append(Document(title="TESTOWY TYTUŁ!@#$%^&*(),_./\'\"",text="TESTOWY CONTENT!!@#$%^&,*()_./\'\"",date="2017-08-05!@#$%,^&*()_./\'\"",source="www.wp.pl!@#$%^&*()_./,\'\"")) 


        self.testHelper.startIterator(self.tableName)
        docsExtracted = []
        try:
            while(True):
                docsExtracted.append(self.testHelper.getNextDocument())
                #print("!")
        except StopIteration:

            self.testHelper.stopIterator()

        for i in range(0,len(docsExtracted)):
            print(docsExtracted[i].title)
            print(docsExtracted[i].text)
            print(docsExtracted[i].date)
            print(docsExtracted[i].source)
            self.assertEqual(docsExtracted[i]== testDocs[i],True)

    #def test_IteratorOnEmptyFile(self):
    #    emptyHelper = CsvHelper("D:/databases/csv")
    #    emptyName = "emptyTestDatabase"
    #    emptyHelper.createDocumentTable(emptyName)
    #    emptyHelper.startIterator(emptyName)

    #    docsExtracted = []
    #    try:
    #        while(True):
    #            docsExtracted.append(emptyHelper.getNextDocument())
    #    except StopIteration:
    #        emptyHelper.stopIterator()
    #    self.assertEqual(len(docsExtracted),0)

if __name__ == '__main__':
    unittest.main()
