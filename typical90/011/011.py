n = int(input())
dcs = [list(map(int, input().split())) for _ in range(n)]
dcs.sort()
d_max = dcs[-1][0]

dp = [[0] * (d_max + 1) for _ in range(n + 1)]

for i in range(n):
    d, c, s = dcs[i]
    for j in range(d):  # 完了している日数
        dp[i + 1][j] = max(dp[i][j], dp[i + 1][j])
        if j + c <= d:
            dp[i + 1][j + c] = max(dp[i][j] + s, dp[i + 1][j + c])

ans = max(list(map(lambda x: max(x), dp)))
print(ans)
