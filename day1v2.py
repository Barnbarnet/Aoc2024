list1 = []
list2 = []

with open("day1_input.txt") as f:

    for line in f:
        t = line.split("   ")
        list1.append(int(t[0]))
        list2.append(int(t[1]))       
list1.sort()
list2.sort()

d = 0 

for l in list1:
    d = d + list2.count(l)*l
    #print("d is %s" % d)

print(d)