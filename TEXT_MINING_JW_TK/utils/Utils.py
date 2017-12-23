
def removeRedundantSpaces(word=""):
    if len(word)<1:
        return word

    if word[0] == " ":
        word = word[1:]
    if word[-1] == " ":
        word = word[:-1]
        while word.find("  ") !=-1:
            word = word.replace("  "," ")
    return word

def longestWord(words = []):
    out = words[0]
    for w in words:
        if len(w) > len(out):
            out = w
    return out

def letterCombo():
    letters = "abcdefghijklmnopqrstuvwyzęóąśłżźćń"
    out1 = []
    out2 = []
    out3 = []
    print(letters)
    for l1 in letters:
        out1.append(l1)
        for l2 in letters:
            out2.append(l1 + l2)
            for l3 in letters:
                out3.append(l1 + l2 + l3)

    out = out1
    out.extend(out2)
    out.extend(out3)
    return out

def countPatternOccurances(pattern="",word=""):
    count =0
    flag=True
    start=0
    while flag:
        a = word.find(pattern,start)  # find() returns -1 if the word is not found, 
                                      #start i the starting index from the search starts(default value is 0)
        if a==-1:          #if pattern not found set flag to False
            flag=False
        else:               # if word is found increase count and set starting index to a+1
            count+=1        
            start=a+1
    return count
