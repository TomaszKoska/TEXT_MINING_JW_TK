from collections import namedtuple
from cingCiangCiong.Clean import *
from dataModel.Document import Document
from collections import Counter
import tempfile


def getAllWords(documents = []):
    #niechaj funkcja ta bazuje na liście dokumentów wczytanych wcześniej
    #niechaj funkcja ta zwraca listę stringów - słów, które wystąpiły we wszystkich dokumentach
    #
    if (type(documents) is Document):
        documents=[documents]

    outcome = []
    for d in documents:
        #rozbij dokument na pojedyncze słowa (czyli ze względu na spacje)
        #weź słowo
        #zapisz je w wynikach
        outcome.extend(d.text.split(" "))
        outcome = list(set(outcome))
    return outcome




def getAllWordsIter(dbHelper=None, tableName="NoNameGiven"):
    #niechaj funkcja ta bazuje na iteratorze - tzn niech przyjmuje dbHelpera
    outcome = []
    dbHelper.startIterator(tableName)
    try:
        while(True):
            d = dbHelper.getNextDocument()
            outcome.extend(d.text.split(" "))
            outcome = list(set(outcome))
    except StopIteration:
        dbHelper.stopIterator()

    return outcome




def getWordsCount(documents = [], allWords = []):
    #niechaj funkcja ta bazuje na liście dokumentów wczytanych wcześniej
    #jeśli drugi argument jest pustą listą (nie podano go) to niech ta funkcja wykorzysta getallWords
    #niechaj funkcja ta zwraca słownik (dictionary) {"słowo": 1, "słowo2": 400, "słowo3": 435 ...}
    #przy czym liczby te to LICZBA WYSTĄPIEŃ
    #
    
    if (type(documents) is Document):
        documents=[documents]
    
    words = []
    for d in documents:
        #rozbij dokument na pojedyncze słowa (czyli ze względu na spacje) i dodaj listę do obecnej listy
        words.extend(d.text.split(" "))
    counterOutput = dict(Counter(words))

    output = {}

    if len(allWords) == 0:
        allWords = getAllWords(documents)

    for w in allWords:
        try:
            output[w] = counterOutput[w]
        except KeyError:
            output[w] = 0

    return output



def getWordsCountIter(dbHelper=None, tableName="NoNameGiven", allWords = []):
    words = []
    dbHelper.startIterator(tableName)
    try:
        while(True):
            d = dbHelper.getNextDocument()
            words.extend(d.text.split(" "))
    except StopIteration:
        dbHelper.stopIterator()

        counterOutput = dict(Counter(words))

    output = {}

    if len(allWords) == 0:
        allWords = getAllWordsIter(dbHelper,tableName)

    for w in allWords:
        try:
            output[w] = counterOutput[w]
        except KeyError:
            output[w] = 0

    return output

def getWordsFrequency(documents = [], allWords = []):
    #niechaj funkcja ta bazuje na liście dokumentów wczytanych wcześniej
    #jeśli drugi argument jest pustą listą (nie podano go) to niech ta funkcja wykorzysta getallWords
    #niechaj funkcja ta zwraca słownik (dictionary) {"słowo": 1, "słowo2": 400, "słowo3": 435 ...}
    if (type(documents) is Document):
        documents=[documents]

    if len(allWords) == 0:
        allWords = getAllWords(documents)

    counts = getWordsCount(documents,allWords)
    total = sum(counts.values())#wszystkich słów istotnych z punktu widzenia allWords


    for k,v in counts.items():
        counts[k]=v/total

    return counts


def getWordsFrequencyIter(dbHelper=None, tableName="NoNameGiven",  allWords = []):
    #niechaj funkcja ta bazuje na iteratorze - tzn niech przyjmuje dbHelpera
    #jeśli drugi argument jest pustą listą (nie podano go) to niech ta funkcja wykorzysta getallWordsIter
    #niechaj funkcja ta zwraca słownik (dictionary) {"słowo": 1, "słowo2": 400, "słowo3": 435 ...}
    #przy czym liczby te to LICZBA DOKUMENTÓW w których występuje słowo

    if len(allWords) == 0:
        allWords = getAllWordsIter(dbHelper,tableName)

    counts = getWordsCountIter(dbHelper,tableName,allWords)
    total = sum(counts.values())#wszystkich słów istotnych z punktu widzenia allWords


    for k,v in counts.items():
        counts[k]=v/total

    return counts



