def checkMul(str):
    check=str.find('mul(')
    if check!=-1:
        return check+4
    return -1
def findEnable(str, last):
    do=str.find('do()')
    do_not=str.find('don\'t()')
    if((do==-1 and  do_not==-1 and last) or (do>-1)):
        return True
    return False
        
def checkNumberSequence(str):
    i=0
    num1=''
    num2=''
    if(not str[0].isdigit()):
        return 0,-1
    while str[i]!=",":
        if not str[i].isdigit():
            return 0,-1
        num1+=str[i]
        i+=1
    i+=1
    if(not str[i].isdigit()):
        return 0,-1
    while str[i]!=')':
        if not str[i].isdigit():
            return 0,-1
        num2+=str[i]
        i+=1
    return int(num1)*int(num2),i

file=''.join(open('test_2','r'))

i=0
sum=0
enable=True
while i<len(file):
    start=checkMul(file[i:])
    #enable per pt 2
   #enable=findEnable(file[i:i+start],enable)
    if(start>=0):
        i+=start
        add,i_1=checkNumberSequence(file[i:])
        if i_1>=0:
            if(enable):
                sum+=add
            i+=(i_1+1)
    else:
        i+=1
print(sum)


    
