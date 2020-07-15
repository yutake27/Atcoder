s = input()
c = [1 for i in range(len(s))]
c_before = [-1]*len(c)

for j in range(len(s)):
    c_new = [0]*len(c)
    for i in range(len(s)):
        if s[i] == 'L':
            c_new[i-1] += c[i]
        elif s[i] == 'R':
            c_new[i+1] += c[i]
    if c_new == c:
        break
    if c_new == c_before:
        if j%2 != 0:
            c = c_new
        break
    c_before = c
    c = c_new
from functools import reduce
print(reduce(lambda a, b:str(a)+' '+str(b), c))