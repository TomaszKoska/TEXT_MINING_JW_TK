from stemmers import AbstractStemmer
from dataModel import Document
from dataModel import TextTopic


class DictionaryBasedStemmer(AbstractStemmer):
    """description of class"""
    def stemDocument(self, doc = Document()):
#todo: dopisać testy i dopisać pozbywanie się interpunkcji

        """
            Każde słowo po kolei w contencie i w title
            Weź
            I
            Zamień za pomocą bazy na formę bazową
            Jak nie ma w bazie
            To zostaw jak jest
        """
        out = Document(date = doc.date, source = doc.source, label = doc.label )
        tmp = [] #to będzie lista już użytych stemów

        titleArray = " ".split(doc.title)
        textArray = " ".split(doc.text)

        for w in titleArray:
            if w not in tmp:
                dbOutput = checkInDatabase(w) #db output zwróci stem z bazy albo argument
                tmp.append(dbOutput)
                textArray = [dbOutput if x == w else x  for x in textArray]
                titleArray = [dbOutput if x == w else x  for x in titleArray]

        for w in textArray:
            if w not in tmp:
                dbOutput = checkInDatabase(w) #db output zwróci stem z bazy albo argument
                tmp.append(dbOutput)
                textArray = [dbOutput if x == w else x  for x in textArray]
        out.title = " ".join(titleArray)
        out.text = " ".join(textArray)


        return out
