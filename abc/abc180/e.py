n = int(input())
xyz_list = [list(map(int, input().split())) for _ in range(n)]

dist = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(i, n):
        a, b, c = xyz_list[i]
        p, q, r = xyz_list[j]
        dist[i][j] = abs(p - a) + abs(q - b) + max(0, r - c)
        dist[j][i] = abs(p - a) + abs(q - b) + max(0, c - r)

INF = float('inf')
# dp[1 << n][n] [1 << n]は通った都市の集合を表し， [n]は最後に通った都市を表す
dp = [[INF] * n for _ in range(1 << n)]
# 開始地点0のみ初期値0にする
dp[1][0] = 0

# 全ての通った都市の集合に対して
for i in range(1 << n):
    # 全ての最後に通った都市の集合に対して
    for j in range(n):
        # 通ってなかったらcontinue
        if dp[i][j] == INF: continue
        # 各bitに対して
        for k in range(n):
            # 既に通っていたらcontinue
            if i >> k & 1 == 1: continue
            # それ以外のまだ通っていない都市に対して配るdp
            nexti = i | 1 << k
            nextd = dp[i][j] + dist[j][k]
            dp[nexti][k] = min(dp[nexti][k], nextd)

# 全ての都市を通った場合
all = (1 << n) - 1
ans = INF
# 全ての最後に通った都市に対して
for i in range(n):
    if dp[all][i] == INF: continue
    # 全ての都市を周るコストと最後に開始地点0に戻ってくるコストを足す
    tmp = dp[all][i] + dist[i][0]
    ans = min(ans, tmp)

print(ans)