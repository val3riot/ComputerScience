def findGuard(rows):
    for i in range(0,len(rows)):
        for j in range(0,len(rows[i])):
            if rows[i][j]=='^':
                return i,j
    return
def checkVisit(i,j,rows):
    if rows[i][j]=='X':
        return rows
    riga = list(rows[i])
    riga[j]='X'
    rows[i]=''.join(riga)
    return rows
def ostacolo(i,j,r):
    rows=list(r)
    if rows[i][j]=='#' or rows[i][j]=='^':
        return []
    riga = list(rows[i])
    riga[j]='#'
    rows[i]=''.join(riga)
    return rows
def move(i,j,guard,rows):
    if (guard == '^' and i==0) or (guard == '>' and j==len(rows[0])-1) or(guard == 'v' and i==len(rows)-1) or (guard == '<' and j==0):
        rows=checkVisit(i,j,rows)
        return -1,-1,guard,rows
    if guard == '^':
        if rows[i-1][j]=='#':
            return i,j,'>',rows
        rows=checkVisit(i-1,j,rows)
        return i-1,j,'^',rows
    if guard == '>':
        if rows[i][j+1]=='#':
            return i,j,'v',rows
        rows=checkVisit(i,j+1,rows)
        return i,j+1,'>',rows
    if guard == '<':
        if rows[i][j-1]=='#':
            return i,j,'^',rows
        rows=checkVisit(i,j-1,rows)
        return i,j-1,'<',rows 
    if guard == 'v': 
        if rows[i+1][j]=='#':
            return i,j,'<',rows
        rows=checkVisit(i+1,j,rows)
        return i+1,j,'v',rows


fileContent=''.join(open('test2','r'))
r=fileContent.split('\n')
posi,posj=findGuard(r)
''' fase 1
r=checkVisit(i,j,r)
sum=0
for rr in r:
    for c in range(0,len(rr)):
        if(rr[c]=='X'):
            sum+=1

print(r)
print(sum)'''
#fase 2
guard='^'
cicli=0
for ii in range(0,len(r)):
    for jj in range(0,len(r[0])):
        rr=ostacolo(ii,jj,r)
        i,j=posi,posj
        guard='^'
        if len(rr)==0:
            continue
        print('ostacolo: ', ii,jj)
        percorso=set()
        while True:
            if i<0 or i>=len(rr) or j<0 or j>=len(rr[0]):
                break
            percorso.add((i,j,guard))
            i,j,guard,rr=move(i,j,guard,rr)
            if  (i,j,guard) in percorso:
                print('ciclo:',ii,jj)
                cicli+=1
                break
print(cicli)
