sx, sy, gx, gy = map(int, input().split())
gy = -gy

w = gx - sx
h = sy - gy
k = w / h
ans = k * sy + sx
print(ans)