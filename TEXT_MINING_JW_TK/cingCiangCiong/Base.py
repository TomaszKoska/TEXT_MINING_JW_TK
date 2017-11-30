from collections import namedtuple
from cingCiangCiong.Clean import *
from dataModel.Document import Document
from collections import Counter
import tempfile


def getAllWords(documents = []):
    #niechaj funkcja ta bazuje na liście dokumentów wczytanych wcześniej
    #niechaj funkcja ta zwraca listę stringów - słów, które wystąpiły we wszystkich dokumentach
    #
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

    pass

def getWordsFrequency(documents = [], allWords = []):
    #niechaj funkcja ta bazuje na liście dokumentów wczytanych wcześniej
    #jeśli drugi argument jest pustą listą (nie podano go) to niech ta funkcja wykorzysta getallWords
    #niechaj funkcja ta zwraca słownik (dictionary) {"słowo": 1, "słowo2": 400, "słowo3": 435 ...}
    #przy czym liczby te to LICZBA DOKUMENTÓW w których występuje słowo
    #
    pass


def getWordsFrequencyIter(dbHelper=None, allWords = []):
    #niechaj funkcja ta bazuje na iteratorze - tzn niech przyjmuje dbHelpera
    #jeśli drugi argument jest pustą listą (nie podano go) to niech ta funkcja wykorzysta getallWordsIter
    #niechaj funkcja ta zwraca słownik (dictionary) {"słowo": 1, "słowo2": 400, "słowo3": 435 ...}
    #przy czym liczby te to LICZBA DOKUMENTÓW w których występuje słowo
    #
    pass

def getWordsCofrequency(documents = [], allWords = []):
    #niechaj funkcja ta bazuje na liście dokumentów wczytanych wcześniej
    #jeśli drugi argument jest pustą listą (nie podano go) to niech ta funkcja wykorzysta getallWords
    #niechaj funkcja ta zwraca coś w stylu lity
    #(word1="kot",word2="Azor",cofrequency=0)
    #(word1="kot",word2="Mruczek",cofrequency=10)
    #(word1="kot",word2="pies",cofrequency=2)
    #etc...
    # to powyżej to pseudo kod, info spod linku niżej może pomóc
    #https://stackoverflow.com/questions/15418386/what-is-the-best-data-structure-for-storing-a-set-of-four-or-more-values
    #przy czym liczby te to LICZBA DOKUMENTÓW w których słowa występują wspólnie
    #
    pass


def getWordsCofrequencyIter(dbHelper=None, allWords = []):
    #niechaj funkcja ta bazuje na iteratorze - tzn niech przyjmuje dbHelpera
#jeśli drugi argument jest pustą listą (nie podano go) to niech ta funkcja wykorzysta getallWords
    #niechaj funkcja ta zwraca coś w stylu lity
    #(word1="kot",word2="Azor",cofrequency=0)
    #(word1="kot",word2="Mruczek",cofrequency=10)
    #(word1="kot",word2="pies",cofrequency=2)
    #etc...
    # to powyżej to pseudo kod, info spod linku niżej może pomóc
    #https://stackoverflow.com/questions/15418386/what-is-the-best-data-structure-for-storing-a-set-of-four-or-more-values
    #przy czym liczby te to LICZBA DOKUMENTÓW w których słowa występują wspólnie
    #
    #zadanie z gwiazdką: jeśli trzeci argument jest True, to niech zwracana lista będzie posortowana po liczbie wspólnych wystąpień
    pass


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
    
    pass

def getLeftContextIter(dbHelper=None, word = "", distance = 1, allWords = []):
    #niechaj funkcja ta bazuje na iteratorze - tzn niech przyjmuje dbHelpera
    #niechaj funkcja ta zwraca słownik (dictionary) {"słowo": 1, "słowo2": 400, "słowo3": 435 ...}
    #example:
    #wywołanie getLeftContext(jakieśDokumenty,"pies",2)
    #wynik: {"Ten":10, "Tamten": 23, "Dziwny": 10 ...}
    #powyższy wynik oznaza:
    #słowo "Ten" wystąpiło 10 razy po lewej stronie słowa "pies" w odległości NIE WIĘKSZEJ niż 2
    #słowo "Tamten" wystąpiło 23 razy po lewej stronie słowa "pies" w odległości NIE WIĘKSZEJ niż 2
    #itd.
    pass


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
    
    pass

def getRightContextIter(dbHelper=None, word = "", distance = 1, allWords = []):
    #niechaj funkcja ta bazuje na iteratorze - tzn niech przyjmuje dbHelpera
    #niechaj funkcja ta zwraca słownik (dictionary) {"słowo": 1, "słowo2": 400, "słowo3": 435 ...}
    #example:
    #wywołanie getRightContext(jakieśDokumenty,"pies",2)
    #wynik: {"Ten":10, "Tamten": 23, "Dziwny": 10 ...}
    #powyższy wynik oznaza:
    #słowo "Ten" wystąpiło 10 razy po prawej stronie słowa "pies" w odległości NIE WIĘKSZEJ niż 2
    #słowo "Tamten" wystąpiło 23 razy po prawej stronie słowa "pies" w odległości NIE WIĘKSZEJ niż 2
    #itd.
    pass

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
    
    pass

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
    pass

def BM25(context):
    pass


def similarity(context1, context2):
    pass

def similarityIDF(context1, context2):
    pass
