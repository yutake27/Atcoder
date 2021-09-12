# これは橋を見つけようとして書いたコードだがNot AC
n, m = map(int, input().split())
g = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    g[a - 1].append((b - 1, c))
    g[b - 1].append((a - 1, c))

cnt = 0
seen = [float('inf')] * n
lowlink = [float('inf')] * n
bridges = []


def dfs(node, parent, cnt):
    seen[node] = cnt
    lowlink[node] = seen[node]
    cnt += 1
    for v, c in g[node]:
        if seen[v] == float('inf'):
            dfs(v, node, cnt)
            lowlink[node] = min(lowlink[node], lowlink[v])
            if seen[node] < lowlink[v]:
                bridges.append((node, v, c))
            elif v != parent:
                lowlink[node] = min(lowlink[node], seen[v])


dfs(0, -1, 0)
ans = 0
for bridge in bridges:
    print(bridge)
    node, v, c = bridge
    if c > 0:
        ans += c

print(ans)
