#Day 6

'''
[1,0] - up
[0,-1] - right
[-1,0] - down
[0,1] - left
'''

def d(direction):
    if direction == [1,0]:
        return [0,-1]
    elif direction == [0,-1]:
        return [-1,0]
    elif direction == [-1,0]:
        return [0,1]
    else:
        return [1,0]

with open('6.txt', 'r') as file:
    content = file.read().split('\n')

for i in range(len(content)):
    line = content[i]
    try:
        j = line.index('^')
        break
    except ValueError:
        continue

initial = (i,j)
position = [i,j]
new_position = [i,j]
count = 1

direction = [1,0]
pos = []

while 0<=position[0]<len(content[1])-1 and 0<=position[1]<len(content[1])-1:
    if content[position[0]-direction[0]][position[1]-direction[1]] == '#':
        direction = d(direction)
        #print('collision')
    else:
        position[0] = position[0]-direction[0]
        position[1] = position[1]-direction[1]
        count+=1
        #print(position)
        pos.append(tuple(position))

unique_pos = set(pos)
print("Puzzle 1")
print(len(unique_pos))

position = list(initial)
pd = []
block = 0
soln = []

ite = 0

for potential in list(unique_pos):
    if potential == list(initial):
        pass
    else:
        ite+=1
        print(ite)
        #print(potential)
        position = list(initial)
        pd = []
        direction = [1,0]
        #print(position)
        while 0<=position[0]<len(content[1])-1 and 0<=position[1]<len(content[1])-1:
            #print(pd)
            if content[position[0]-direction[0]][position[1]-direction[1]] == '#' or [position[0]-direction[0], position[1]-direction[1]] == list(potential):
                direction = d(direction)
                #print('collision')
            else:
                position[0] = position[0]-direction[0]
                position[1] = position[1]-direction[1]
                #print(position)
                if (position, direction) in pd:
                    #print('repeat')
                    #print((position, direction))
                    block+=1
                    soln.append(list(potential))
                    #print(pd)
                    #print('^ works\n')
                    break
                else:
                    pd.append(([position[0]+direction[0],position[1]+direction[1]], direction))
                
print("Puzzle 2")
print(block)
    
    
