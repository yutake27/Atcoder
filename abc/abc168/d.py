from collections import deque

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

neighbor_list = [[] for _ in range(N+1)]
for ab in AB:
    neighbor_list[ab[0]].append(ab[1])
    neighbor_list[ab[1]].append(ab[0])


parent_array = [-1]*(N+1)
parent_array[1] = 0
d = deque([1])
while len(d)!=0:
    v = d.popleft()
    for ch in neighbor_list[v]:
        if parent_array[ch] == -1:
            parent_array[ch] = v
            d.append(ch)

print('Yes')
for i in parent_array[2:]:
    print(i)

