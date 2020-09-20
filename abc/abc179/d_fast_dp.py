# 累積和を用いたdpの高速か

n, k = map(int, input().split())
mod = 998244353

lr_list = [list(map(int, input().split())) for _ in range(k)]

dp = [0] * (n + 1)
dp[1] = 1
sdp = [0] * (n + 1)
sdp[1] = 1
for i in range(2, n + 1):
    for j in range(k):
        right = max(0, i - lr_list[j][0])
        left = max(0, i - lr_list[j][1] - 1)
        dp[i] = (dp[i] + sdp[right] - sdp[left]) % mod
    sdp[i] = sdp[i - 1] + dp[i]

print(dp[n])