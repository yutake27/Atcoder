import heapq
n, w = map(int, input().split())
stp_list = sorted([list(map(int, input().split())) for _ in range(n)])

ans = True
sum_p = 0
h_list = []
for s, t, p in stp_list:
    while len(h_list) != 0 and h_list[0][0] <= s:
        bt, bp = heapq.heappop(h_list)
        sum_p -= bp
    sum_p += p
    heapq.heappush(h_list, [t, p])
    if sum_p > w:
        ans = False
        break

print('Yes' if ans else 'No')