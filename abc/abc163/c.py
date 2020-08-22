import collections

n = int(input())
a_array = list(map(int, input().split()))

c = collections.Counter(a_array)

for i in range(n):
    if i + 1 in c:
        print(c[i + 1])
    else:
        print(0)