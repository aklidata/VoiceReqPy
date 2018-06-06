A='hello sir bestest lucky'
R='hello sir best lucky'
M='jaguar is a beautiful car'
#comparaison des mots: check if ch fits in sh
def compare(ch,sh):
    e=ch[0]
    for i in range(len(sh)):
        if sh[i]==ch[0]:
            k=i
            l=1
            for j in range(1,len(ch)):
                k+=1
                if sh[k]!=ch[j]:
                    break;
                l+=1
            if l==len(ch):
                return True
    return False
#search for ch1 (characters) in ch2 (charcters)
def exist(ch1,ch2):
    searchin=ch2.split()
    searchfor=ch1.split()
    e=0
    for i in range(len(searchfor)):
        for j in range(len(searchin)):
            if searchfor[i]==searchin[j]:
                e+=1
    if e!=0:return True
    else: return False
#if ch charcter matches one of the charcters on list L
def match(ch,L):
    for i in range(len(L)):
        if exist(ch,L[i]):
            return True
    return False
#match a sentence on a list L:
def matchG(sentence,L):
    sp=sentence.split()
    for i in range(len(sp)):
        if match(sp[i],L):
            return True
    return False
#count match
def countmatch(sentence,L):
    sp=sentence.split()
    e=0
    for i in range(len(sp)):
        if match(sp[i],L):
            e+=1
    return e
    
    
    
    
    
    
    
    