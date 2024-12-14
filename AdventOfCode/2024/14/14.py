

mx=101
my=103
it=100
fileContent=''.join(open('test2','r')).split('\n')
robot=[]

for r in fileContent:
    r1,r2=r.split()
    r1=list(map(int,r1[2:].split(',')))
    r2=list(map(int,r2[2:].split(',')))
    robot.append((r1,r2))

q1=0
q2=0
q3=0
q4=0
matrix = []
ss=set()
for r in range(my):
    r=[]
    for c in range(mx):
        r.append('.')
    matrix.append(r)

t=len(robot)

for s in range(it*it):
    ss=set()
    for r in robot:
        x,y=r[0]
        vx,vy=r[1] 
        fx=(x+s*vx)%mx
        fy=(y+s*vy)%my
        matrix[vy][vx]='*'
        ss.add((fx,fy))
        if s == 100:
            if 0<=fx<mx//2 and fy <my//2:
                q1+=1
            if mx//2<fx<mx and fy <my//2:
                q2+=1
            if 0<=fx<mx//2 and my//2<fy<my:
                q3+=1
            if mx//2<fx<mx and  my//2<fy<my:
                q4+=1
    if len(ss)==t:
        print(s)
        break
for s in ss:
    matrix[s[1]][s[0]]='#'
#giocare con lo zoom del terminale per vedere
print(matrix)
print(q1*q2*q3*q4)
