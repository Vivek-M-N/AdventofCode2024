#Day 2

def safety(report):
    #print(report)
    if report == sorted(report) or report == sorted(report, reverse=True):
        diff = [abs(report[i]-report[i+1]) for i in range(len(report)-1)]
        if set(diff).issubset(set([1,2,3])):
            return True
        else:
            return False
    else:
        return False

count = 0
safe_list = []

with open(r'2.txt', 'r') as file:
    content = file.read().split('\n')

for i in range(len(content)):
    report = list(map(int, content[i].split(' ')))
    if safety(report):
        count+=1
        safe_list.append(i)
    else:
        pass
            
print("Puzzle 1")
print(count)

damped_count = 0

for i in range(len(content)):
    if not i in safe_list:
        report = list(map(int, content[i].split(' ')))
        for j in range(len(report)):
            if safety([report[k] for k in range(len(report)) if k!=j]):
                damped_count+=1
                break
        
print("Puzzle 2")
print(damped_count+count) 
    
    
