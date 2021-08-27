from collections import deque

n = int(input())
g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)


def dfs(n, g, start=1):
    visited = [-1] * (n + 1)
    stack = deque([])
    visited[start] = 0
    stack.append(start)
    while stack:
        node = stack.pop()
        score = visited[node]
        for adjacent_node in g[node]:
            if visited[adjacent_node] >= 0:
                continue
            stack.append(adjacent_node)
            visited[adjacent_node] = score + 1
    return visited


score_from_1 = dfs(n, g, start=1)
max_node = score_from_1.index(max(score_from_1))
score_from_max_node = dfs(n, g, start=max_node)
ans = max(score_from_max_node) + 1
print(ans)
