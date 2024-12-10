def find_trailhead(matrice,r,c,visited=None):
    if visited is None:
        visited=set()
    current = int(matrice[r][c])
    next =current+1
    if current==9:
        visited.add((r,c))
        return visited
    if c>0 and matrice[r][c-1]==next:
        find_trailhead(matrice,r,c-1,visited)
    if c<len(matrice[r])-1 and matrice[r][c+1]==next:
        find_trailhead(matrice,r,c+1,visited)
    if r>0 and matrice[r-1][c]==next:
        find_trailhead(matrice,r-1,c,visited)
    if r<len(matrice)-1 and matrice[r+1][c]==next:
        find_trailhead(matrice,r+1,c,visited)
    return visited
def find_trailhead2(matrice,r,c,visited=None):
    if visited is None:
        visited=set()
    current = int(matrice[r][c])
    next =current+1
    if current==9:
        return 1
    total =0
    visited.add((r,c))
    if c>0 and matrice[r][c-1]==next and (r,c-1) not in visited:
        total+=find_trailhead2(matrice,r,c-1,visited)
    if c<len(matrice[r])-1 and matrice[r][c+1]==next and (r,c+1) not in visited:
        total+=find_trailhead2(matrice,r,c+1,visited)
    if r>0 and matrice[r-1][c]==next and (r-1,c) not in visited:
        total+=find_trailhead2(matrice,r-1,c,visited)
    if r<len(matrice)-1 and matrice[r+1][c]==next and (r+1,c) not in visited:
        total+=find_trailhead2(matrice,r+1,c,visited)
    visited.remove((r,c))
    return total


file = ''.join(open('test2','r')).split('\n')
matrice = []
for stringa in file:
    numeri = [int(stringa[i]) for i in range(0, len(stringa))]
    matrice.append(numeri)
count=0
for r in range(0,len(matrice)):
    row = matrice[r]
    for c in range(0,len(row)):
        if row[c] == 0:
            '''pt1
                        visited = find_trailhead(matrice,r,c)
            count+=len(visited)
            '''
            '''pt2'''
            count+=find_trailhead2(matrice,r,c)
print(count)