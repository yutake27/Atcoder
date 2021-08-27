n = int(input())
s = input()
obj = 'atcoder'
obj_dic = {si: i for i, si in enumerate(obj)}
mod = pow(10, 9) + 7

dp = [[0] * len(obj) for _ in range(n)]

for i in range(n):
    si = s[i]
    si_index = obj_dic[si] if si in obj_dic else 7
    for j in range(len(obj)):
        if j == si_index:
            if i == 0:
                if si == 'a':
                    dp[i][si_index] = 1
            else:
                if si == 'a':
                    dp[i][si_index] = 1 + dp[i - 1][si_index]
                elif dp[i][si_index - 1] > 0:
                    dp[i][si_index] = (dp[i - 1][si_index] + dp[i][si_index - 1]) % mod
        else:
            if i != 0:
                dp[i][j] = dp[i - 1][j]

ans = dp[n - 1][len(obj) - 1]
print(ans)
