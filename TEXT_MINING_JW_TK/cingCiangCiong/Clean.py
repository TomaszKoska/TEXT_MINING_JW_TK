def removePunctuation(document=None):
    # bierze dokument
    # zwraca taki sam dokument, tylko bez interpunkcji
    print("not implemented yet")
    return document

def removeGarbage(document = None):
    #TODO
    return document

def toUpperCase(document = None):
    #TODO
    return document

def toLowerCase(document = None):
    #TODO
    return document

def applyToAllDocuments(documents =[], fun=removePunctuation):
    for d in documents:
        d = fun(d)
    return documents