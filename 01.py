import os
from collections import defaultdict


n1, n2 = [], []
n2dict = defaultdict(int) 
with open("01.input", 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        parts = line.split("   ")
        n1.append(int(parts[0]))
        n2.append(int(parts[1]))
        n2dict[int(parts[1])]+=1


n1,n2 = sorted(n1), sorted(n2)
d, d2 = 0, 0
for j, i in zip(n1, n2):
    d+=abs(j-i)
    d2+=j*n2dict.get(j,0) 
print(d)
print(d2)