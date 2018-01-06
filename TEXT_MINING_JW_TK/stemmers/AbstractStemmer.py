from dataModel import Document
from dataModel import TextTopic


class AbstractStemmer(object):
    """description of class"""
    def stemDocument(self, doc = Document()):
        """
        Niechaj ta funkcja przyjmie doc i zróci ten sam doc z tym, że po setemmingu
        Stemming powinien objąć title i content
        """
        raise NotImplemented
