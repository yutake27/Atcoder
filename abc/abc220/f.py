from collections import deque

N = int(input())
g = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    g[u - 1].append(v - 1)
    g[v - 1].append(u - 1)


def dfs():
    q = deque([(0, 0)])
    sum_dist = 0
    visited = [False] * N
    sub_size = [0] * N
    while q:
        # stackで帰りがけを記録するためにpopせずに右端を見る
        node, dist = q[-1]
        visited[node] = True
        num_not_visited_adj = 0  # 未訪問の隣接ノード数を記録
        for adj in g[node]:
            if not visited[adj]:
                num_not_visited_adj += 1
                q.append((adj, dist + 1))
        # 未訪問の隣接ノードがなかったら帰りがけの処理を行う
        if num_not_visited_adj == 0:
            sum_dist += dist
            node, dist = q.pop()
            # 部分木のサイズは子ノードの部分木の和
            # (親ノードの部分木のサイズは未決定(0)なので足して問題ない)
            sub_size[node] = 1
            for adj in g[node]:
                sub_size[node] += sub_size[adj]
    return sum_dist, sub_size


sum_dist, sub_size = dfs()
print(sub_size)


def dfs2():  # dfsでノード0から順に隣接ノードの答えを埋めていく
    q = deque([0])
    ans = [0] * N
    ans[0] = sum_dist
    visited = [False] * N
    while q:
        node = q.pop()
        visited[node] = True
        for adj in g[node]:
            if not visited[adj]:
                q.append(adj)
                # 隣接ノードの部分木のサイズから距離の合計が求まる
                ans[adj] = ans[node] + N - 2 * sub_size[adj]
    return ans


ans = dfs2()
print(*ans, sep='\n')
