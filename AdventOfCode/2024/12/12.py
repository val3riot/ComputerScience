direction={(-1,0),(0,-1),(1,0),(0,1)}
def dfs(matrice, x, y, visited, val):
    stack = [(x, y)]
    visited[x][y] = True
    area = 0
    perimetro=0
    lati=0
    p_node=[]
    while stack:
        cx, cy = stack.pop()  
        area += 1    
        for dx, dy in direction:
            nx, ny = cx + dx, cy + dy  
            if 0 <= nx < len(matrice) and 0 <= ny < len(matrice[0]):
                if  val != matrice[nx][ny]:
                    p_node.append(((cx,cy),(nx,ny)))
                    perimetro+=1
            else:
                p_node.append(((cx,cy),(nx,ny)))
                perimetro+=1           
            if 0 <= nx < len(matrice) and 0 <= ny < len(matrice[0]) and not visited[nx][ny]:
                if matrice[nx][ny] == val: 
                    visited[nx][ny] = True
                    stack.append((nx, ny))
    for n0,n1 in p_node:
        c_lato=True
        for dx,dy in [(1,0),(0,1)]:
            l1=(n0[0]+dx,n0[1]+dy)
            l2=(n1[0]+dx,n1[1]+dy)
            if(l1,l2)in p_node:
                c_lato=False
        if c_lato:
            lati+=1
    return area,perimetro,lati

def trova_regioni(matrice):
    rows, cols = len(matrice), len(matrice[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    regioni = []
    
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]: 
                valore = matrice[i][j]
                area,perimetro,lati = dfs(matrice, i, j, visited, valore)
                regioni.append((valore, area,perimetro,lati))
    return regioni
file=''.join(open('test2','r')).split('\n')

regioni=trova_regioni(file)
pt1=0
pt2=0
for r in regioni:
    pt1+=(r[1]*r[2])
    pt2+=(r[1]*r[3])
print(regioni)
print(f'pt1: {pt1}')
print(f'pt2: {pt2}')
