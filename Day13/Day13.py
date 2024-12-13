#Day 13

import re
import numpy as np

with open('13.txt','r') as file:
    content = file.read().split('\n\n')

machines = []
for line in content:
    data = line.split('\n')
    A = re.findall('\d+',data[0])
    B = re.findall('\d+',data[1])
    L = re.findall('\d+',data[2])
    machines.append((A,B,L))
    
#print(machines)

solns = {}
mid = 1

for machine in machines:
    solns[mid] = ()
    ax = int(machine[0][0])
    ay = int(machine[0][1])
    bx = int(machine[1][0])
    by = int(machine[1][1])
    lx = int(machine[2][0])
    ly = int(machine[2][1])
    alim = min((lx//ax+1),(ly//ay+1),100)
    blim = min((lx//bx+1),(ly//by+1),100)
    #print(alim)
    #print(blim)
    for i in range(0,alim): #Button A
        x0 = ax*i
        y0 = ay*i
        for j in range(0,blim):
            x = x0 + bx*j
            y = y0 + by*j
            if x == lx and y == ly:
                solns[mid] += (i,j,3*i+j)
                break
    mid+=1
    
print(solns)

tokens = 0
for mid in solns.keys():
    try:
        tokens+=solns[mid][2]
    except IndexError:
        continue

print("Puzzle 1")
print(tokens)
    
solns = {}
mid = 1

for machine in machines:
    solns[mid] = ()
    ax = int(machine[0][0])
    ay = int(machine[0][1])
    bx = int(machine[1][0])
    by = int(machine[1][1])
    lx = int(machine[2][0])+10000000000000
    ly = int(machine[2][1])+10000000000000
    coeff = np.array([[ax, bx],[ay, by]])
    l = np.array([lx, ly]).reshape((2, 1))
    coeff_inv = np.linalg.inv(coeff)
    sol = coeff_inv @ l

    if (round(float(sol[0]))*ax + round(float(sol[1]))*bx == lx) and (round(float(sol[0]))*ay + round(float(sol[1]))*by == ly):
        solns[mid] += (sol[0],sol[1],3*sol[0]+sol[1])
    #print(sol)
    mid+=1
    
#print(solns)

tokens = 0
for mid in solns.keys():
    try:
        tokens+=solns[mid][2]
    except IndexError:
        continue

print("Puzzle 2")
print(round(float(tokens)))
