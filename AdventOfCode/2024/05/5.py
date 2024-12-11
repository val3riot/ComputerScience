fileContent=''.join(open('test2','r'))
ordinamenti,pagine=fileContent.split('\n\n')
pagineList=[]
for r in pagine.split('\n'):
    t=[]
    for p in r.split(','):
        t.append(int(p))
    pagineList.append(t)
mappa={}
for o in ordinamenti.split('\n'):
    i,j=map(int, o.split('|'))
    if(not mappa.get(i)):
        mappa[i]=[j]
    else:
        mappa[i].append(j)

sum=0
print(mappa)
for pp in pagineList:
    tempList=pp
    corretto=True
    for p in tempList:
        if p in list(mappa.keys()):
            values=list(set(tempList) & set(mappa.get(p)))
            add=False
            for value in values:
                if tempList.index(p)>tempList.index(value):
                    corretto=False
                    add=True
                    elemento = tempList.pop(tempList.index(p))
                    tempList.insert(tempList.index(value),p)
        #rimuovere commento
        #if corretto:
            #break
    if(not corretto):
        i=len(tempList)-1
        if(i%2==0):
            print(tempList[len(tempList) //2])
            sum+=tempList[len(tempList) //2]
        else:
            print(tempList[len(tempList) //2-1])
            sum+=tempList[len(tempList) // 2-1]
print(sum)