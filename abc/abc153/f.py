from collections import deque

n, d, a = map(int, input().split())
xh_list = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[0])
x_list, h_list = [list(i) for i in zip(*xh_list)]

queue = deque([])
ans = 0
total = 0
for i in range(n):
    while queue and queue[0][0] < x_list[i]:
        _, damage = queue.popleft()
        total -= damage

    h = h_list[i] - total
    if h > 0:
        num = (h - 1) // a + 1
        ans += num
        damage = a * num
        total += damage
        queue.append([x_list[i] + 2 * d, damage])

print(ans)