#Day 5

def check_page_list(pl):
    check = True
    for i in range(1,len(pl)):
        cl = pl[0:i]
        for num in cl:
            try:
                if num in rd[pl[i]]:
                    check = False
                    break
            except KeyError:
                pass
        if check == False:
            break
    if check == True:
        return True
    

with open(r'5.txt', 'r') as file:
    content = file.read().split('*****\n')

rules = content[0].split('\n')[:-2]
page_lists = content[1].split('\n')

rd = {}
rl = []
check_page_old = 0
follow_page_old = 0

for rule in rules:
    [check_page, follow_page] = map(int,rule.split('|'))
    #print(check_page)
    #print(follow_page)
    try:
        old = rd[check_page]
        #print(type(old))
        rd[check_page] = old + [follow_page]
    except KeyError:
        rd[check_page] = [follow_page]
    #print(rd)

for key in rd.keys():
    rd[key] = sorted(rd[key])

center = 0
right_order = []

for j in range(len(page_lists)):
    pl = page_lists[j]
    pl = list(map(int,pl.split(',')))
    if check_page_list(pl):
        center += pl[int(len(pl)/2)]
        right_order.append(j)

print("Part 1")
print(center)

new_center = 0

for j in range(len(page_lists)):
    if j in right_order:
        continue
    else:
        pl = page_lists[j]
    pl = list(map(int,page_lists[j].split(',')))
    check = True
    for i in range(1,len(pl)):
        cl = pl[0:i]
        for k in range(len(cl)):
            num = cl[k]
            try:
                if num in rd[pl[i]]:
                    temp = num
                    pl[k] = pl[i]
                    pl[i] = temp
            except KeyError:
                pass
    
    if check_page_list(pl):
        #print(pl)
        new_center += pl[int(len(pl)/2)]

print("Part 2")
print(new_center)
