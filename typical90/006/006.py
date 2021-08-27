import heapq

n, k = map(int, input().split())
S = list(input())

hqueue = []
heapq.heapify(hqueue)
ans = ''
selected_index = -1
for i in range(n):
    heapq.heappush(hqueue, (S[i], i))
    if i >= n - k:
        while True:
            s, index = heapq.heappop(hqueue)
            if index > selected_index:
                ans += s
                selected_index = index
                break

print(ans)
