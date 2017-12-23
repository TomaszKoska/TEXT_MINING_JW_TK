import csv
import sqlite3
import re
import datetime
import os
from utils.Utils import *
from collections import OrderedDict

def prepareDatabase(databasePath="D:/databases/casesDictionary.db"):
    try:
        os.remove(databasePath)
    except:
        pass
    connection = sqlite3.connect(databasePath)
    query = "CREATE TABLE 'STEMS' ('ID' INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, 'BASE' TEXT, 'WORD' TEXT, 'ENDINGS_PATTERN' TEXT, 'STEM' TEXT);"
    connection.execute(query)
    connection.commit()
    connection.close()

def prepareDatabaseForFeatures(databasePath="D:/databases/casesDictionary.db"):
    pass
def loadFeatures(databasePath="D:/databases/casesDictionary.db"):
    pass


def loadData(casesFilePath = "D:/test/sjp-odm-20171214/odm.txt", databasePath="D:/databases/casesDictionary.db", delimiter=",",quotechar="\""):
    
    connection = sqlite3.connect(databasePath)
    with open(casesFilePath, 'rt',encoding="utf8") as csvfile:
        csvReader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
        a = 0
        print(datetime.datetime.now())
        for row in csvReader:
            a=a+1
            #if(a>1000):
            #   break
            size = len(row)
            if(size>1):
                row = [removeRedundantSpaces(e) for e in row]
                row = [e.lower() for e in row]
                stem = findStem(words=row)
                #endings = wordsMinusStem(stem=stem,words=row)
                print(row)
                for i in range(1,size):
                    query = "INSERT INTO STEMS (BASE, WORD, STEM, ENDINGS_PATTERN) VALUES (?, ?, ? , ?)"
                    
                    base = row[0]
                    if base.find(" ") !=-1:
                        break
                    word = row[i]
                    ending = wordMinusStem(stem,word)
                    #connection.execute(query,(row[0],row[i],stem,",".join(endings)))
                    connection.execute(query,(base,word,stem.lower(),ending.lower()))
            else:
                #query = "INSERT INTO STEMS (BASE, WORD) VALUES (?, ?)"
                #connection.execute(query,(row[0],row[0]))
                pass
        if a % 200:
            print("%r loaded" % a)
            connection.commit()
    connection.commit()
    connection.close()
    print(datetime.datetime.now())

def longestWord(words = []):
    out = words[0]
    for w in words:
        if len(w) > len(out):
            out = w
    return out



def loadDataGroups(casesFilePath = "D:/test/sjp-odm-20171214/odm.txt", databasePath="D:/databases/casesDictionary.db", delimiter=",",quotechar="\""):
    
    connection = sqlite3.connect(databasePath)
    with open(casesFilePath, 'rt',encoding="utf8") as csvfile:
        csvReader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
        a = 0
        print(datetime.datetime.now())
        for row in csvReader:
            a=a+1
            #if(a>1000):
            #   break
            size = len(row)
            if(size>1):
                row = [removeRedundantSpaces(e) for e in row]
                row = [e.lower() for e in row]
                stem = findStem(words=row)
                ending = wordsMinusStem(stem,row)
                #print(row)
                for i in range(1,size):
                    query = "INSERT INTO STEMS (BASE, WORD, STEM, ENDINGS_PATTERN) VALUES (?, ?, ? , ?)"
                    base = row[0]
                    if base.find(" ") !=-1:
                        break
                    word = row[i]
                    connection.execute(query,(base,word,stem.lower(),"|".join(ending)))
            else:
                pass
        if a % 200:
            print("%r loaded" % a)
            connection.commit()
    connection.commit()
    connection.close()
    print(datetime.datetime.now())


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

def findStem(words = []):
    #find the longest common part
    stem = ""
    #letters = [x for x in longestWord(words)]
    letters = [x for x in words[0]]

    for l in letters:
        letterIn = True
        for w in words:
           #print("Does word %r meets %r - %r?" % (w,stem+l,(stem+l).replace("?","[a-zA-Z]*")))
           checkedW =removeRedundantSpaces(w)
           if re.search((stem+l).replace("?","[a-zA-Z]*"),checkedW) is None:
               #print("no!")
               letterIn=False
        if letterIn:
            #print("all in!")
            stem=stem+l
        else:
            if len(stem)>0:
                if stem[-1]!="?":
                    stem=stem+"?"
            else:
                return "#" + words[0]
    #print(stem)
    if len(stem)>0:
       while stem[-1]=="?":
            stem = stem[:-1]
    return stem

