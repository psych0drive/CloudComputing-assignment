def readfile(file):
    content=[]
    stopword=['and','i','to','an','the','of','it','a']
    for line in file:
        words=line.split(" ")
        for word in words:
            if word.lower() not in stopword:
                content.append(word)
    return content

def wordcount(content):
    d=dict()
    for word in content:
        word=word.lower()
        if word in d:
            d[word]=d[word]+1
        else: 
            d[word]=1
    return d

def toptenwords(wordcountdct):
    ls=sorted(wordcountdct.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)
    res =[]
    for i in range(0,10):
        res.append(ls[i][0])
    return res

def main():
    file=open("sample.txt",'r')
    content=readfile(file)
    wordcountdct=wordcount(content)
    res=toptenwords(wordcountdct)
    for i in res:
        print(i)

if __name__=='__main__':
    main()

