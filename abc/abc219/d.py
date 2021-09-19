n = int(input())
x, y = map(int, input().split())
ab_list = [list(map(int, input().split())) for _ in range(n)]

# dp[見た弁当の数][たこ焼きの数][たい焼きの数] = 選んだ弁当数
dp = [[[float('inf')] * (y + 1) for _ in range(x + 1)] for _ in range(n + 1)]
dp[0][0][0] = 0

for i in range(n):
    a, b = ab_list[i - 1]
    for j in range(x + 1):
        for k in range(y + 1):
            # 貰うDP
            dp[i + 1][j][k] = min(dp[i][max(j - a, 0)][max(k - b, 0)] + 1, dp[i][j][k])

ans = dp[n][x][y]
ans = ans if ans != float('inf') else -1
print(ans)
