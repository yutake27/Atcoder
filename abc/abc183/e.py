h, w = map(int, input().split())
s_array = [list(input()) for _ in range(h)]

mod = pow(10, 9) + 7

dp = [[0] * w for _ in range(h)]
x_sum = [[0] * w for _ in range(h)]
y_sum = [[0] * w for _ in range(h)]
z_sum = [[0] * w for _ in range(h)]

dp[0][0] = 1

for i in range(h):
    for j in range(w):
        if s_array[i][j] == '#':
            continue
        if i != h - 1 and s_array[i + 1][j] == '.':
            x_sum[i + 1][j] = (dp[i][j] + x_sum[i][j]) % mod
            dp[i + 1][j] += x_sum[i + 1][j]
        if j != w - 1 and s_array[i][j + 1] == '.':
            y_sum[i][j + 1] = (dp[i][j] + y_sum[i][j]) % mod
            dp[i][j + 1] += y_sum[i][j + 1]
        if i != h - 1 and j != w - 1 and s_array[i + 1][j + 1] == '.':
            z_sum[i + 1][j + 1] = (dp[i][j] + z_sum[i][j]) % mod
            dp[i + 1][j + 1] += z_sum[i + 1][j + 1]

ans = dp[h - 1][w - 1] % mod
print(ans)