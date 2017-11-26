from dataModel.Document import Document

class AbstractDatabaseHelper(object):
    """description of class"""

    def __init__(self, databesePath):
        pass

    def start(self):
        pass

    def close(self):
        pass

    def createDocumentTable(self,tableName=""):
        pass

    def saveDocument(self,document = Document(), tableName = ""):
        pass

    def getDocuments(self, tableName = ""):
        pass

    def startIterator(self):
        pass

    def getNextDocument(self):
        pass

    def stopIterator(self):
        pass