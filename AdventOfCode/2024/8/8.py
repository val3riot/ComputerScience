import itertools
rows = ''.join(open('test2','r')).split('\n')
antinodes=set()
antenne={}
print('mappa ',len(rows), ' ',len(rows[0]))
for r in range(0,len(rows)):
    for c in range(0, len(rows[r])):
        el = rows[r][c]
        if el.isalnum():
            if el in antenne.keys():
                antenne[el].append((r,c))
            else:
                antenne[el]=[(r,c)]
for a in antenne:
    for p in itertools.combinations(antenne[a], 2):
        pos1=p[0]
        pos2=p[1]
        dx = pos1[0]-pos2[0]
        dy = pos1[1]-pos2[1] 
        '''pt1
        pos3=(pos1[0]-dx*2,pos1[1]-dy*2)
        if 0<=pos3[0] <len(rows) and 0<=pos3[1]<len(rows[0]):
                antinodes.add(pos3)
        pos4=(pos2[0]+dx*2,pos2[1]+dy*2)
        if 0<=pos4[0]<len(rows) and 0<=pos2[1]+dy*2<len(rows[0]):
                antinodes.add(pos4)
        print(f"pos1:{pos1} pos2:{pos2} pos3:{pos3} pos4:{pos4}")
        '''
        '''pt2  '''
        antinodes.add(pos1)
        antinodes.add(pos2)
        pos3 = (pos1[0]-dx,pos1[1]-dy)
        while 0<=pos3[0]<len(rows) and 0<=pos3[1] and pos3[1]<len(rows[0]):
            antinodes.add(pos3)
            pos3 = (pos3[0]-dx,pos3[1]-dy)
        pos4 = (pos2[0]+dx,pos2[1]+dy) 
        while 0<=pos4[0]<len(rows) and 0<=pos4[1] and pos4[1]<len(rows[0]):
            antinodes.add(pos4)
            pos4 = (pos4[0]+dx,pos4[1]+dy)    
        
print(len(antinodes))
