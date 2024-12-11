
temp_L={}
def calcola(el):
    s = str(el)
    split=len(s)//2
    left=s[:split]
    right=s[split:]
    temp_L[el]=[int(left),int(right)]
    return int(left),int(right)
temp_S={}
def it_list(el,t):
    if (el,t) in temp_S:
        return temp_S[(el,t)]
    if t ==0:
        out= 1
    elif el == 0:
        out= it_list(1,t-1)
    elif len(str(el))%2==0:
        if el in temp_L:
            l,r=temp_L[el]
        else:
            l,r=calcola(el)
        out= it_list(l,t-1) + it_list(r,t-1)
    else:
        if el not in temp_L:
            temp_L[el]=[el*2024]
        v=temp_L[el]
        out= it_list(v[0],t-1)
    temp_S[(el,t)]=out
    return out

file=[int(r) for r in ''.join(open('test2','r')).split()]
lista=file
s=0
for el in lista:
    s+=it_list(el,75)
print(s)
        
            