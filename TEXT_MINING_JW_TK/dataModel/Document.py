class Document(object):
    """description of class"""
    def __init__(self, title="", text="", date="", source="", label=""):
        self.title = title
        self.text = text
        self.date = date
        self.source = source
        self.label = label #tego chcemy, tak myślę


    def __eq__(self, other) : 
        return self.__dict__ == other.__dict__

    def __lt__(self, other):
        return (self.text < other.text)

    def toUpper(self):
        self.title = title.upper()
        self.text = text.upper()

    def toLower(self):
        self.title = title.lower()
        self.text = text.lower()