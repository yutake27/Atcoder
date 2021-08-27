n = int(input())
s = input()
t = 'atcoder'
idx = {t[i]: i + 1 for i in range(len(t))}
mod = pow(10, 9) + 7

dp = [[0] * (len(t) + 1) for i in range(n + 1)]
for i in range(n + 1):
    for j in range(len(t) + 1):
        if j == 0:
            dp[i][j] = 1

for i in range(1, n + 1):
    c = s[i - 1]
    for j in range(1, len(t) + 1):
        c_idx = idx[c] if c in idx else None
        if j == c_idx:
            if dp[i][c_idx - 1] > 0:
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % mod
        else:
            dp[i][j] = dp[i - 1][j]

ans = dp[n][len(t)]
print(ans)
