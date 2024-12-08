#Day 8

im = 0+1j
locs = {}

'''
Imaginary axis used to solve

----> +x
|
|
v y
'''

##read input and store input as a dictionary with complex keys as location
with open('8.txt', 'r') as file:
    content = file.read().split('\n')
    height = len(content)
    width = len(content[0])
    for y in range(height):
        for x in range(width):
            locs[(x)+(y)*im] = content[y][x]

'''
for y in range(height):
    for x in range(width):
        print(locs[x+y*im],end='')
    print('\n')

'''

freq = set()

##find unique frequencies
for key in locs.keys():
    if locs[key] != '.':
        freq.add(locs[key])

print(freq)

flocs = {}

##find location of each frequency
for f in freq:
    flocs[f] = []
    for key in locs.keys():
        if locs[key] == f:
            flocs[f] = flocs[f] + [key]

#print(flocs)

all_anodes = []

##find all locations of the first resonant antinode
for f in freq:
    for floc in flocs[f]:
        for check in flocs[f]:
            if check == floc:
                pass
            else:
                ##first antinode is found using vector addition
                all_anodes.append(2*floc-check)

#print(all_anodes)

anodes = set()

##find possible locations for first antinode
for anode in all_anodes:
    if 0<=anode.real<=width-1 and 0<=anode.imag<=height-1:
        anodes.add(anode)

print('Puzzle 1')
print(len(anodes))

res_anodes = []

##find all locations of all resonant antinodes
##number of possible locations is max(width,height)
for f in freq:
    for floc in flocs[f]:
        for check in flocs[f]:
            if check == floc:
                pass
            else:
                ##locations are found using direction vector between pair
                d = floc-check
                res_anodes+=[floc+i*d for i in range(max(height,width))]

anodes = set()

##find possible locations for all antinodes
for anode in res_anodes:
    if 0<=anode.real<=width-1 and 0<=anode.imag<=height-1:
        anodes.add(anode)

print('Puzzle 2')
print(len(anodes))
