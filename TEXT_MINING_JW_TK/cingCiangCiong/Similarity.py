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

    for w in allWords:
        try:
            result[w] = wordCountList[w]/size1*wordCountList2[w]/size2
        except KeyError:
            result[w] = 0
    return sum(result.values())

def BM25Similarity(wordCountList={}, wordCountList2={}, allWords=[], k=0, b=0, avgDocLength = 1,**kwargs):


    if len(allWords) == 0:
        allWords = list(wordCountList.keys())[:]
        allWords.extend(list(wordCountList2.keys())[:])

    total = sum(wordCountList.values())
    
    for w in allWords:
        try:
            wordCountList[w] = wordCountList[w]*(k+1)/(wordCountList[w]+k*(1-b+b*total)/avgDocLength)
        except KeyError:
            wordCountList[w] = 0

    total = sum(wordCountList2.values())
    
    for w in allWords:
        try:
            wordCountList2[w] = wordCountList2[w]*(k+1)/(wordCountList2[w]+k*(1-b+b*total)/avgDocLength)
        except KeyError:
            wordCountList2[w] = 0
    result ={}

    total1=sum(wordCountList.values())
    total2=sum(wordCountList2.values())

    for w in allWords:
        result[w] = wordCountList[w]/total1*wordCountList2[w]/total2

    return sum(result.values())


def getIDF(documents=[], allWords=[]):
    
    if len(allWords) == 0:
        allWords = getAllWords(documents)

    wordLists = []
    for d in documents:
        wordLists.append(getAllWords(d))
    
    totalDocs = len(documents)
    result={}

    for w in allWords:
        docsContaining = 0
        for wl in wordLists:
            if w in wl:
                docsContaining= docsContaining+1
        if docsContaining>0:
            result[w] = math.log((1+totalDocs)/(docsContaining))
        else:
            result[w] = 0
    return result



def getIDFSimilarity(wordCountList={},wordCountList2={},idf={},**kwargs):

    result ={}
    size1=sum(wordCountList.values())
    size2=sum(wordCountList2.values())

    for w in idf.keys():
        try:
            result[w] = wordCountList[w]/size1*wordCountList2[w]/size2*idf[w]
        except KeyError:
            result[w] = 0
    return sum(result.values())



def getAllSimilarities(documents =[] , sim = basicSimilarity, **kwargs):
    sim(wordCountList={'A':1,'B':2}, wordCountList2={'A':1,'B':1,'C':3,'D':4}, k=kwargs['k'], b= kwargs['b'], documentCount=1)

#getAllSimilarities(documents=[], sim = basicSimilarity,k=1,b=6)
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