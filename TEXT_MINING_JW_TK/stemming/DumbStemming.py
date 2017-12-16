from dataModel.Document import Document
from cingCiangCiong.Base import *
from cingCiangCiong.Clean import *
from databaseHelpers.AbstractDatabaseHelper import AbstractDatabaseHelper

def getStemFromDb(word="", dbHelper = AbstractDatabaseHelper(), tableName = ""):
    stem=word
    #sprawdza czy słowo samo w sobie nie jest stemem
    
    
    return stem
def removePolishCharacters(word = ""):
    return word.upper().replace("Ę","E").replace("Ó","O").replace("Ą","A").replace("Ł","L").replace("Ż","Z").replace("Ź","Z").replace("Ć","C").replace("Ń","N")

def dumbStemmer(word = "", minLength = 3):
    word = removePolishCharacters(word)
    stem = word

    #nie obcinamy krótkich słów
    if len(stem)<=minLength:
        return stem
    #nie dotykamy słów będących hasztagami
    if stem[0] == "#":
        return stem

    #wywalamy polskie znaki

    #dumb przymiotnik - zmieniamy końcówki na suffix
    #a najpierw próbujemy uwspólnić formę
    if len(stem) > 3 and stem[0:2] == "naj":
        stem = stem[3:]

    if len(stem) > 4 and stem[-4:] == "zszy":
        stem = stem[:-4]

    if len(stem) > 4 and stem[-4:] == "nszy":
        stem = stem[:-4]
        
    if len(stem) > 4 and stem[-4:] == "lszy":
        stem = stem[:-4]

    if len(stem) > 3 + minLength and  stem[-3:] == "szy":
        stem = stem[:-3] + "y"

    if len(stem) > 3 + minLength and  stem[-3:] == "sza":
        stem = stem[:-3] + "a"
    
    if len(stem) > 3 + minLength and  stem[-3:] == "sze":
        stem = stem[:-3] + "e"
    
    suffix = ""
    # przymiotnik z 4 literami
    if len(stem) > 4 + minLength and  stem[-4:] == "iego":
        return stem[:-4] + suffix
    if len(stem) > 4 + minLength and  stem[-4:] == "iemu":
        return stem[:-4] + suffix
    
    #przymiotnik z trzema literami
    if len(stem) > 3 + minLength and  stem[-3:] == "ich":
        return stem[:-3] + suffix
    if len(stem) > 3 + minLength and  stem[-3:] == "ych":
        return stem[:-3] + suffix
    if len(stem) > 3 + minLength and  stem[-3:] == "ego":
        return stem[:-3] + suffix
    if len(stem) > 3 + minLength and  stem[-3:] == "emu":
        return stem[:-3] + suffix
    if len(stem) > 3 + minLength and  stem[-3:] == "iej":
        return stem[:-3] + suffix
    
    #przymiotnik z dwiema literami
    if len(stem) > 2 + minLength and  stem[-2:] == "ym":
        return stem[:-2] + suffix
    if len(stem) > 2 + minLength and  stem[-2:] == "im":
        return stem[:-2] + suffix
    if len(stem) > 2 + minLength and  stem[-2:] == "ei":
        return stem[:-2] + suffix
    if len(stem) > 2 + minLength and  stem[-2:] == "ie":
        return stem[:-2] + suffix
    if len(stem) > 2 + minLength and  stem[-2:] == "ej":
        return stem[:-2] + suffix

    #przymiotnik z jedną literą
    if len(stem) > 1 + minLength and  stem[-1:] == "y":
        return stem[:-1] + suffix
    if len(stem) > 1 + minLength and  stem[-1:] == "a":
        return stem[:-1] + suffix
    if len(stem) > 1 + minLength and  stem[-1:] == "i":
        return stem[:-1] + suffix

    

    #dumb czasownik


    #dumb rzeczownik


    return stem

def runStemming(documents = [], dbHelper = AbstractDatabaseHelper(), tableName = ""):
    pass

