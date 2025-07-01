#dato un arrai A[1:n] di n bit, A[i]\in{0,1}, trovare l'indice k dell'ultimo 0
#T(n)=log(n) e T(n)=log(k)
def flz(A,i,j):
    m =  int((i+j)/2)
    if (A[m] == 0 and A[m+1]==1):
        return m
    elif A[m]==0:
        return flz(A,m+1,j)
    else:
        return flz(A,i,m-1)
def find_last_zero(A):
    n = len(A)-1
    if n==0:
        return -1
    if A[n]==0:
        return n
    return flz(A,0,n)
def find_last_zero_faster(A):
    n = len(A)-1
    if n==0:
        return -1
    if A[n]==0:
        return n
    i=0
    while not (A[pow(2,i)] == 0 and A[pow(2,i+1)] ==1):
        i+=1
    return flz(A,pow(2,i),pow(2,i+1)+1)
def es1():
    A=[0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1]
    print(find_last_zero_faster(A))

#dato un vettore A[1:n] di n bit, A[1]\in{0,1}, trovare un indice k tale che il numero di zeri in A[1:k]
#sia uguale al numero di uni in A[k+1:n].
#T(n)=O(n)
def find_k_bil(A):
    i=1
    j=len(A)-2
    zeri=[0]*len(A)
    zeri[0]=1 if A[0]==0 else 0
    uni=[0]*len(A)
    while i<len(A) and j>=0:
        zeri[i]=zeri[i-1]+ (1 if A[i] == 0 else 0)
        uni[j] = uni[j+1]+ A[j]
        i+=1
        j-=1
    for k in range(0,len(zeri)):
        if zeri[k]==uni[k]:
            return k
    return -1
def es2():
    A=[0,0,1,0,1,1,1,0]
    print(find_k_bil(A))


def main():
    #es1()
    es2()
if __name__=='__main__':
    main()
