from collections import deque

n = int(input())
G = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)


def dfs(start):
    queue = deque([(start, True)])
    visited = [False] * (n + 1)
    a_half = []
    b_half = []
    while queue:
        node, b = queue.pop()
        visited[node] = True
        if b:
            a_half.append(node)
        else:
            b_half.append(node)
        for adj in G[node]:
            if not visited[adj]:
                queue.append((adj, not b))
    return a_half, b_half


a_half, b_half = dfs(1)
if len(a_half) >= n // 2:
    ans = a_half
else:
    ans = b_half
print(*ans[: n // 2], sep=' ')
