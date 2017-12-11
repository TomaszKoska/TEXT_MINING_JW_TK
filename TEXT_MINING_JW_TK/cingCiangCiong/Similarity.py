from cingCiangCiong.Base import *
import math

def basicSimilarity(wordCountList={},wordCountList2={},allWords=[],**kwargs):
    #przyjmuje kontekst1 (dictionary {słowo:count,słowo:count...}) kontekst z countem!
    #przyjmuje kontekst2 (dictionary {słowo:count,słowo:count...}) kontekst z countem!
    #allWords może służyć do okrojenia lub rozszerzenia wordSpace'u. Jeśli nie podano, to allWords jest sumą słów  z kontekstów
    
    if len(allWords) == 0:
        allWords = list(wordCountList.keys())[:]
        allWords.extend(list(wordCountList2.keys())[:])
    
    result ={}
    size1=sum(wordCountList.values())
    size2=sum(wordCountList2.values())

    #print("WORD COUNT!")
    #print(wordCountList)
    #print(size1)
    #print(wordCountList2)
    #print(size2)

    for w in allWords:
        try:
            result[w] = wordCountList[w]/size1*wordCountList2[w]/size2
        except KeyError:
            result[w] = 0
        except:
            result[w] = 0
    #print(result)
    return sum(result.values())


def getIdf(documents=[], allWords=[]):
    
    if len(allWords) == 0:
        allWords = getAllWords(documents)

    wordLists = []
    for d in documents:
        wordLists.append(getAllWords(d))
    
    totalDocs = len(documents)
    result={}
    #print("total docs: " + str(totalDocs))
    for w in allWords:
        docsContaining = 0
        for wl in wordLists:
            if w in wl:
                docsContaining= docsContaining+1
        #print("word " + w + " is in " + str(docsContaining) + " docs out of " + str(totalDocs)  + " so the probaility is " + str(docsContaining/totalDocs))
        if docsContaining>0:
            result[w] = math.log((1+totalDocs)/(docsContaining), math.e)
        else:
            result[w] = 0
    return result



def idfSimilarity(wordCountList={},wordCountList2={},idf={},**kwargs):
    result ={}
    size1=sum(wordCountList.values())
    size2=sum(wordCountList2.values())
    #print(wordCountList)
    #print(wordCountList2)
    #print(size1)
    #print(size2)
    for w in idf.keys():
        try:
            result[w] = wordCountList[w]/size1*wordCountList2[w]/size2*idf[w]
        except KeyError:
            result[w] = 0
    #print(result)
    return sum(result.values())



def bm25Similarity(wordCountList={},wordCountList2={},idf={}, k=0, b=0, avgDocLength = 1, **kwargs):
    total = sum(wordCountList.values())
    tmp ={}
    for w in idf.keys():
        try:
            tmp[w] = (wordCountList[w]*(k+1))/(wordCountList[w]+k*(1-b+b*total/avgDocLength))
        except KeyError:
            tmp[w] = 0

    total1=sum(tmp.values())

    total = sum(wordCountList2.values())
    tmp2 ={}

    for w in idf.keys():
        try:
            tmp2[w] = wordCountList2[w]*(k+1)/(wordCountList2[w]+k*(1-b+b*total/avgDocLength))
        except KeyError:
            tmp2[w] = 0
    result ={}
    total2=sum(tmp2.values())


    for w in idf.keys():
        result[w] = tmp[w]/total1*tmp2[w]/total2*idf[w]
    return sum(result.values())



def documentsSimilarity(document1=Document(),document2=Document(),allWords=[],similarityFunction=basicSimilarity,**kwargs):
    if len(allWords)==0:
        allWords = getAllWords([document1,document2])

    return similarityFunction(wordCountList=getWordsCount(documents=document1,allWords=allWords),wordCountList2=getWordsCount(documents=document2,allWords=allWords),allWords=allWords,**kwargs)

def allDocumentsSimilarity(documents =[], allWords=[],similarityFunction=basicSimilarity,**kwargs):
    result = {}
    for d in documents:
        result[d.title] = {}
        for d2 in documents:
            result[d.title][d2.title] = documentsSimilarity(d,d2,allWords=allWords,similarityFunction=similarityFunction,**kwargs)
    return result


def getWordProbability(word="",documents=[]):
    if (type(documents) is Document):
        documents=[documents]
    containing=0
    total = len(documents)
    for d in documents:
        if word in getAllWords(d):
            containing = containing +1
    #co jeśli total nie istlnieje?
    if total != 0:
        return containing/total
    else:
        return 0



def getWordConditionalProbability(word="",conditionWord="",documents=[]):
    if (type(documents) is Document):
        documents=[documents]
    containing=0
    containingCondition=0
    for d in documents:
        aw = getAllWords(d)
        if conditionWord in aw:
            containingCondition = containingCondition +1
            if word in aw:
                containing = containing +1
    #co jeśli condition nie występuje?
    if containingCondition != 0:
        return containing/containingCondition
    else:
        return 0

def get01ConditionalProbability(word="",conditionWord="",documents=[]):
    if (type(documents) is Document):
        documents=[documents]
    containing=0
    containingCondition=0
    for d in documents:
        aw = getAllWords(d)
        if conditionWord in aw:
            containingCondition = containingCondition +1
            if not(word in aw):
                containing = containing +1
    if containingCondition != 0:
        return containing/containingCondition
    else:
        return 0

