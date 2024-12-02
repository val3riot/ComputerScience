


def splitStringListSorted(list):
    list1=[]
    list2=[]
    for s in list:
        sx = s.split("   ")[0]
        dx = s.split("   ")[1]
        list1.append(int(sx))
        list2.append(int(dx))
    list1.sort()
    list2.sort()
    return list1,list2
def calcolaDistanzaTotale(list1, list2):
    i=0
    out=0
    #len(list1) == len(list2)
    while i<len(list1):
        out+=abs(list1[i]-list2[i])
        i+=1
    return out
def calcolaSimilarita(l1,l2):
    out=0
    for e1 in l1:
        counter = 0
        for e2 in l2:
            if(e2 == e1):
                counter+=1
        out+=(e1*counter)
    return out


if __name__== "__main__":
   fileName="test_1.txt"
   fileContent =''.join(open(fileName, "r").readlines()).split("\n")
   l1,l2=splitStringListSorted(fileContent)
   print(calcolaDistanzaTotale(l1,l2))
   print(calcolaSimilarita(l1,l2))