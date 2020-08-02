import math

a, b, n = map(int, input().split())

top = min(n, b-1)
ans = math.floor(a*top/b)
print(ans)