def get10ConditionalProbability(word="",conditionWord="",documents=[]):
    if (type(documents) is Document):
        documents=[documents]
    containing=0
    containingCondition=0
    for d in documents:
        aw = getAllWords(d)
        if not(conditionWord in aw):
            containingCondition = containingCondition +1
            if word in aw:
                containing = containing +1
    #co jeśli condition nie występuje?
    if containingCondition != 0:
        return containing/containingCondition
    else:
        return 0

def get00ConditionalProbability(word="",conditionWord="",documents=[]):
    if (type(documents) is Document):
        documents=[documents]
    containing=0
    containingCondition=0
    for d in documents:
        aw = getAllWords(d)
        if not(conditionWord in aw):
            containingCondition = containingCondition +1
            if not(word in aw):
                containing = containing +1
    #co jeśli condition nie występuje?
    if containingCondition != 0:
        return containing/containingCondition
    else:
        return 0


def get11ConditionalProbability(word="",conditionWord="",documents=[]):
    return getWordConditionalProbability(word=word,conditionWord=conditionWord,documents=documents)


def getCoocurenceProbability(word="",word2="",documents=[]):
    if (type(documents) is Document):
        documents=[documents]
    containing=0
    total = len(documents)
    for d in documents:
        aw = getAllWords(d)
        if word in aw and word2 in aw:
            containing = containing +1
    #co jeśli total nie istlnieje?
    if containingCondition != 0:
        return containing/containingCondition
    else:
        return 0

def getWordEntrophy(word="",documents=[]):
    p=getWordProbability(word,documents)
    q=1-p
    x=0
    if p != 0:
        x =-p*math.log2(p)
    else:
        x=0
    if p != 0:
        x =x -q*math.log2(q)
    return x

def getWordConditionalEntrophy(word="",conditionWord="",documents=[]):
    p11 = getWordConditionalProbability(word=word,conditionWord=conditionWord,documents=documents)
    x=0
    if p11 != 0:
        x =-p11*math.log2(p11)
    else:
        x=0
    if (1-p11) != 0:
        x =x -(1-p11)*math.log2(1-p11)
    return x   




#d1 = Document(title="TEST!", text="THE DOG GOES TO A VET BECAUSE HE IS VERY SICK HE HOPES TO GET SOME MEDICINE", date="", source="")
#d2 = Document(title="TEST2!", text="A DOG IS A NICE PET HE RUNS AND RUNS CHASES CATS", date="", source="")

#aw = getAllWords([d1,d2])
#c1= getWordsCount(d1,aw)
#c2= getWordsCount(d2,aw)

#print(basicSimilarity(wordCountList=c1, wordCountList2=c2,allWords=aw))
#print(documentsSimilarity(document1=d1,document2=d2,allWords=[],similarityFunction=basicSimilarity))

#print(basicSimilarity(wordCountList=c1, wordCountList2=c1,allWords=aw))
#print(documentsSimilarity(document1=d1,document2=d1,allWords=[],similarityFunction=basicSimilarity))

#print(basicSimilarity(wordCountList=c2, wordCountList2=c2,allWords=aw))
#print(documentsSimilarity(document1=d2,document2=d2,allWords=[],similarityFunction=basicSimilarity))

#print("idf now")
#idf = getIdf([d1,d2],aw)
#print(idf)

#print(idfSimilarity(wordCountList=c1, wordCountList2=c2,allWords=aw,idf=idf))
#print(documentsSimilarity(document1=d1,document2=d2,allWords=aw,similarityFunction=idfSimilarity,idf=idf))
#print("idfBm25Similarity")
#print(bm25Similarity(wordCountList=c1, wordCountList2=c2,idf=idf,k=1000,b=0.9,avgDocLength=1))
#print(documentsSimilarity(document1=d1,document2=d2,allWords=aw,similarityFunction=bm25Similarity,idf=idf,k=1000,b=0.9,avgDocLength=1))

#print("All docs now")
#print(allDocumentsSimilarity(documents=[d1,d2],allWords=aw,similarityFunction=bm25Similarity,idf=idf,k=1000,b=0.9,avgDocLength=1))









#getAllSimilarities(documents=[], sim1 = basicSimilarity,k=1,b=6)
#getAllSimilarities(documents=[], sim = BM25similarity,k=1,b=6)

#k=10
#a=BM25Similarity(wordCountList={'A':1,'B':2}, wordCountList2={'A':2,'B':1,'C':3,'D':4},k=k,b=0.9,avgDocLength= 3)
#print(a)
#a=BM25Similarity(wordCountList={'A':1,'B':2}, wordCountList2={'A':1,'B':1,'C':3,'D':4},k=k,b=0.9,avgDocLength= 3)
#print(a)
#a=BM25Similarity(wordCountList={'A':1,'B':2}, wordCountList2={'A':1,'B':2,'C':3,'D':4},k=k,b=0.9,avgDocLength= 3)
#print(a)
#a=BM25Similarity(wordCountList={'A':1,'B':2}, wordCountList2={'A':1,'B':2,'C':0,'D':0},k=k,b=0.9,avgDocLength= 3)
#print(a)