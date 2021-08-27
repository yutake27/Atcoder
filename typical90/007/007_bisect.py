import bisect

n = int(input())
a = list(map(int, input().split()))
a.append(float('inf'))
a.append(-float('inf'))
a.sort()
q = int(input())
for _ in range(q):
    b = int(input())
    i = bisect.bisect(a, b)
    print(min(b - a[i - 1], a[i] - b))
