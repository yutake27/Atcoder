t = int(input())

mod = 1000000007

def solve(n, a, b):
    if n - a - b >= 0:
        x3 = (n - a - b + 2) * (n - a - b + 1)
    else:
        x3 = 0
    x2 = (n - a + 1) * (n - b + 1) - x3
    x1 = pow(x2, 2)
    ans = (pow(n - a + 1, 2) * pow(n - b + 1, 2) - x1) % mod
    return ans


for i in range(t):
    n, a, b = map(int, input().split())
    ans = solve(n, a, b)
    print(ans)