n, k = map(int, input().split())

d = n // k
ans = min(abs(n - k * d), abs(n - k * (d + 1)))

print(ans)