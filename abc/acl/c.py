from collections import deque

n, m = map(int, input().split())
ad_list = [[] for i in range(n)]
for _ in range(m):
    i, j = map(int, input().split())
    ad_list[i - 1].append(j - 1)
    ad_list[j - 1].append(i - 1)


def bfs(node, ad_list):
    visited = [-1] * node
    queue = deque()
    count = 0
    for i in range(node):
        if visited[i] == 0: continue
        queue.append(i)
        visited[i] = 0
        while queue:
            n = queue.popleft()
            for ad in ad_list[n]:
                if visited[ad] == -1:
                    visited[ad] = 0
                    queue.append(ad)
        count += 1
    return count

ans = bfs(n, ad_list) - 1
print(ans)
