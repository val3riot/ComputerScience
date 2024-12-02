def checkWin(list1,list2):
    value = 0
    c=0
    for el in list2:
        if el in list1:
            if value ==0:
                value=1
                c=1
            else:
                value*=2
                c+=1
    return value,c
def set_map(i,map,count):
    for c in range(i+1,i+count+1):
            if(map.get(c)):
                map.update({c:map.get(c)+1})



rows = "".join(open('test_2','r')).split('\n')
count=0
repeatMap={i:1 for i in range(0,len(rows))}
for i in range(0,len(rows)):
    row=rows[i]
    el1=[el for el in row[row.find(':')+2:row.find('|')-1].split(" ") if el!='']
    el2=[el for el in row[row.find('|')+2::].split(" ") if el!='']
    win,c=checkWin(el1,el2)
    for r in range(0,repeatMap.get(i)):
        set_map(i,repeatMap,c)
    count+=win
print(count)
count=0
for el in repeatMap.values():
    count+=el
print(count)

