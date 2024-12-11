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
def find_repeated_number_opt(lst, num, value, sequence_length, start, end):
    for i in range(len(lst[0:start+1]) - sequence_length + 1):
        sublist = lst[i:i + sequence_length]
        if sublist == [num] * sequence_length:
            for j in range(i,i + sequence_length):
                lst[j] = value
            lst = clear_old_value(lst,start,end)
            break
    return lst
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
def clear_old_value(outl,j,i):
    for ii in range(j+1,i+1):
        outl[ii] = None
    return outl
def pt2_opt(outl):
    #soluzione ottimale
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
        outl = find_repeated_number_opt(outl,None,outl[i],i-j,j,i)
        i-=(i-j)
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
outl = pt2_opt(outl)
print(outl)
checksum(outl)