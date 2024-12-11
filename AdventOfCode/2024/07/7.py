import itertools

def calcola(nums,operators):
    sum=nums[0]
    i=0
    for o in operators:
        if o == '+':
            sum += nums[i+1]
        elif o == '*':
            sum *=nums[i+1]
        elif o == '||':
            el = str(sum)+str(nums[i+1])
            sum=int(el)
        i+=1
    return sum
fileContent=''.join(open('test2','r')).split("\n")
counter=0
#per parte 1 togliere l'operatore || dalla lista passata a product
for f in fileContent:
    r =int(f.split(":")[0])
    nums=list(map(int,(f.split(":")[1]).split()))
    l_nums=len(nums)-1
    operators=[x for x in itertools.product(['+','*','||'], repeat=l_nums)]
    res=[]
    for o in operators:
        res.append(calcola(nums,o))
    if r in res:
        counter +=r
print(counter)