n = int(input())
A = list(map(int, input().split()))
dp = [[0] * 10 for _ in range(n)]
dp[0][A[0]] = 1
mod = 998244353

for i in range(1, n):
    for j in range(10):
        f = (j + A[i]) % 10
        g = (j * A[i]) % 10
        dp[i][f] = (dp[i][f] + dp[i - 1][j]) % mod
        dp[i][g] = (dp[i][g] + dp[i - 1][j]) % mod

for i in range(10):
    print(dp[n - 1][i])
