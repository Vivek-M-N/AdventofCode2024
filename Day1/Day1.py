#Day 1

nums = []
left = []
right = []
diff = []

with open(r'1.txt', 'r') as file:
        nums = file.read().split('\n')

for i in range(len(nums)):
        left = left + [int(nums[i].split('   ')[0])]
        right = right + [int(nums[i].split('   ')[1])]

left.sort()
right.sort()

for i in range(len(right)):
        diff.append(abs(left[i]-right[i]))

print("Part 1")
print(sum(diff))

sim_score = 0

for ele in set(left):
        sim_score += right.count(ele)*ele

print("Part 2")
print(sim_score)