def wordMinusStem(stem = "", word=""):
    if stem[0]=="#":
        return word

    letters = [x for x in stem]
    out = word #wynikowy string    
    pointer=0 #gdzie w sprawdzanym słowie stoję
    stemPattern = "^"+(stem).replace("?","[a-zA-Z]*")+"[a-zA-Z]*"
     
    #najpierw znajde fragment pasujacy do patternu - to bedzie miejsce pointera

    #print(stemPattern)
    for i in range(0,len(word)):
        #print(word[i:])
        if re.search(stemPattern,word[i:]) is None:
            #print("does not fit...")
            pointer = pointer+1
        else:
            break
    #print("%r    %r" % (pointer, word))
    for l in letters:
        #print("checking letter %r" % l)
        if l != "?":
            pos = out.find(l,pointer)
            #print("na pozycji %r!" % pos)
            #print("no to zmieniam na znak zapytania")
            tmp =list(out)
            tmp[pos] ="?"
            out="".join(tmp)
            #print( "Wynik: %r" % out)
            pointer = pos
    
    while out.find("??") != -1:
        out = out.replace("??","?")

    return out


def wordsMinusStem(stem = "", words=[]):
    out =[]
    for w in words:
        out.append(wordMinusStem(stem=stem,word = w))
    return list(set(out))





def primitiveTest():
    l = ["Kapetyng", "Kapetynga", "Kapetyngach", "Kapetyngami", "Kapetyngi", "Kapetyngiem", "Kapetyngom", "Kapetyngowi", "Kapetyngowie", "Kapetyngów", "Kapetyngu"]
    s =findStem(l)
    suf = wordsMinusStem(stem=s,words=l)
    print(l)
    print(s)
    print(suf)

    l = ["incydencik", "incydencikach", "incydencikami", "incydenciki", "incydencikiem", "incydencikom", "incydencikowi", "incydencików", "incydenciku"]
    s =findStem(l)
    suf = wordsMinusStem(stem=s,words=l)
    print(l)
    print(s)
    print(suf)


    l= ["indukować", "indukowali", "indukowaliby", "indukowalibyście", "indukowalibyśmy", "indukowaliście", "indukowaliśmy", "indukował", "indukowała", "indukowałaby", "indukowałabym", "indukowałabyś", "indukowałam", "indukowałaś", "indukowałby", "indukowałbym", "indukowałbyś", "indukowałem", "indukowałeś", "indukowało", "indukowałoby", "indukowały", "indukowałyby", "indukowałybyście", "indukowałybyśmy", "indukowałyście", "indukowałyśmy", "indukowana", "indukowaną", "indukowane", "indukowanego", "indukowanej", "indukowanemu", "indukowani", "indukowania", "indukowaniach", "indukowaniami", "indukowanie", "indukowaniem", "indukowaniom", "indukowaniu", "indukowano", "indukowany", "indukowanych", "indukowanym", "indukowanymi", "indukowań", "indukuj", "indukują", "indukując", "indukująca", "indukującą", "indukujące", "indukującego", "indukującej", "indukującemu", "indukujący", "indukujących", "indukującym", "indukującymi", "indukujcie", "indukujcież", "indukuje", "indukujecie", "indukujemy", "indukujesz", "indukuję", "indukujmy", "indukujmyż", "indukujże", "nieindukowana", "nieindukowaną", "nieindukowane", "nieindukowanego", "nieindukowanej", "nieindukowanemu", "nieindukowani", "nieindukowania", "nieindukowaniach", "nieindukowaniami", "nieindukowanie", "nieindukowaniem", "nieindukowaniom", "nieindukowaniu", "nieindukowany", "nieindukowanych", "nieindukowanym", "nieindukowanymi", "nieindukowań", "nieindukująca", "nieindukującą", "nieindukujące", "nieindukującego", "nieindukującej", "nieindukującemu", "nieindukujący", "nieindukujących", "nieindukującym", "nieindukującymi"]
    s =findStem(l)
    suf = wordsMinusStem(stem=s,words=l)
    print(l)
    print(s)
    print(suf)


    l= ["pies", " psa", "psach", "psami", "psem", "psie", "psom", "psów", "psu", "psy", "nienajpies"]
    s =findStem(l)
    suf = wordsMinusStem(stem=s,words=l)
    print(l)
    print(s)
    print(suf)


    l= ["być", "bądź", "bądźcie", "bądźcież", "bądźmy", "bądźmyż", "bądźże", "będą", "będąc", "będąca", "będącą", "będące", "będącego", "będącej", "będącemu", "będący", "będących", "będącym", "będącymi", "będę", "będzie", "będziecie", "będziemy", "będziesz", "bycia", "byciach", "byciami", "bycie", "byciem", "byciom", "byciu", "byli", "byliby", "bylibyście", "bylibyśmy", "byliście", "byliśmy", "był", "była", "byłaby", "byłabym", "byłabyś", "byłam", "byłaś", "byłby", "byłbym", "byłbyś", "byłem", "byłeś", "było", "byłoby", "były", "byłyby", "byłybyście", "byłybyśmy", "byłyście", "byłyśmy", "byto", "jest", "jestem", "jesteś", "jesteście", "jesteśmy", "niebędąca", "niebędącą", "niebędące", "niebędącego", "niebędącej", "niebędącemu", "niebędący", "niebędących", "niebędącym", "niebędącymi", "niebycia", "niebyciach", "niebyciami", "niebycie", "niebyciem", "niebyciom", "niebyciu", "niebyć", "są"]
    s =findStem(l)
    suf = wordsMinusStem(stem=s,words=l)
    print(l)
    print(s)
    print(suf)


    l= ["Aachen","Aachenem","Aachenie","Aachenowi","Aachenu"]
    s =findStem(l)
    suf = wordsMinusStem(stem=s,words=l)
    print(l)
    print(s)
    print(suf)


    l= ["Aachen"," Aachenem"," Aachenie"," Aachenowi"," Aachenu"]
    s =findStem(l)
    suf = wordsMinusStem(stem=s,words=l)
    print(l)
    print(s)
    print(suf)


