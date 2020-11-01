n, k = map(int, input().split())

def solve(n, k):
    return min(k - 1, 2 * n + 1 - k)

k = abs(k)
ans = 0
for i in range(k + 2, n + n + 1):
    ans += solve(n, i) * solve(n, i - k)

print(ans)