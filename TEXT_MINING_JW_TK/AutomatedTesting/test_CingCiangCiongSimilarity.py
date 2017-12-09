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
        self.docs.append(Document(title="TEST!", text="THE DOG CHASES TRUCKS UNTIL HE DIES", date="", source=""))
        self.docs.append(Document(title="TEST!", text="TODAY A DOG ATTACKED ME HE KILLED MY RAT", date="", source=""))
        self.docs.append(Document(title="TEST!", text="WE GENERALLY KEEP DOGS FOR PROTECTION DOG BITES WE KNOW ONE WHO ALWAYS CHASES THE BURGLARS AWAY", date="", source=""))
        self.docs.append(Document(title="TEST!", text="I HAD A DOG AND IT WAS FOR PROTECTION", date="", source=""))
        self.docs.append(Document(title="TEST!", text="THE BEAST RUNS CHASES AND BITES", date="", source=""))
        self.docs.append(Document(title="TEST!", text="A DOCTOR GAVE ME A MEDICINE TODAY THE MEDICINE WAS NOT TASTY BUT IT HEALS ME", date="", source=""))
        self.docs.append(Document(title="TEST!", text="A DOG BITES AND THE WOUND HEALS", date="", source=""))
        self.docs.append(Document(title="TEST!", text="THE DOCTOR TOLD ME THAT I AM SICK", date="", source=""))
        self.docs.append(Document(title="TEST!", text="ACTUALLY THE DOCTOR IS NOT THAT FOND OF HIS DOG HE SAYS THE DOG BITES", date="", source=""))
        self.docs.append(Document(title="TEST!", text="THIS MEDICINE SIMPLY HEALS PEOPLE WHY WOULD YOU NOT LIKE IT", date="", source=""))
        self.docs.append(Document(title="TEST!", text="THE DOCTORS ARE ALMOST SURE THAT HE IS SO SICK MEDICINE SHOULD BE APPLIED", date="", source=""))
        self.docs.append(Document(title="TEST!", text="TODAY A MURDERER KILLED MY DOG", date="", source=""))
        self.docs.append(Document(title="TEST!", text="THE FOLLOWING CRIMINALS ARE KNOWN THE BURGLAR THE MURDERER THE RAPIST", date="", source=""))
        self.docs.append(Document(title="TEST!", text="A GUY JUST KILLED SOMEBODY MAN THE BLOOD WAS EVERYWHERE", date="", source=""))
        self.docs.append(Document(title="TEST!", text="SOMEBODY KILLED THE DOCTOR HE DRUNK HIS BLOOD AFTER THIS IS SO SICK", date="", source=""))

        for d in self.docs:
            self.testHelper.saveDocument(d,self.tableName)

    def tearDown(self):
        self.testHelper.close()
    
    def test_basicSimilarity(self):
        docs = self.testHelper.getDocuments(self.tableName)
        d1 = docs[0]
        d2 = docs[1]
        d3 = docs[17]
        aw = getAllWords([d1,d2,d3])
        c1 = getWordsCount(d1,aw)
        c2 = getWordsCount(d2,aw)
        c3 = getWordsCount(d3,aw)
        sim12 = basicSimilarity(wordCountList=c1,wordCountList2=c2,allWords=aw)
        sim13 = basicSimilarity(wordCountList=c1,wordCountList2=c3,allWords=aw)
        sim23 = basicSimilarity(wordCountList=c2,wordCountList2=c3,allWords=aw)

        self.assertAlmostEqual(sim12,0.029411765)
        self.assertAlmostEqual(sim13,0.022624434)
        self.assertAlmostEqual(sim23,0.012820513)

    def test_idfSimilarity(self):
        docs = self.testHelper.getDocuments(self.tableName)
        d1 = docs[0]
        d2 = docs[1]
        d3 = docs[17]
        aw = getAllWords([d1,d2,d3])
        idf = getIdf([d1,d2,d3],aw)
        c1 = getWordsCount(d1,aw)
        c2 = getWordsCount(d2,aw)
        c3 = getWordsCount(d3,aw)
        sim12 = idfSimilarity(wordCountList=c1,wordCountList2=c2,idf=idf)
        sim13 = idfSimilarity(wordCountList=c1,wordCountList2=c3,idf=idf)
        sim23 = idfSimilarity(wordCountList=c2,wordCountList2=c3,idf=idf)

        self.assertAlmostEqual(sim12,0.01442396)
        self.assertAlmostEqual(sim13,0.010178012)
        self.assertAlmostEqual(sim23,0.003688232)

    def test_getIdf(self):
        docs = self.testHelper.getDocuments(self.tableName)
        aw = getAllWords(docs)
        idf=getIdf(docs,aw)
        #print(idf)
        expected= {'THE' : 0.379489621704904,'DOG' : 0.641853886172395,'GOES' : 2.94443897916644,'TO' : 2.94443897916644,'A' : 0.864997437486605,'VET' : 2.94443897916644,'BECAUSE' : 2.94443897916644,'HE' : 0.864997437486605,'IS' : 1.15267950993839,'VERY' : 2.94443897916644,'SICK' : 1.55814461804655,'HOPES' : 2.94443897916644,'GET' : 2.94443897916644,'SOME' : 2.94443897916644,'MEDICINE' : 1.55814461804655,'NICE' : 2.94443897916644,'PET' : 2.94443897916644,'RUNS' : 1.84582669049833,'AND' : 1.33500106673234,'CHASES' : 1.55814461804655,'CATS' : 2.94443897916644,'PLAYS' : 2.94443897916644,'ALL' : 2.94443897916644,'DAY' : 2.94443897916644,'LONG' : 2.94443897916644,'SO' : 1.84582669049833,'FRIENDLY' : 2.94443897916644,'TRUCKS' : 2.94443897916644,'UNTIL' : 2.94443897916644,'DIES' : 2.94443897916644,'TODAY' : 1.84582669049833,'ATTACKED' : 2.94443897916644,'ME' : 1.84582669049833,'KILLED' : 1.55814461804655,'MY' : 2.2512917986065,'RAT' : 2.94443897916644,'WE' : 2.94443897916644,'GENERALLY' : 2.94443897916644,'KEEP' : 2.94443897916644,'DOGS' : 2.94443897916644,'FOR' : 2.2512917986065,'PROTECTION' : 2.2512917986065,'BITES' : 1.55814461804655,'KNOW' : 2.94443897916644,'ONE' : 2.94443897916644,'WHO' : 2.94443897916644,'ALWAYS' : 2.94443897916644,'BURGLARS' : 2.94443897916644,'AWAY' : 2.94443897916644,'I' : 2.2512917986065,'HAD' : 2.94443897916644,'IT' : 1.84582669049833,'WAS' : 1.84582669049833,'BEAST' : 2.94443897916644,'DOCTOR' : 1.55814461804655,'GAVE' : 2.94443897916644,'NOT' : 1.84582669049833,'TASTY' : 2.94443897916644,'BUT' : 2.94443897916644,'HEALS' : 1.84582669049833,'WOUND' : 2.94443897916644,'TOLD' : 2.94443897916644,'THAT' : 1.84582669049833,'AM' : 2.94443897916644,'ACTUALLY' : 2.94443897916644,'FOND' : 2.94443897916644,'OF' : 2.94443897916644,'HIS' : 2.2512917986065,'SAYS' : 2.94443897916644,'THIS' : 2.2512917986065,'SIMPLY' : 2.94443897916644,'PEOPLE' : 2.94443897916644,'WHY' : 2.94443897916644,'WOULD' : 2.94443897916644,'YOU' : 2.94443897916644,'LIKE' : 2.94443897916644,'DOCTORS' : 2.94443897916644,'ARE' : 2.2512917986065,'ALMOST' : 2.94443897916644,'SURE' : 2.94443897916644,'SHOULD' : 2.94443897916644,'BE' : 2.94443897916644,'APPLIED' : 2.94443897916644,'MURDERER' : 2.2512917986065,'FOLLOWING' : 2.94443897916644,'CRIMINALS' : 2.94443897916644,'KNOWN' : 2.94443897916644,'BURGLAR' : 2.94443897916644,'RAPIST' : 2.94443897916644,'GUY' : 2.94443897916644,'JUST' : 2.94443897916644,'SOMEBODY' : 2.2512917986065,'MAN' : 2.94443897916644,'BLOOD' : 2.2512917986065,'EVERYWHERE' : 2.94443897916644,'DRUNK' : 2.94443897916644,'AFTER' : 2.94443897916644}
        for w in idf.keys():
            self.assertAlmostEqual(idf[w],expected[w])

    def test_bm25Similarity(self):
        docs = self.testHelper.getDocuments(self.tableName)
        d1 = docs[0]
        d2 = docs[1]
        d3 = docs[17]
        aw = getAllWords([d1,d2,d3])
        idf = getIdf([d1,d2,d3],aw)
        #print(idf)
        c1 = getWordsCount(d1,aw)
        c2 = getWordsCount(d2,aw)
        c3 = getWordsCount(d3,aw)
        

        adl = (sum(c1.values())+sum(c2.values())+sum(c3.values()))/3.0
        

        sim12 = bm25Similarity(wordCountList=c1,wordCountList2=c2,idf=idf,k=100,b=0.5,avgDocLength=adl)
        sim13 = bm25Similarity(wordCountList=c1,wordCountList2=c3,idf=idf,k=100,b=0.5,avgDocLength=adl)
        sim23 = bm25Similarity(wordCountList=c2,wordCountList2=c3,idf=idf,k=100,b=0.5,avgDocLength=adl)

        self.assertAlmostEqual(sim12,0.014407898)
        self.assertAlmostEqual(sim13,0.010176157)
        self.assertAlmostEqual(sim23,0.003701238)


    def test_documentsSimilarity(self):
        docs = self.testHelper.getDocuments(self.tableName)
        d1 = docs[0]
        d2 = docs[1]
        d3 = docs[17]
        aw = getAllWords([d1,d2,d3])
        sim12 = documentsSimilarity(document1=d1,document2=d2,allWords=aw,similarityFunction=basicSimilarity)
        sim13 = documentsSimilarity(document1=d1,document2=d3,allWords=aw,similarityFunction=basicSimilarity)
        sim23 = documentsSimilarity(document1=d2,document2=d3,allWords=aw,similarityFunction=basicSimilarity)
        self.assertAlmostEqual(sim12,0.029411765)
        self.assertAlmostEqual(sim13,0.022624434)
        self.assertAlmostEqual(sim23,0.012820513)
        idf = getIdf([d1,d2,d3],aw)

        sim12 = documentsSimilarity(document1=d1,document2=d2,allWords=aw,similarityFunction=idfSimilarity,idf=idf)
        sim13 = documentsSimilarity(document1=d1,document2=d3,allWords=aw,similarityFunction=idfSimilarity,idf=idf)
        sim23 = documentsSimilarity(document1=d2,document2=d3,allWords=aw,similarityFunction=idfSimilarity,idf=idf)
        self.assertAlmostEqual(sim12,0.01442396)
        self.assertAlmostEqual(sim13,0.010178012)
        self.assertAlmostEqual(sim23,0.003688232)

        adl = (sum(getWordsCount(d1,aw).values())+sum(getWordsCount(d2,aw).values())+sum(getWordsCount(d3,aw).values()))/3.0
        
        
        sim12 = documentsSimilarity(document1=d1,document2=d2,allWords=aw,similarityFunction=bm25Similarity,idf=idf,k=100,b=0.5,avgDocLength=adl)
        sim13 = documentsSimilarity(document1=d1,document2=d3,allWords=aw,similarityFunction=bm25Similarity,idf=idf,k=100,b=0.5,avgDocLength=adl)
        sim23 = documentsSimilarity(document1=d2,document2=d3,allWords=aw,similarityFunction=bm25Similarity,idf=idf,k=100,b=0.5,avgDocLength=adl)

        self.assertAlmostEqual(sim12,0.014407898)
        self.assertAlmostEqual(sim13,0.010176157)
        self.assertAlmostEqual(sim23,0.003701238)



if __name__ == '__main__':
    unittest.main()
