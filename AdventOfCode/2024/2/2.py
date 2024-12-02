# pezzotto time

def check(list):
    count=0
    for el in list:
        subl=[int(e) for e in el.split(" ")]
        j=0
        check=True
        salita=discesa=False
        if subl[0]<subl[1]:
            salita=True
        else:
            discesa=True
        while j<len(subl)-1:
            if( subl[j]==subl[j+1] or
                (salita and
                (subl[j]>subl[j+1] or
                 subl[j+1]-subl[j]>3))or
                 (discesa)and(subl[j]<subl[j+1] or subl[j]-subl[j+1]>3)
            ):
                check=False
            j+=1
        if(check):
            count+=1
    print(count)
    return count


def check2(list):
    count=0
    subl2=[]
    for el in list:
        subl=[int(e) for e in el.split(" ")]
        j=0
        check=True
        first=True
        salita=discesa=False
        if subl[0]<subl[1]:
            salita=True
        else:
            discesa=True
        
        while j<len(subl)-1:
            if( subl[j]==subl[j+1] or
                (salita and
                (subl[j]>subl[j+1] or
                 subl[j+1]-subl[j]>3))or
                 (discesa)and(subl[j]<subl[j+1] or subl[j]-subl[j+1]>3)
            ):
                check=False
                subl2.append(subl)
                break                             
            j+=1
        if(check):
            count+=1
    for el in subl2:
        sottoliste = [el[:i] + el[i+1:] for i in range(len(el))]
        for ss in sottoliste:
            j=0
            check=True
            salita=discesa=False
            if ss[0]<ss[1]:
                salita=True
            else:
                discesa=True
            
            while j<len(ss)-1:
                if( ss[j]==ss[j+1] or
                    (salita and
                    (ss[j]>ss[j+1] or
                    ss[j+1]-ss[j]>3))or
                    (discesa)and(ss[j]<ss[j+1] or ss[j]-ss[j+1]>3)
                ):
                    check=False
                    break                             
                j+=1
            if(check):
                count+=1
                break
    print(count)
    return count

if __name__== "__main__":
    fileName="test_2.txt"
    fileContent =''.join(open(fileName, "r").readlines()).split("\n")
    check2(fileContent)