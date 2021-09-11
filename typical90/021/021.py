import sys
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
g = [set() for _ in range(n + 1)]
g_reversed = [set() for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].add(b)
    g_reversed[b].add(a)

seen = [False] * (n + 1)
order = []


def dfs(node):
    seen[node] = True
    for adj in g[node]:
        if seen[adj] is False:
            dfs(adj)
    order.append(node)


for i in range(1, n + 1):
    if seen[i] is False:
        dfs(i)


rseen = [False] * (n + 1)


def rdfs(node) -> int:
    size = 0
    rseen[node] = True
    for adj in g_reversed[node]:
        if rseen[adj] is False:
            size += 1
            size += rdfs(adj)
    return size


ans = 0
for i in reversed(order):
    if rseen[i] is False:
        size = rdfs(i) + 1
        ans += size * (size - 1) // 2

print(ans)
