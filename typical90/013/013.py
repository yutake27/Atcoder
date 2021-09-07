import heapq

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))


def dijkstra(G, start, goal):
    hq = [(0, start)]
    seen = [False] * len(G)
    dist = [float('inf')] * len(G)
    dist[start] = 0
    while hq:
        cost, node = heapq.heappop(hq)
        if seen[node]:
            continue
        seen[node] = True
        for adj_node, adj_cost in G[node]:
            if seen[adj_node] is False and cost + adj_cost < dist[adj_node]:
                dist[adj_node] = cost + adj_cost
                heapq.heappush(hq, (dist[adj_node], adj_node))
    return dist


forth = dijkstra(g, 1, n)
back = dijkstra(g, n, 1)

for i in range(n):
    print(forth[i + 1] + back[i + 1])
