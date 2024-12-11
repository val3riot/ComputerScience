def checkWord(r,c,matrix):
    #verifico stessa riga destra e sinistra
    counter=0
    row=matrix[r]
    comp=row[c]
    for i in range(c,len(row)-1):
        if row[i]=='S':
            break
        if DICT.get(row[i])==row[i+1]:
            comp+=row[i+1]
        else:
            break
    if(comp == 'XMAS'):
        counter+=1
    comp=row[c]
    for i in range(c,-1,-1):
        if row[i]=='S':
            break
        if DICT.get(row[i])==row[i-1]:
            comp+=row[i-1]
        else:
            break
    if(comp == 'XMAS'):
        counter+=1  
    #verifico righe sopra verticale
    comp=matrix[r][c]
    for i in range(r,-1,-1):
        if matrix[i][c]=='S':
            break
        if DICT.get(matrix[i][c])==matrix[i-1][c]:
            comp+=matrix[i-1][c]
        else:
            break
    if(comp == 'XMAS'):
        counter+=1
    #verifico righe sotto verticale
    comp=matrix[r][c]
    for i in range(r,len(matrix)-1):
        if matrix[i][c]=='S':
            break
        if DICT.get(matrix[i][c])==matrix[i+1][c]:
            comp+=matrix[i+1][c]
        else:
            break
    if(comp == 'XMAS'):
        counter+=1
    #verifica diagonale
    comp=matrix[r][c]
    i=r
    j=c
    while i < len(matrix)-1 and j < len(matrix[0])-1:
        if(matrix[i][j]=='S'):
            break
        if DICT.get(matrix[i][j])==matrix[i+1][j+1]:
            comp+=matrix[i+1][j+1]
        else:
            break
        i += 1
        j += 1
    if(comp == 'XMAS'):
        counter+=1  
    comp=matrix[r][c]
    i=r
    j=c
    while i >0 and j >0:
        if(matrix[i][j]=='S'):
            break
        if DICT.get(matrix[i][j])==matrix[i-1][j-1]:
            comp+=matrix[i-1][j-1]
        else:
            break
        i -= 1
        j -= 1
    if(comp == 'XMAS'):
        counter+=1  
    comp=matrix[r][c]
    i=r
    j=c
    while i <len(matrix)-1 and j >0:
        if(matrix[i][j]=='S'):
            break
        if DICT.get(matrix[i][j])==matrix[i+1][j-1]:
            comp+=matrix[i+1][j-1]
        else:
            break
        i += 1
        j -= 1
    if(comp == 'XMAS'):
        counter+=1  
    comp=matrix[r][c]
    i=r
    j=c
    while i >0 and j<len(matrix[0])-1 :
        if(matrix[i][j]=='S'):
            break
        if DICT.get(matrix[i][j])==matrix[i-1][j+1]:
            comp+=matrix[i-1][j+1]
        else:
            break
        i -= 1
        j += 1
    if(comp == 'XMAS'):
        counter+=1
    return counter

def checkMAS(r,c,matrix):
    if r==0 or c == 0 or r == len(matrix)-1 or c == len(matrix[0])-1:
        return 0
    dic=['MAS','SAM']
    word1=matrix[r-1][c-1]+matrix[r][c]+matrix[r+1][c+1]
    word2=matrix[r+1][c-1]+matrix[r][c]+matrix[r-1][c+1]
    if(word1 in dic and word2 in dic):
        return 1
    return 0


matrix=''.join(open('test_2','r')).split('\n')
DICT={
    'X':'M',
    'M':'A',
    'A':'S'
}
counterX=0
counter=0
for r in range(0,len(matrix[0])):
    for c in range(0,len(matrix[r])):
        if(matrix[r][c] =='X'):
            counterX+=checkWord(r,c,matrix)
        if(matrix[r][c]=='A'):
            counter+=checkMAS(r,c,matrix)
print(counter)