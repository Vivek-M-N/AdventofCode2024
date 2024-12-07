#Day 7

import math

def calc(op,num):
    ##Decide which operation
    if op == '0':
        return '+'
    elif op == '1':
        return '*'
    elif op == '2':
        return '*10**'+str(len(num))+'+'

def ter(n):
    ##decimal to ternary
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

with open('7.txt', 'r') as file:
    content = file.read().split('\n')

cal = 0

for eqn in content:
    #print(eqn)
    eqn = eqn.split(r':')
    res = int(eqn[0].strip()); nums = eqn[1].strip().split(' ')
    nops = len(nums)-1 ##number of operations between numbers
    #bnops = bin(nops).strip('0b')
    lops = [] ##full list of possivle operations in binary
    for i in range(0,2**nops):
        #print(i)
        form = '0' + str(nops) + 'b'
        bop = format(i, form)
        lops.append(str(bop))

    for op in lops:
        eqn_str = nums[0]
        ##forming equations to be evaluated
        for i in range(len(op)):
            eqn_str = '('+eqn_str+calc(op[i],nums[i])+nums[i+1]+')'
        #print(eqn_str)
        if eval(eqn_str) == res:
            #print(res)
            cal+=res
            break

print("Puzzle 1")
print(cal)

cal = 0

for eqn in content:
    #print(eqn)
    eqn = eqn.split(r':')
    res = int(eqn[0].strip()); nums = eqn[1].strip().split(' ')
    nops = len(nums)-1 ##number of operations between numbers
    lops = [] ##full list of possible operations in ternary
    for i in range(0,3**nops):
        #print(i)
        top = ter(i)
        top = '0'*(nops-len(top)) + top
        #print(top)
        lops.append(str(top))

    for op in lops:
        eqn_str = nums[0]
        ##forming equations to be evaluated
        for i in range(len(op)):
            eqn_str = '('+eqn_str+calc(op[i],nums[i+1])+nums[i+1]+')'
        #print(eqn_str)
        if eval(eqn_str) == res:
            #print(res)
            cal+=res
            break

print("Puzzle 2")
print(cal)
