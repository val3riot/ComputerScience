map ={
    'one':1,
    'two':2,
    'three':3,
    'four':4,
    'five':5,
    'six':6,
    'seven':7,
    'eight':8,
    'nine':9
}
def mapNumber(string):
    out=[]
    substrings = []
    n = len(string)
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.append(string[i:j])
    for ss in substrings:
        if ss.isdigit():
            out.append(str(ss))     
        elif ss in map.keys():
            out.append(str(map.get(ss))) 
    if(len(out) == 0):
        return 0
    if(len(out) == 1):
        return int(out[0]+out[0])
    return int(out[0]+out[-1])

with open('input_1.txt','r') as file:
    out =0
    text =[riga.rstrip('\n') for riga in file]
    for s in text:
        out+=mapNumber(s)
        
print(out)
