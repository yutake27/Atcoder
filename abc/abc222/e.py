from collections import deque

n, m, k = map(int, input().split())
A = list(map(int, input().split()))
g = [[] for _ in range(n + 1)]
e = []  # 辺のリストを保存
for i in range(n - 1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
    edge = (u, v) if u < v else (v, u)
    e.append(edge)
mod = 998244353


def dfs(start, goal):  # dfsで通過する辺をメモしておく
    q = deque([(start, [])])
    seen = [False] * len(g)
    while q:
        node, edges = q.popleft()
        seen[node] = True
        if node == goal:
            return edges
        for adj in g[node]:
            if seen[adj] is False:
                new_edge = (node, adj) if node < adj else (adj, node)
                q.append((adj, edges + [new_edge]))


# 各辺を通る回数を求める．
edge_counts = {edge: 0 for edge in e}  # 各辺を通る回数
edge_sum = 0  # 辺を通る回数の合計
for i in range(m - 1):
    start, goal = A[i], A[i + 1]
    edges = dfs(start, goal)
    for edge in edges:
        edge_counts[edge] += 1
        edge_sum += 1

if (edge_sum + k) % 2 != 0 or (edge_sum + k) < 0:  # Rの回数が整数にならない場合は条件を満たさない
    print(0)
    exit()

R = (edge_sum + k) // 2  # 赤辺を通る回数の合計
# DPで赤辺を通る回数の合計がRとなるような方法が何通りあるか数える
dp = [[0] * (R + 1) for _ in range(n)]  # dp[辺をみた数][赤辺の合計] = 通り数
dp[0][0] = 1
for i in range(n - 1):
    for j in range(R + 1):
        dp[i + 1][j] = dp[i][j]
    edge = e[i]
    edge_count = edge_counts[edge]
    for j in range(R + 1 - edge_count):
        dp[i + 1][j + edge_count] = (dp[i + 1][j + edge_count] + dp[i][j]) % mod

print(dp[n - 1][R])
