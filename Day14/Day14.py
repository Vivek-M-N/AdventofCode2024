#Day 14

import re

locs = {}
im = 0+1j

'''
Imaginary axis used to solve

----> +x
|
|
v y
'''

botid = 0
vlist = {}
with open('14.txt', 'r') as file:
    content = file.read().split('\n')
    [width,height] = content[0].split(',')
    height = int(height); width = int(width)
    for line in content[1:]:
        [p,v] = line.split(' ')
        [x,y] = re.findall('\d+',p)
        v = v.split(',')
        vx = int(v[0].strip('v=')); vy = int(v[1])
        locs[botid] = (int(x))+(int(y))*im
        vlist[botid] = (vx+vy*im)
        botid+=1

#print(locs)
#print(vlist)

tframe = 0
for t in range(100):
    for [botid, loc] in list(locs.items()):
        #print(botid)
        new_loc = loc + vlist[botid]
        if 0<=new_loc.real<width and 0<=new_loc.imag<height:
            locs[botid] = new_loc
        else:
            #if botid == 10:
                #print('x'+str(new_loc))
            if new_loc.real<0:
                new_loc = width+new_loc.real + new_loc.imag*im
            elif new_loc.real>width-1:
                new_loc = new_loc.real-width + new_loc.imag*im
            if new_loc.imag<0:
                new_loc = new_loc.real + (height+new_loc.imag)*im
            elif new_loc.imag>height-1:
                new_loc = new_loc.real + (new_loc.imag-height)*im
            locs[botid] = new_loc

#print(locs)

q1 = 0
q2 = 0
q3 = 0
q4 = 0

for loc in locs.values():
    if loc.real < int(width/2) and loc.imag < int(height/2):
        q1+=1
    elif loc.real > int(width/2) and loc.imag < int(height/2):
        q2+=1
    elif loc.real < int(width/2) and loc.imag > int(height/2):
        q3+=1
    elif loc.real > int(width/2) and loc.imag > int(height/2):
        q4+=1

print("Puzzle 1")
print(q1*q2*q3*q4)

tframe = 0
for t in range(101*103):
    pos = [['.' for a in range(width)]for b in range(height)]
    for [botid, loc] in list(locs.items()):
        #print(botid)
        new_loc = loc + vlist[botid]
        if 0<=new_loc.real<width and 0<=new_loc.imag<height:
            locs[botid] = new_loc
        else:
            #if botid == 10:
                #print('x'+str(new_loc))
            if new_loc.real<0:
                new_loc = width+new_loc.real + new_loc.imag*im
            elif new_loc.real>width-1:
                new_loc = new_loc.real-width + new_loc.imag*im
            if new_loc.imag<0:
                new_loc = new_loc.real + (height+new_loc.imag)*im
            elif new_loc.imag>height-1:
                new_loc = new_loc.real + (new_loc.imag-height)*im
            locs[botid] = new_loc
        pos[int(new_loc.imag)][int(new_loc.real)] = 'X'

    if t == 99:
        loc100 = locs
    
    for line in pos:
        if re.findall('XXXXXXXXX',''.join(line)):
            tframe = t+1

    if 6750<t<6800:
        with open('14out//14out'+str(t)+'.txt', 'w') as file:
            for j in range(height):
                file.write(''.join(pos[j]))
                file.write('\n')

print("Puzzle 2")
print(tframe)
