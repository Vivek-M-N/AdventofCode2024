#Day 4

content = []
letters = {}
xloc = []
aloc = []

with open('4.txt', 'r') as file:
    content = file.read().split('\n')

#letters = [[0 for a in range(len(content[1]))]for b in range(len(content))]

for j in range(len(content)):
    l = content[j]
    for i in range(len(l)):
        c = l[i]
        letters[j,i] = c
        if c == 'X':
            xloc.append((j,i))
        if c == 'A':
            aloc.append((j,i))

xmascount = 0

for loc in xloc:
    [j,i] = [loc[0],loc[1]]
    try:
        nn = 'X'+letters[j-1,i]+letters[j-2,i]+letters[j-3,i]
    except KeyError:
        nn=''
    
    try:
        ss = 'X'+letters[j+1,i]+letters[j+2,i]+letters[j+3,i]
    except KeyError:
        ss=''

    try:
        ww = 'X'+letters[j,i-1]+letters[j,i-2]+letters[j,i-3]
    except KeyError:
        ww=''

    try:
        ee = 'X'+letters[j,i+1]+letters[j,i+2]+letters[j,i+3]
    except KeyError:
        ee=''

    try:
        nw = 'X'+letters[j-1,i-1]+letters[j-2,i-2]+letters[j-3,i-3]
    except KeyError:
        nw=''

    try:
        ne = 'X'+letters[j-1,i+1]+letters[j-2,i+2]+letters[j-3,i+3]
    except KeyError:
        ne=''

    try:
        sw = 'X'+letters[j+1,i-1]+letters[j+2,i-2]+letters[j+3,i-3]
    except KeyError:
        sw=''

    try:
        se = 'X'+letters[j+1,i+1]+letters[j+2,i+2]+letters[j+3,i+3]
    except KeyError:
        se=''
        
    xmascount+=(1*(nn=='XMAS')+1*(ss=='XMAS')+1*(ww=='XMAS')+1*(ee=='XMAS'))
    xmascount+=(1*(nw=='XMAS')+1*(ne=='XMAS')+1*(sw=='XMAS')+1*(se=='XMAS'))

    #print(nn,ss,ww,ee,nw,ne,sw,se)

print("Puzzle 1")
print(xmascount)

mascount = 0
     
for loc in aloc:
    [j,i] = [loc[0],loc[1]]
    #print(loc)
    try:
        nw = letters[j-1,i-1]+'A'+letters[j+1,i+1]
    except KeyError:
        nw=''

    try:
        ne = letters[j-1,i+1]+'A'+letters[j+1,i-1]
    except KeyError:
        ne=''

    if ((nw == 'MAS' or nw == 'SAM') and (ne == 'MAS' or ne == 'SAM')):
        #print(nw,ne)
        mascount+=1

print("Puzzle 2")
print(mascount)
