class Document(object):
    """description of class"""
    def __init__(self, title="", text="", date="", source=""):
        self.title = title
        self.text = text
        self.date = date
        self.source = source

    def __eq__(self, other) : 
        return self.__dict__ == other.__dict__

    def __lt__(self, other):
        return (self.text < other.text) 