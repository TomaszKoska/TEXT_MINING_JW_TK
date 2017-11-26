from collections import namedtuple

def getallWords(documents = []):
    #niechaj funkcja ta bazuje na liście dokumentów wczytanych wcześniej
    #niechaj funkcja ta zwraca listę stringów - słów, które wystąpiły we wszystkich dokumentach
    #
    #bez duplikatów!
    pass

def getallWordsIter(dbHelper=None):
    #niechaj funkcja ta bazuje na iteratorze - tzn niech przyjmuje dbHelpera
    pass

def getVocabCount(documents = [], allWords = [], sort=False):
    #niechaj funkcja ta bazuje na liście dokumentów wczytanych wcześniej
    #jeśli drugi argument jest pustą listą (nie podano go) to niech ta funkcja wykorzysta getallWords
    #niechaj funkcja ta zwraca słownik (dictionary) {"słowo": 1, "słowo2": 400, "słowo3": 435 ...}
    #przy czym liczby te to LICZBA WYSTĄPIEŃ
    #
    #zadanie z gwiazdką: jeśli trzeci argument jest True, to niech zwracana lista będzie posortowana od najczęstszych słów do najrzadszych
    pass


def getVocabCountIter(dbHelper=None, allWords = []):
    #niechaj funkcja ta bazuje na iteratorze - tzn niech przyjmuje dbHelpera
    #jeśli drugi argument jest pustą listą (nie podano go) to niech ta funkcja wykorzysta getallWordsIter
    #niechaj funkcja ta zwraca słownik (dictionary) {"słowo": 1, "słowo2": 400, "słowo3": 435 ...}
    #przy czym liczby te to LICZBA WYSTĄPIEŃ
    #
    #zadanie z gwiazdką: jeśli trzeci argument jest True, to niech zwracana lista będzie posortowana od najczęstszych słów do najrzadszych
    pass

def getVocabFrequency(documents = [], allWords = [], sort=False):
    #niechaj funkcja ta bazuje na liście dokumentów wczytanych wcześniej
    #jeśli drugi argument jest pustą listą (nie podano go) to niech ta funkcja wykorzysta getallWords
    #niechaj funkcja ta zwraca słownik (dictionary) {"słowo": 1, "słowo2": 400, "słowo3": 435 ...}
    #przy czym liczby te to LICZBA DOKUMENTÓW w których występuje słowo
    #
    #zadanie z gwiazdką: jeśli trzeci argument jest True, to niech zwracana lista będzie posortowana od najczęstszych słów do najrzadszych
    pass


def getVocabFrequencyIter(dbHelper=None, allWords = []):
    #niechaj funkcja ta bazuje na iteratorze - tzn niech przyjmuje dbHelpera
    #jeśli drugi argument jest pustą listą (nie podano go) to niech ta funkcja wykorzysta getallWordsIter
    #niechaj funkcja ta zwraca słownik (dictionary) {"słowo": 1, "słowo2": 400, "słowo3": 435 ...}
    #przy czym liczby te to LICZBA DOKUMENTÓW w których występuje słowo
    #
    #zadanie z gwiazdką: jeśli trzeci argument jest True, to niech zwracana lista będzie posortowana od najczęstszych słów do najrzadszych
    pass

def getVocabCofrequency(documents = [], allWords = [], sort=False):
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
    #zadanie z gwiazdką: jeśli trzeci argument jest True, to niech zwracana lista będzie posortowana po liczbie wspólnych wystąpień
    pass


def getVocabCofrequencyIter(dbHelper=None, allWords = []):
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