data = [
    ['T1', ['Milk', 'Bread', 'Eggs']],
    ['T2', ['Bread', 'Butter']],
    ['T3', ['Bread', 'Cheese']],
    ['T4', ['Milk', 'Bread', 'Butter']],
    ['T5', ['Milk', 'Cheese']],
    ['T6', ['Bread', 'Cheese']],
    ['T7', ['Milk', 'Cheese']],
    ['T8', ['Milk', 'Bread', 'Cheese', 'Eggs']],
    ['T9', ['Milk', 'Bread', 'Cheese']]
]


init = []
for i in data:
    for q in i[1]:
        if(q not in init):
            init.append(q)
init = sorted(init)

sp = 0.8
s = int(sp*len(init))
print("Support:", s)

from collections import Counter

c = Counter()
for i in init:
    for d in data:
        if(i in d[1]):
            c[i]+=1
print("C1:")
for i in c:
    print(str([i])+": "+str(c[i]))
print()
l = Counter()
for i in c:
    if(c[i] >= s):
        l[frozenset([i])]+=c[i]
print("L1:")
for i in l:
    print(str(list(i))+": "+str(l[i]))
print()
pl = l
pos = 1
for count in range (2,1000):
    nc = set()
    temp = list(l)
    for i in range(0,len(temp)):
        for j in range(i+1,len(temp)):
            t = temp[i].union(temp[j])
            if(len(t) == count):
                nc.add(temp[i].union(temp[j]))
    nc = list(nc)
    c = Counter()
    for i in nc:
        c[i] = 0
        for q in data:
            temp = set(q[1])
            if(i.issubset(temp)):
                c[i]+=1
    print("C"+str(count)+":")
    for i in c:
        print(str(list(i))+": "+str(c[i]))
    print()
    l = Counter()
    for i in c:
        if(c[i] >= s):
            l[i]+=c[i]
    print("L"+str(count)+":")
    for i in l:
        print(str(list(i))+": "+str(l[i]))
    print()
    if(len(l) == 0):
        break
    pl = l
    pos = count
print("Result: ")
print("L"+str(pos)+":")
for i in pl:
    print(str(list(i))+": "+str(pl[i]))
print()

from itertools import combinations

# Prompt the user to input the minimum confidence percentage
min_confidence = float(input("Enter the minimum confidence percentage: "))

for l in pl:
    c = [frozenset(q) for q in combinations(l,len(l)-1)]
    mmax = 0
    for a in c:
        b = l-a
        ab = l
        sab = 0
        sa = 0
        sb = 0
        for q in data:
            temp = set(q[1])
            if a.issubset(temp):
                sa += 1
            if b.issubset(temp):
                sb += 1
            if ab.issubset(temp):
                sab += 1

        # No need to calculate confidence percentage here

        # Compare confidence with minimum confidence input by the user
        confidence_a = round(sab / sa * 100,2)
        if confidence_a >= min_confidence:
            print(str(list(a)) + " -> " + str(list(b)) + " = " + str(confidence_a) + "%")

        confidence_b = round(sab / sb * 100,2)
        if confidence_b >= min_confidence:
            print(str(list(b)) + " -> " + str(list(a)) + " = " + str(confidence_b) + "%")

    # curr = 1
    # print("choosing:", end=' ')
    # for a in c:
    #     b = l - a
    #     ab = l
    #     sab = 0
    #     sa = 0
    #     sb = 0
    #     for q in data:
    #         temp = set(q[1])
    #         if a.issubset(temp):
    #             sa += 1
    #         if b.issubset(temp):
    #             sb += 1
    #         if ab.issubset(temp):
    #             sab += 1

    #     # No need to calculate confidence percentage here

    #     confidence_a = sab / sa * 100
    #     if confidence_a >= min_confidence:
    #         print(curr, end=' ')
    #     curr += 1

    #     confidence_b = sab / sb * 100
    #     if confidence_b >= min_confidence:
    #         print(curr, end=' ')
    #     curr += 1

    print()
    print()
