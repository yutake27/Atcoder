N = input()
K = int(input())

# dp[i][k]: (i+1)桁目見て0でない数がk個出ている時の場合の数
dp0 = [[0] * (K + 1) for _ in range(len(N) + 1)] # N以下が未確定
dp1 = [[0] * (K + 1) for _ in range(len(N) + 1)] # N以下が確定
dp0[0][0] = 1

for i, n in enumerate(N):
    for k in range(K + 1):
        if n == '0': # Nの(i + 1)桁目が0の時
            dp0[i + 1][k] += dp0[i][k]
            dp1[i + 1][k] += dp1[i][k]
            if k < K:
                dp1[i + 1][k + 1] += dp1[i][k] * 9
        else:
            if k < K:
                dp0[i + 1][k + 1] += dp0[i][k]
                dp1[i + 1][k + 1] += dp1[i][k] * 9 + dp0[i][k] * (int(n) - 1)
            dp1[i + 1][k] += dp0[i][k] + dp1[i][k]

ans = dp0[len(N)][K] + dp1[len(N)][K]
print(ans)