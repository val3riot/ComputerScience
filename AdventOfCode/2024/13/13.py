
def sol_matrice(a, b, c):
    a1, a2 = a
    b1, b2 = b
    c1, c2 = c
    det = a1 * b2 - a2 * b1
    if det == 0:
        return None
    i = (c1 * b2 - c2 * b1) / det
    j = (a1 * c2 - a2 * c1) / det
    if i < 0:
        k = (-i + (b2 / det) - 1) // (b2 / det)
    else:
        k = 0
    i = i + k * (b2 / det)
    j = j - k * (a2 / det)
    if j < 0:
        k = (-j + (a2 / det) - 1) // (a2 / det)
        i = i - k * (b2 / det)
        j = j + k * (a2 / det)
    if i.is_integer() and j.is_integer() and i >= 0 and j >= 0 :
        return i,j
    else:
        return None


fileContent=''.join(open('test2','r')).split('\n\n')
sol1=0
sol2=0
for fc in fileContent:
    rows=fc.strip().split('\n')
    a=(int(rows[0][rows[0].find('X+')+2:rows[0].find(',')]),int(rows[0][rows[0].find('Y+')+2:]))
    b=(int(rows[1][rows[1].find('X+')+2:rows[1].find(',')]),int(rows[1][rows[1].find('Y+')+2:]))
    r2=(int(rows[2][rows[2].find('X=')+2:rows[2].find(',')])+10000000000000,int(rows[2][rows[2].find('Y=')+2:])+10000000000000)
    r1=(int(rows[2][rows[2].find('X=')+2:rows[2].find(',')]),int(rows[2][rows[2].find('Y=')+2:]))
    s1=sol_matrice(a,b,r1)
    s2=sol_matrice(a,b,r2)
    if s1 is not None:
        sol1+=(3*s1[0]+s1[1])
    if s2 is not None:
        sol2+=(3*s2[0]+s2[1])
print(f'parte 1: {int(sol1)}')
print(f'parte 2: {int(sol2)}')
