N = int(input())
xy = []
xy_set = set()

for _ in range(N):
    x, y = map(int, input().split())
    xy.append((x, y))
    xy_set.add((x, y))

cnt = 0
for i in range(N):
    xi, yi = xy[i]
    for j in range(i, N):
        xj, yj = xy[j]
        if xi == xj or yi == yj:
            continue
        if (xi, yj) in xy_set and (xj, yi) in xy_set:
            cnt += 1

ans = cnt // 2
print(ans)
