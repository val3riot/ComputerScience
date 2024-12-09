def pt1(outl):
    lens=len(outl)
    i=lens-1
    idx=0
    while i>=0:
        if outl[i] is not None:
            for j in range(idx,i):
                if outl[j] is None:
                    outl[j]=outl[i]
                    outl.pop(i)
                    idx=j+1
                    lens=lens-1
                    break
        i-=1
    return outl
def checksum(outl):
    count=0
    for e in range(0,len(outl)):
        if not outl[e] is None:
            count+=(outl[e]*e)
    print(count)
def find_repeated_number(lst, num, sequence_length):
    for i in range(len(lst) - sequence_length + 1):
        sublist = lst[i:i + sequence_length]
        if sublist == [num] * sequence_length:
            return i
    return -1
def pt2(outl):
    #soluzione lenta pezzotta
    lens=len(outl)
    i=lens-1
    while i>0:
        if outl[i] is None:
            i-=1
            continue
        n=0
        for j in range(i,-1,-1):
            if outl[j]!=outl[i]:
                break
        idx = find_repeated_number(outl[0:j+1],None,i-j)
        if idx==-1:
            i-=(i-j)
            continue
        for j in range(idx,idx+i-j):
            outl[j]=outl[i]
            outl[i]=None
            i-=1
    return outl
content = ''.join(open('input2','r'))
outl=[]
i=0
c=0
while i < len(content):
    if i%2 ==0:
        if int(content[i]) != 0:
            for cc in range(0,int(content[i])):
                outl.append(c)
            c+=1
    else:
        for cc in range(0,int(content[i])):
            outl.append(None)
    i+=1
outl = pt2(outl)
checksum(outl)