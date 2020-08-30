from collections import deque

n, m = map(int, input().split())
ab_array = [list(map(int, input().split())) for _ in range(m)]

ad_sum_array = [0] * n
ad_array = [set() for _ in range(n)]

for ab in ab_array:
    a, b = ab
    ad_array[a - 1].add(b - 1)
    ad_array[b - 1].add(a - 1)

check_array = [False] * n

def bfs(node_num):
    queue = deque([node_num])
    check_array[node_num] = True
    num = 1

    while queue:
        node = queue.popleft()
        for ad in ad_array[node]:
            if not check_array[ad]:
                check_array[ad] = True
                queue.append(ad)
                num += 1
    return num

ans = 0
for i in range(n):
    if not check_array[i]:
        ans = max(ans, bfs(i))

print(ans)