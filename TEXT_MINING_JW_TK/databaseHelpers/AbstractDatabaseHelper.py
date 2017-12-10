from dataModel.Document import Document
from dataModel.TextTopic import TextTopic

class AbstractDatabaseHelper(object):
    """description of class"""

    def __init__(self, databesePath):
        raise NotImplementedError

    def start(self):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError

    def createDocumentTable(self,tableName=""):
        raise NotImplementedError

    def saveDocument(self,document = Document(), tableName = ""):
        raise NotImplementedError

    def getDocuments(self, tableName = ""):
        raise NotImplementedError

    def startIterator(self):
        raise NotImplementedError

    def getNextDocument(self):
        raise NotImplementedError

    def stopIterator(self):
        raise NotImplementedError

    def createTopicTable(self,tableName=""):
        raise NotImplementedError

    def saveTopic(self,topic = TextTopic(), tableName = ""):
        raise NotImplementedError

    def getTopics(self, tableName = ""):
        raise NotImplementedError
