import unittest
from databaseHelpers.CsvHelper import CsvHelper
from cingCiangCiong.Similarity import *

class test_CingCiangCiongSimilarity(unittest.TestCase):

    def setUp(self):
        self.testHelper = CsvHelper(tempfile.gettempdir())
        self.tableName = "someTestNameThatYouShouldNOTUse"
        self.testHelper.createDocumentTable(self.tableName)
        
        self.docs = []
        self.docs.append(Document(title="TEST!", text="THE DOG GOES TO A VET BECAUSE HE IS VERY SICK HE HOPES TO GET SOME MEDICINE", date="", source=""))
        self.docs.append(Document(title="TEST!", text="A DOG IS A NICE PET HE RUNS AND RUNS CHASES CATS", date="", source=""))
        self.docs.append(Document(title="TEST!", text="THE DOG RUNS AND PLAYS ALL DAY LONG HE IS SO FRIENDLY", date="", source=""))
        self.docs.append(Document(title="TEST!", text="THE DOG CHASES  TRUCKS UNTIL HE DIES", date="", source=""))
        self.docs.append(Document(title="TEST!", text="TODAY A DOG ATTACKED ME HE KILLED MY RAT", date="", source=""))
        self.docs.append(Document(title="TEST!", text="WE GENERALLY KEEP DOGS FOR PROTECTION DOG BITES WE KNOW ONE WHO ALWAYS CHASES THE BURGLARS AWAY", date="", source=""))
        self.docs.append(Document(title="TEST!", text="I HAD A DOG AND IT WAS FOR PROTECTION", date="", source=""))
        self.docs.append(Document(title="TEST!", text="THE BEAST RUNS CHASES AND BITES", date="", source=""))
        self.docs.append(Document(title="TEST!", text="A DOCTOR GAVE ME A MEDICINE TODAY THE MEDICINE WAS NOT TASTY BUT IT HEALS ME", date="", source=""))
        self.docs.append(Document(title="TEST!", text="A DOG BITES AND THE WOUND HEALS", date="", source=""))
        self.docs.append(Document(title="TEST!", text="THE DOCTOR TOLD ME THAT I AM SICK", date="", source=""))
        self.docs.append(Document(title="TEST!", text="ACTUALLY THE DOCTOR IS NOT THAT FOND OF HIS DOG HE SAYS THE DOG BITES", date="", source=""))
        self.docs.append(Document(title="TEST!", text="THIS MEDICINE SIMPLY HEALS PEOPLE… WHY WOULD YOU NOT LIKE IT?", date="", source=""))
        self.docs.append(Document(title="TEST!", text="THE DOCTORS ARE ALMOST SURE THAT HE IS SO SICK MEDICINE SHOULD BE APPLIED", date="", source=""))
        self.docs.append(Document(title="TEST!", text="TODAY A MURDERER KILLED MY DOG", date="", source=""))
        self.docs.append(Document(title="TEST!", text="THE FOLLOWING CRIMINALS ARE KNOWN THE BURGLAR THE MURDERER THE RAPIST", date="", source=""))
        self.docs.append(Document(title="TEST!", text="A GUY JUST KILLED SOMEBODY MAN THE BLOOD WAS EVERYWHERE", date="", source=""))
        self.docs.append(Document(title="TEST!", text="SOMEBODY KILLED THE DOCTOR HE DRUNK HIS BLOOD AFTER THIS IS SO SICK", date="", source=""))

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