#tu puszczone komendy
#print(letterCombo())
#print(countPatternOccurances("aa","abcabaaaaaaaabdadgstahsyrthbabcasgdhfjrstabcdsggrjttrhebrfabc"))


#prepareDatabase("D:/databases/casesDictionary.db")
#loadDataGroups(databasePath ="D:/databases/casesDictionary.db")
def findRedundantCombos(databasePath="",letterSet=letterCombo()):
    combos = [x for x in letterSet]
    
    connection = sqlite3.connect(databasePath)
    out={}
    i = 0
    total = len(letterSet)
    for c in combos:
        i=i+1
        print(i/total)
        cursor = connection.execute("select '"+c+"', count(1) from stems where word like '%"+c+"%'")
        for row in cursor:
            out[c] = int(row[1])
            #print(c)
            #print(out[c])
    connection.close()
    return out


import json
def saveComboCounts():
    combos =findRedundantCombos(databasePath="D:/databases/casesDictionary_A.db",letterSet=letterCombo())
    with open('D:/databases/data.json', 'w') as outfile:
        json.dump(combos, outfile, indent=4 )


    for x,y in combos.items():
        if(y==0):
            print("%r     %r" % (x,y))

def getFinalFeatures(path = 'D:/databases/data.json', without3 = True, minWords = 1):
    with open(path, 'r') as fp:
        data = json.load(fp)
    if without3:
        zeros = [x for x,y in data.items() if y<minWords or len(x)>2]
    else:
        zeros = [x for x,y in data.items() if y<minWords]
    #print(len(zeros))
    #print(len(data.keys()))


    finalFeatures = list(set(data.keys()) - set(zeros))
    finalFeatures.sort()
    if without3:
        finalFeatures = [f for f in finalFeatures if len(f)<3]
    return finalFeatures

def getFeaturesFromWord(word = "", wordSpace = []):
    word = word.lower()
    out = {}
    letters = list(set([x for x in word]))
    for l in letters:
        out[l] = countPatternOccurances(l,word)

    di = []
    for i in range(1,len(word)):
        di.append(word[i-1]+word[i])

    di= list(set(di))
    for d in di:
        out[d] = countPatternOccurances(d,word)

    tri = []
    for i in range(2,len(word)):
        di.append(word[i-2]+word[i-1]+word[i])

    #tri= list(set(tri))
    #for t in tri:
    #    out[t] = countPatternOccurances(t,word)
        
    outputVec = []
    for w in wordSpace:
        try:
            outputVec.append(out[w])
        except KeyError:
            outputVec.append(0)
    return outputVec


def getFeaturesAndSaveInCsv(features = getFinalFeatures(), outputPath = "D:/databases/features.csv", databasePath="D:/databases/casesDictionary_A.db", delimiter=",",quotechar="\""):
    connection = sqlite3.connect(databasePath)
    query = "SELECT word, endings_pattern from stems"
    cursor  = connection.execute(query)
    a= 0
    headers = ["WORD", "ENDING"]
    headers.extend(features)
    with open(outputPath, "w") as myCsv:
        csvWriter = csv.DictWriter(myCsv,fieldnames=headers, delimiter=delimiter,lineterminator = '\n')
        csvWriter.writeheader()
        for row in cursor:
            a+=1
            print(a/4028572)
            #if a > 1000 :
            #    break
            #print(row[0] , "       " + row[1])
            #print()
            rowDict = {}
            featureValues = getFeaturesFromWord(row[0],wordSpace=features)
            rowDict["WORD" ]= row[0]
            rowDict["ENDING" ]=row[1]
            for i in range(0,len(features)):
                rowDict[features[i]] = featureValues[i]
            csvWriter.writerow(rowDict)
    connection.close()

#features = getFinalFeatures(minWords = 1000,without3=True)
#features.sort()
#print("sorted")
#print(features)
#print(getFeaturesFromWord("Konstantynopolitańczykowianeczkównaniedotykagówna",wordSpace=features))
#pies = getFeaturesFromWord("piesek",wordSpace=features)
#print(pies)

#getFeaturesAndSaveInCsv(features = features)

def openFeatures(path ="D:/databases/features_extracted.csv", delimiter=",",quotechar="\""):
    with open(path, 'rt') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
        a = 0
        print(datetime.datetime.now())
        for row in csvReader:
            a=a+1
            if a>10000:
                break
            print(row)
            
        print(datetime.datetime.now())

#openFeatures()