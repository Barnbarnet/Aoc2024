def analyze_report(report:list):

    d_list = []
    for i in range(1,len(report)):
        d = report[i]-report[i-1]
        if (d == 0) or (abs(d) > 3) :
            return 0 
        d_list.append(d)
    
    if all(x > 0 for x in d_list) or all(x < 0 for x in d_list):
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