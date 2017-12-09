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

    def test_getWordProbability(self):
        docs = self.testHelper.getDocuments(self.tableName)
        aw = getAllWords(docs)
        expected = {'THE' : 0.722222222222222,'DOG' : 0.555555555555556,'GOES' : 0.0555555555555556,'TO' : 0.0555555555555556,'A' : 0.444444444444444,'VET' : 0.0555555555555556,'BECAUSE' : 0.0555555555555556,'HE' : 0.444444444444444,'IS' : 0.333333333333333,'VERY' : 0.0555555555555556,'SICK' : 0.222222222222222,'HOPES' : 0.0555555555555556,'GET' : 0.0555555555555556,'SOME' : 0.0555555555555556,'MEDICINE' : 0.222222222222222,'NICE' : 0.0555555555555556,'PET' : 0.0555555555555556,'RUNS' : 0.166666666666667,'AND' : 0.277777777777778,'CHASES' : 0.222222222222222,'CATS' : 0.0555555555555556,'PLAYS' : 0.0555555555555556,'ALL' : 0.0555555555555556,'DAY' : 0.0555555555555556,'LONG' : 0.0555555555555556,'SO' : 0.166666666666667,'FRIENDLY' : 0.0555555555555556,'TRUCKS' : 0.0555555555555556,'UNTIL' : 0.0555555555555556,'DIES' : 0.0555555555555556,'TODAY' : 0.166666666666667,'ATTACKED' : 0.0555555555555556,'ME' : 0.166666666666667,'KILLED' : 0.222222222222222,'MY' : 0.111111111111111,'RAT' : 0.0555555555555556,'WE' : 0.0555555555555556,'GENERALLY' : 0.0555555555555556,'KEEP' : 0.0555555555555556,'DOGS' : 0.0555555555555556,'FOR' : 0.111111111111111,'PROTECTION' : 0.111111111111111,'BITES' : 0.222222222222222,'KNOW' : 0.0555555555555556,'ONE' : 0.0555555555555556,'WHO' : 0.0555555555555556,'ALWAYS' : 0.0555555555555556,'BURGLARS' : 0.0555555555555556,'AWAY' : 0.0555555555555556,'I' : 0.111111111111111,'HAD' : 0.0555555555555556,'IT' : 0.166666666666667,'WAS' : 0.166666666666667,'BEAST' : 0.0555555555555556,'DOCTOR' : 0.222222222222222,'GAVE' : 0.0555555555555556,'NOT' : 0.166666666666667,'TASTY' : 0.0555555555555556,'BUT' : 0.0555555555555556,'HEALS' : 0.166666666666667,'WOUND' : 0.0555555555555556,'TOLD' : 0.0555555555555556,'THAT' : 0.166666666666667,'AM' : 0.0555555555555556,'ACTUALLY' : 0.0555555555555556,'FOND' : 0.0555555555555556,'OF' : 0.0555555555555556,'HIS' : 0.111111111111111,'SAYS' : 0.0555555555555556,'THIS' : 0.111111111111111,'SIMPLY' : 0.0555555555555556,'PEOPLE' : 0.0555555555555556,'WHY' : 0.0555555555555556,'WOULD' : 0.0555555555555556,'YOU' : 0.0555555555555556,'LIKE' : 0.0555555555555556,'DOCTORS' : 0.0555555555555556,'ARE' : 0.111111111111111,'ALMOST' : 0.0555555555555556,'SURE' : 0.0555555555555556,'SHOULD' : 0.0555555555555556,'BE' : 0.0555555555555556,'APPLIED' : 0.0555555555555556,'MURDERER' : 0.111111111111111,'FOLLOWING' : 0.0555555555555556,'CRIMINALS' : 0.0555555555555556,'KNOWN' : 0.0555555555555556,'BURGLAR' : 0.0555555555555556,'RAPIST' : 0.0555555555555556,'GUY' : 0.0555555555555556,'JUST' : 0.0555555555555556,'SOMEBODY' : 0.111111111111111,'MAN' : 0.0555555555555556,'BLOOD' : 0.111111111111111,'EVERYWHERE' : 0.0555555555555556,'DRUNK' : 0.0555555555555556,'AFTER' : 0.0555555555555556}
        for w in aw:
            self.assertAlmostEqual(getWordProbability(word=w,documents=docs),expected[w])

    def test_getWordEntrophy(self):
        docs = self.testHelper.getDocuments(self.tableName)
        aw = getAllWords(docs)
        expected = {'THE' : 0.852405178649479,'DOG' : 0.991076059838222,'GOES' : 0.309543429150325,'TO' : 0.309543429150325,'A' : 0.991076059838222,'VET' : 0.309543429150325,'BECAUSE' : 0.309543429150325,'HE' : 0.991076059838222,'IS' : 0.91829583405449,'VERY' : 0.309543429150325,'SICK' : 0.76420450650862,'HOPES' : 0.309543429150325,'GET' : 0.309543429150325,'SOME' : 0.309543429150325,'MEDICINE' : 0.76420450650862,'NICE' : 0.309543429150325,'PET' : 0.309543429150325,'RUNS' : 0.650022421648354,'AND' : 0.852405178649479,'CHASES' : 0.76420450650862,'CATS' : 0.309543429150325,'PLAYS' : 0.309543429150325,'ALL' : 0.309543429150325,'DAY' : 0.309543429150325,'LONG' : 0.309543429150325,'SO' : 0.650022421648354,'FRIENDLY' : 0.309543429150325,'TRUCKS' : 0.309543429150325,'UNTIL' : 0.309543429150325,'DIES' : 0.309543429150325,'TODAY' : 0.650022421648354,'ATTACKED' : 0.309543429150325,'ME' : 0.650022421648354,'KILLED' : 0.76420450650862,'MY' : 0.503258334775646,'RAT' : 0.309543429150325,'WE' : 0.309543429150325,'GENERALLY' : 0.309543429150325,'KEEP' : 0.309543429150325,'DOGS' : 0.309543429150325,'FOR' : 0.503258334775646,'PROTECTION' : 0.503258334775646,'BITES' : 0.76420450650862,'KNOW' : 0.309543429150325,'ONE' : 0.309543429150325,'WHO' : 0.309543429150325,'ALWAYS' : 0.309543429150325,'BURGLARS' : 0.309543429150325,'AWAY' : 0.309543429150325,'I' : 0.503258334775646,'HAD' : 0.309543429150325,'IT' : 0.650022421648354,'WAS' : 0.650022421648354,'BEAST' : 0.309543429150325,'DOCTOR' : 0.76420450650862,'GAVE' : 0.309543429150325,'NOT' : 0.650022421648354,'TASTY' : 0.309543429150325,'BUT' : 0.309543429150325,'HEALS' : 0.650022421648354,'WOUND' : 0.309543429150325,'TOLD' : 0.309543429150325,'THAT' : 0.650022421648354,'AM' : 0.309543429150325,'ACTUALLY' : 0.309543429150325,'FOND' : 0.309543429150325,'OF' : 0.309543429150325,'HIS' : 0.503258334775646,'SAYS' : 0.309543429150325,'THIS' : 0.503258334775646,'SIMPLY' : 0.309543429150325,'PEOPLE' : 0.309543429150325,'WHY' : 0.309543429150325,'WOULD' : 0.309543429150325,'YOU' : 0.309543429150325,'LIKE' : 0.309543429150325,'DOCTORS' : 0.309543429150325,'ARE' : 0.503258334775646,'ALMOST' : 0.309543429150325,'SURE' : 0.309543429150325,'SHOULD' : 0.309543429150325,'BE' : 0.309543429150325,'APPLIED' : 0.309543429150325,'MURDERER' : 0.503258334775646,'FOLLOWING' : 0.309543429150325,'CRIMINALS' : 0.309543429150325,'KNOWN' : 0.309543429150325,'BURGLAR' : 0.309543429150325,'RAPIST' : 0.309543429150325,'GUY' : 0.309543429150325,'JUST' : 0.309543429150325,'SOMEBODY' : 0.503258334775646,'MAN' : 0.309543429150325,'BLOOD' : 0.503258334775646,'EVERYWHERE' : 0.309543429150325,'DRUNK' : 0.309543429150325,'AFTER' : 0.309543429150325}
        for w in aw:
            self.assertAlmostEqual(getWordEntrophy(word=w,documents=docs),expected[w])
            
    def test_getWordConditionalProbability(self):
        docs = self.testHelper.getDocuments(self.tableName)
        aw = getAllWords(docs)
        self.assertAlmostEqual(getWordConditionalProbability(word="NICE",conditionWord="A", documents=docs),0.125)
        self.assertAlmostEqual(getWordConditionalProbability(word="DAY",conditionWord="RUNS", documents=docs),0.333333333)
        self.assertAlmostEqual(getWordConditionalProbability(word="ONE",conditionWord="THE", documents=docs),0.076923077)
        self.assertAlmostEqual(getWordConditionalProbability(word="KILLED",conditionWord="TODAY", documents=docs),0.666666667)
        self.assertAlmostEqual(getWordConditionalProbability(word="NICE",conditionWord="A", documents=docs),0.125)
    
    def test_getWordConditionalEnthropy(self):
        docs = self.testHelper.getDocuments(self.tableName)
        aw = getAllWords(docs)
        self.assertAlmostEqual(getWordConditionalEntrophy(word="GOES",conditionWord="THE", documents=docs),0.391243564)



if __name__ == '__main__':
    unittest.main()
