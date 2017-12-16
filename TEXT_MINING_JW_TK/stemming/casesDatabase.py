import csv
import sqlite3

def prepareDatabase(databasePath="D:/databases/casesDictionary.db"):
    connection = sqlite3.connect(databasePath)
    query = "CREATE TABLE 'STEMS' ('ID' INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, 'STEM' TEXT, 'WORD' TEXT);"
    connection.execute(query)
    connection.commit()
    connection.close()

def loadData(casesFilePath = "D:/test/sjp-odm-20171214/odm.txt", databasePath="D:/databases/casesDictionary.db", delimiter=",",quotechar="\""):
    
    connection = sqlite3.connect(databasePath)
    with open(casesFilePath, 'rt',encoding="utf8") as csvfile:
        csvReader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
        a = 0
        
        for row in csvReader:
            a=a+1
            #if(a>100):
            #   break
            size = len(row)
            if(size>1):
                for i in range(1,size):
                    query = "INSERT INTO STEMS (STEM, WORD) VALUES (?, ?)"
                    connection.execute(query,(row[0],row[i]))
            else:
                query = "INSERT INTO STEMS (STEM, WORD) VALUES (?, ?)"
                connection.execute(query,(row[0],row[0]))
        if a % 200:
            connection.commit()
    connection.close()

def longestWord(words = []):
    out = words[0]
    for w in words:
        if len(w) > len(out):
            out = w
    return out

def findSimpleStem(words = []):
    #find the longest common part
    stem = ""
    letters = [x for x in longestWord(words)]
    for l in letters:
        letterIn = True
        for w in words:
           if (stem+l) not in w:
               letterIn=False
        if letterIn:
            stem=stem+l
        else:
            return stem
    return stem

def getSimpleSuffixes(stem = "", words = []):
    out =[]
    for w in words:
        out.append(w.replace(stem,"",True))
    return list(set(out))



#tu puszczone komendy
#prepareDatabase()
#loadData()
l = ["Kapetyng", "Kapetynga", "Kapetyngach", "Kapetyngami", "Kapetyngi", "Kapetyngiem", "Kapetyngom", "Kapetyngowi", "Kapetyngowie", "Kapetyngów", "Kapetyngu"]
s =findStem(l)
suf = getSuffixes(stem=s,words=l)
print(l)
print(s)
print(suf)

l = ["incydencik", "incydencikach", "incydencikami", "incydenciki", "incydencikiem", "incydencikom", "incydencikowi", "incydencików", "incydenciku"]
s =findStem(l)
suf = getSuffixes(stem=s,words=l)
print(l)
print(s)
print(suf)


l= ["indukować", "indukowali", "indukowaliby", "indukowalibyście", "indukowalibyśmy", "indukowaliście", "indukowaliśmy", "indukował", "indukowała", "indukowałaby", "indukowałabym", "indukowałabyś", "indukowałam", "indukowałaś", "indukowałby", "indukowałbym", "indukowałbyś", "indukowałem", "indukowałeś", "indukowało", "indukowałoby", "indukowały", "indukowałyby", "indukowałybyście", "indukowałybyśmy", "indukowałyście", "indukowałyśmy", "indukowana", "indukowaną", "indukowane", "indukowanego", "indukowanej", "indukowanemu", "indukowani", "indukowania", "indukowaniach", "indukowaniami", "indukowanie", "indukowaniem", "indukowaniom", "indukowaniu", "indukowano", "indukowany", "indukowanych", "indukowanym", "indukowanymi", "indukowań", "indukuj", "indukują", "indukując", "indukująca", "indukującą", "indukujące", "indukującego", "indukującej", "indukującemu", "indukujący", "indukujących", "indukującym", "indukującymi", "indukujcie", "indukujcież", "indukuje", "indukujecie", "indukujemy", "indukujesz", "indukuję", "indukujmy", "indukujmyż", "indukujże", "nieindukowana", "nieindukowaną", "nieindukowane", "nieindukowanego", "nieindukowanej", "nieindukowanemu", "nieindukowani", "nieindukowania", "nieindukowaniach", "nieindukowaniami", "nieindukowanie", "nieindukowaniem", "nieindukowaniom", "nieindukowaniu", "nieindukowany", "nieindukowanych", "nieindukowanym", "nieindukowanymi", "nieindukowań", "nieindukująca", "nieindukującą", "nieindukujące", "nieindukującego", "nieindukującej", "nieindukującemu", "nieindukujący", "nieindukujących", "nieindukującym", "nieindukującymi"]
s =findStem(l)
suf = getSuffixes(stem=s,words=l)
print(l)
print(s)
print(suf)