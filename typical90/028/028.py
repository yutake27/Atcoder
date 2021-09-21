N = int(input())
size = 1000 + 1
mat = [[0] * size for _ in range(size)]

for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())
    mat[lx][ly] += 1
    mat[rx][ly] += -1
    mat[lx][ry] += -1
    mat[rx][ry] += 1

ans = [0] * (N + 1)
for x in range(size):
    for y in range(1, size):
        mat[x][y] += mat[x][y - 1]

for y in range(size):
    for x in range(1, size):
        mat[x][y] += mat[x - 1][y]

for x in range(size):
    for y in range(size):
        ans[mat[x][y]] += 1

print(*ans[1:], sep='\n')
