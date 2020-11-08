h, n = map(int, input().split())
ab_list = [list(map(int, input().split())) for _ in range(n)]

dp = [float('inf')] * (h + 1)
dp[0] = 0

for i in range(h + 1):
    for a, b in ab_list:
        if i + a <= h:
            dp[i + a] = min(dp[i + a], dp[i] + b)
        else:
            dp[h] = min(dp[h], dp[i] + b)

print(dp[h])