def getLeftContext(documents = [], word = "", distance = 1, allWords = []):
    #niechaj funkcja ta bazuje na liście dokumentów wczytanych wcześniej
    #niechaj funkcja ta zwraca słownik (dictionary) {"słowo": 1, "słowo2": 400, "słowo3": 435 ...}
    #example:
    #wywołanie getLeftContext(jakieśDokumenty,"pies",2)
    #wynik: {"Ten":10, "Tamten": 23, "Dziwny": 10 ...}
    #powyższy wynik oznaza:
    #słowo "Ten" wystąpiło 10 razy po lewej stronie słowa "pies" w odległości NIE WIĘKSZEJ niż 2
    #słowo "Tamten" wystąpiło 23 razy po lewej stronie słowa "pies" w odległości NIE WIĘKSZEJ niż 2
    #itd.
    if (type(documents) is Document):
        documents=[documents]

    if len(allWords) == 0:
        allWords = getAllWords(documents)
    
    context =[]
    for d in documents:
        words = d.text.split(" ")
        for i in range(0,len(words)-distance):
            for j in range(i+1,distance+i+1):
                if word == words[j]:
                    context.append(words[i])
                    
    context= dict(Counter(context))
    total = sum(context.values())
    output={}
    for w in allWords:
        try:
            output[w] = context[w]/total
        except KeyError:
            output[w] = 0

    return output




def getLeftContextIter(dbHelper=None, tableName="NoNameGiven", word = "", distance = 1, allWords = []):
    #niechaj funkcja ta bazuje na iteratorze - tzn niech przyjmuje dbHelpera
    #niechaj funkcja ta zwraca słownik (dictionary) {"słowo": 1, "słowo2": 400, "słowo3": 435 ...}
    #example:
    #wywołanie getLeftContext(jakieśDokumenty,"pies",2)
    #wynik: {"Ten":10, "Tamten": 23, "Dziwny": 10 ...}
    #powyższy wynik oznaza:
    #słowo "Ten" wystąpiło 10 razy po lewej stronie słowa "pies" w odległości NIE WIĘKSZEJ niż 2
    #słowo "Tamten" wystąpiło 23 razy po lewej stronie słowa "pies" w odległości NIE WIĘKSZEJ niż 2
    #itd.

    if len(allWords) == 0:
        allWords = getAllWordsIter(dbHelper,tableName)

    context =[]
    dbHelper.startIterator(tableName)
    try:
        while(True):
            d = dbHelper.getNextDocument()
            words = d.text.split(" ")
            for i in range(0,len(words)-distance):
                for j in range(i+1,distance+i+1):
                    if word == words[j]:
                        context.append(words[i])
    except StopIteration:
        dbHelper.stopIterator()
   
                    
    context= dict(Counter(context))
    total = sum(context.values())
    output={}
    for w in allWords:
        try:
            output[w] = context[w]/total
        except KeyError:
            output[w] = 0

    return output


def getRightContext(documents = [], word = "", distance = 1, allWords = []):
    #niechaj funkcja ta bazuje na liście dokumentów wczytanych wcześniej
    #niechaj funkcja ta zwraca słownik (dictionary) {"słowo": 1, "słowo2": 400, "słowo3": 435 ...}
    #example:
    #wywołanie getRightContext(jakieśDokumenty,"pies",2)
    #wynik: {"Ten":10, "Tamten": 23, "Dziwny": 10 ...}
    #powyższy wynik oznaza:
    #słowo "Ten" wystąpiło 10 razy po prawej stronie słowa "pies" w odległości NIE WIĘKSZEJ niż 2
    #słowo "Tamten" wystąpiło 23 razy po prawej stronie słowa "pies" w odległości NIE WIĘKSZEJ niż 2
    #itd.
    if (type(documents) is Document):
        documents=[documents]

    if len(allWords) == 0:
        allWords = getAllWords(documents)
    
    context =[]
    for d in documents:
        words = d.text.split(" ")
        for i in range(distance,len(words)):
            for j in range(i-distance,i):
                if word == words[j]:
                    context.append(words[i])
                    
    context= dict(Counter(context))
    total = sum(context.values())
    output={}
    for w in allWords:
        try:
            output[w] = context[w]/total
        except KeyError:
            output[w] = 0

    return output

