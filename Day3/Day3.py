#Day 3

import re

with open(r'3.txt', 'r') as file:
    content = file.read()

#pattern = '''mul\([0-9]\,[0-9]\)|mul\([0-9]\,[0-9][0-9]\)|mul\([0-9]\,[0-9][0-9][0-9]\)|mul\([0-9][0-9]\,[0-9]\)|mul\([0-9][0-9]\,[0-9][0-9]\)|mul\([0-9][0-9]\,[0-9][0-9][0-9]\)|mul\([0-9][0-9][0-9]\,[0-9]\)|mul\([0-9][0-9][0-9]\,[0-9][0-9]\)|mul\([0-9][0-9][0-9]\,[0-9][0-9][0-9]\)'''
pattern1 = 'mul\(\d+\,\d+\)'

matches = re.findall(pattern1,content)

total = 0

for match in matches:
    [a, b] = map(int,match.strip('mul()').split(','))
    print
    total += a*b

print("Puzzle 1")
print(total)

pattern2 = "mul\(\d+\,\d+\)|don\'t|do"

matches = re.findall(pattern2,content)

new_total = 0
mult = 1

for match in matches:
    #print(match)
    if match != "don't" and match != "do":
        [a, b] = map(int,match.strip('mul()').split(','))
        new_total += a*b*mult
    else:
        if match == "don't":
            mult = 0
        elif match == 'do':
            mult = 1

print("Puzzle 2")
print(new_total)
