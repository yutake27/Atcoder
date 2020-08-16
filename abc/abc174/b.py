n, d = map(int, input().split())
xy_array = [list(map(int, input().split())) for _ in range(n)]

ans = 0
d2 = d**2
for xy in xy_array:
    if xy[0]**2 + xy[1]**2 <= d2:
        ans += 1

print(ans)