def getRightContextIter(dbHelper=None, tableName="NoNameGiven", word = "", distance = 1, allWords = []):
    #niechaj funkcja ta bazuje na iteratorze - tzn niech przyjmuje dbHelpera
    #niechaj funkcja ta zwraca słownik (dictionary) {"słowo": 1, "słowo2": 400, "słowo3": 435 ...}
    #example:
    #wywołanie getRightContext(jakieśDokumenty,"pies",2)
    #wynik: {"Ten":10, "Tamten": 23, "Dziwny": 10 ...}
    #powyższy wynik oznaza:
    #słowo "Ten" wystąpiło 10 razy po prawej stronie słowa "pies" w odległości NIE WIĘKSZEJ niż 2
    #słowo "Tamten" wystąpiło 23 razy po prawej stronie słowa "pies" w odległości NIE WIĘKSZEJ niż 2
    #itd.
    if len(allWords) == 0:
        allWords = getAllWordsIter(dbHelper,tableName)

    context =[]
    dbHelper.startIterator(tableName)
    try:
        while(True):
            d = dbHelper.getNextDocument()
            words = d.text.split(" ")
            for i in range(distance,len(words)):
                for j in range(i-distance,i):
                    if word == words[j]:
                        context.append(words[i])
    except StopIteration:
        dbHelper.stopIterator()
   
                    
    context= dict(Counter(context))
    total = sum(context.values())
    output={}
    for w in allWords:
        try:
            output[w] = context[w]/total
        except KeyError:
            output[w] = 0

    return output

def getWindowContext(documents = [], word = "", distance = 1, allWords = []):
    #niechaj funkcja ta bazuje na liście dokumentów wczytanych wcześniej
    #niechaj funkcja ta zwraca słownik (dictionary) {"słowo": 1, "słowo2": 400, "słowo3": 435 ...}
    #example:
    #wywołanie getWindowContext(jakieśDokumenty,"pies",2)
    #wynik: {"Ten":10, "Tamten": 23, "Dziwny": 10 ...}
    #powyższy wynik oznaza:
    #słowo "Ten" wystąpiło 10 razy po prawej lub lewej stronie słowa "pies" w odległości NIE WIĘKSZEJ niż 2
    #słowo "Tamten" wystąpiło 23 razy po prawej lub lewej stronie słowa "pies" w odległości NIE WIĘKSZEJ niż 2
    #itd.
    if (type(documents) is Document):
        documents=[documents]

    if len(allWords) == 0:
        allWords = getAllWords(documents)
    
    context =[]
    for d in documents:
        words = d.text.split(" ")
        for i in range(distance,len(words)-distance):
            if word == words[i]:
                for j in range(i-distance,i+distance+1):
                    if  i != j:
                        context.append(words[j])
    context= dict(Counter(context))

    output={}
    for w in allWords:
        try:
            output[w] = context[w]/1
        except KeyError:
            output[w] = 0
    total = sum(output.values())

    for w in allWords:
        try:
            output[w]=output[w]/total
        except ZeroDivisionError:
            output[w]=0
    return output


def getWindowContextIter(dbHelper=None, word = "", distance = 1, allWords = []):
    #niechaj funkcja ta bazuje na iteratorze - tzn niech przyjmuje dbHelpera
    #niechaj funkcja ta zwraca słownik (dictionary) {"słowo": 1, "słowo2": 400, "słowo3": 435 ...}
    #example:
    #wywołanie getWindowContext(jakieśDokumenty,"pies",2)
    #wynik: {"Ten":10, "Tamten": 23, "Dziwny": 10 ...}
    #powyższy wynik oznaza:
    #słowo "Ten" wystąpiło 10 razy po prawej lub lewej stronie słowa "pies" w odległości NIE WIĘKSZEJ niż 2
    #słowo "Tamten" wystąpiło 23 razy po prawej lub lewej stronie słowa "pies" w odległości NIE WIĘKSZEJ niż 2
    #itd.
    if len(allWords) == 0:
        allWords = getAllWordsIter(dbHelper,tableName)

    context =[]
    dbHelper.startIterator(tableName)
    try:
        while(True):
            d = dbHelper.getNextDocument()
            words = d.text.split(" ")
            for i in range(distance,len(words)-distance):
                for j in range(i-distance,distance+i+1):
                    if word == words[j] and i!=j:
                        context.append(words[i])
    except StopIteration:
        dbHelper.stopIterator()
   
                    
    context= dict(Counter(context))
    total = sum(context.values())
    output={}
    for w in allWords:
        try:
            output[w] = context[w]/total
        except KeyError:
            output[w] = 0

    return output 

def BM25(context):
    pass


def similarity(context1, context2):
    pass

def similarityIDF(context1, context2):
    pass
