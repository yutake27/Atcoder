import itertools

n, k = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for order in list(itertools.permutations([i for i in range(1, n)])):
    cost_sum = 0
    now = 0
    for i in list(order) + [0]:
        cost_sum += T[now][i]
        now = i
    if cost_sum == k:
        ans += 1

print(ans)