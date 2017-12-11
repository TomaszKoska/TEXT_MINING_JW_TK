import unittest
import os
import tempfile

from databaseHelpers.CsvHelper import CsvHelper
from dataModel.Document import Document
from dataModel.TextTopic import TextTopic

class Test_CsvHelper2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        try:
            os.remove(tempfile.gettempdir() + "/docs.csv")
            os.remove(tempfile.gettempdir() + "/tops.csv")
        except:
            pass
        testHelper = CsvHelper(tempfile.gettempdir())
        testHelper.start()
        tableName = "docs"
        topicTableName = "tops"
        testHelper.createDocumentTable( tableName)
        testHelper.createTopicTable( topicTableName)

        docs = []
        docs.append(Document(title="DOG1", text="THE DOG GOES TO A VET BECAUSE HE IS VERY SICK HE HOPES TO GET SOME MEDICINE", date="", source="",label="DOG"))
        docs.append(Document(title="DOG2", text="A DOG IS A NICE PET HE RUNS AND RUNS CHASES CATS", date="", source="",label="DOG"))
        docs.append(Document(title="DOG3", text="THE DOG RUNS AND PLAYS ALL DAY LONG HE IS SO FRIENDLY", date="", source="",label="DOG"))
        docs.append(Document(title="DOG4", text="THE DOG CHASES TRUCKS UNTIL HE DIES", date="", source="",label="DOG"))
        docs.append(Document(title="DOG5", text="TODAY A DOG ATTACKED ME HE KILLED MY RAT", date="", source="",label="DOG"))
        docs.append(Document(title="DOG6", text="WE GENERALLY KEEP DOGS FOR PROTECTION DOG BITES WE KNOW ONE WHO ALWAYS CHASES THE BURGLARS AWAY", date="", source="",label="DOG"))
        docs.append(Document(title="DOG7", text="I HAD A DOG AND IT WAS FOR PROTECTION", date="", source="",label="DOG"))
        docs.append(Document(title="DOG8", text="THE BEAST RUNS CHASES AND BITES", date="", source="",label="DOG"))
        docs.append(Document(title="DOC1", text="A DOCTOR GAVE ME A MEDICINE TODAY THE MEDICINE WAS NOT TASTY BUT IT HEALS ME", date="", source="",label="DOCTOR'S LIFE"))
        docs.append(Document(title="DOC2", text="A DOG BITES AND THE WOUND HEALS", date="", source="",label="DOCTOR'S LIFE"))
        docs.append(Document(title="DOC3", text="THE DOCTOR TOLD ME THAT I AM SICK", date="", source="",label="DOCTOR'S LIFE"))
        docs.append(Document(title="DOC4", text="ACTUALLY THE DOCTOR IS NOT THAT FOND OF HIS DOG HE SAYS THE DOG BITES", date="", source="",label="DOCTOR'S LIFE"))
        docs.append(Document(title="DOC5", text="THIS MEDICINE SIMPLY HEALS PEOPLE WHY WOULD YOU NOT LIKE IT", date="", source="",label="DOCTOR'S LIFE"))
        docs.append(Document(title="DOC6", text="THE DOCTORS ARE ALMOST SURE THAT HE IS SO SICK MEDICINE SHOULD BE APPLIED", date="", source="",label="DOCTOR'S LIFE"))
        docs.append(Document(title="CRI1", text="TODAY A MURDERER KILLED MY DOG", date="", source="",label="CRIME"))
        docs.append(Document(title="CRI2", text="THE FOLLOWING CRIMINALS ARE KNOWN THE BURGLAR THE MURDERER THE RAPIST", date="", source="",label="CRIME"))
        docs.append(Document(title="CRI3", text="A GUY JUST KILLED SOMEBODY MAN THE BLOOD WAS EVERYWHERE", date="", source="",label="CRIME"))
        docs.append(Document(title="CRI4", text="SOMEBODY KILLED THE DOCTOR HE DRUNK HIS BLOOD AFTER THIS IS SO SICK", date="", source="",label="CRIME"))

        for d in  docs:
            testHelper.saveDocument(d, tableName)

    
    def setUp(self):
        self.testHelper = CsvHelper(tempfile.gettempdir())
        self.testHelper.start()
        self.tableName = "docs"
        self.topicTableName = "tops"
        self.testHelper.start()

    def tearDown(self):
        self.testHelper.close()

    def test_Topic(self):
        topic1 = TextTopic("DOG_TOPIC", {'DOG' : 10 , 'CAT' : 2, 'RUNS' : 5, 'CHASES' : 8})
        topic2 = TextTopic("CAT_TOPIC", {'CAT' : 10 , 'EATS' : 2, 'SLEEPS' : 5, 'SUCKS' : 8})

        self.testHelper.saveTopic(topic1, self.topicTableName)
        topic1out = self.testHelper.getTopics(self.topicTableName)["DOG_TOPIC"]
        print(topic1.wordDistributions)
        print(topic1out.wordDistributions)

        self.assertDictEqual(topic1.wordDistributions,topic1out.wordDistributions)


if __name__ == '__main__':
    unittest.main()
