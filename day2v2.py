def analyze_report(report:list):

    d_list = []
    for i in range(1,len(report)):
        d = report[i]-report[i-1]
        d_list.append(d)
# + 
    if (d_list.count(0) > 1)  or (sum(abs(i) > 3 for i in d_list[1:-1]) > 0) :
        return 0
    p1 = abs(d_list[1]) > 3
    p2 = abs(d_list[-1]) > 3 
    p3 = (d_list.count(0) ==1)
    if (p1 and p2) or (p2 and p3) or (p1 and p3):
        return 0
    
    cd = sum(i > 0 for i in d_list)
    n = len(d_list)
    if cd in (0, 1, n-1, n):
        return 1
    else:
        return 0 
    
count = 0 

with open("day2_input.txt") as f:

    for line in f:
        t = []
        for l in line.split(" "):
            t.append(int(l)) 
        if analyze_report(t) == 1:
            print(t)
        count = count + analyze_report(t)

print(count)