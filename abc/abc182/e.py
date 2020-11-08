h, w, n, m = map(int, input().split())

mat = [[0] * w for _ in range(h)]
for _ in range(n):
    a, b = map(int, input().split())
    mat[a - 1][b - 1] = 1

for _ in range(m):
    c, d = map(int, input().split())
    mat[c - 1][d - 1] = -1

ans_mat = [[0] * w for _ in range(h)]
for i in range(h):
    tl = 0
    for j in range(w):
        if mat[i][j] == 1:
            tl = 1
            ans_mat[i][j] = 1
        elif tl == 1 and mat[i][j] == 0:
            ans_mat[i][j] = 1
        elif mat[i][j] == -1:
            tl = 0

for i in range(h):
    tl = 0
    for j in range(w):
        if mat[i][w - j - 1] == 1:
            tl = 1
            ans_mat[i][w - j - 1] = 1
        elif tl == 1 and mat[i][w - j - 1] == 0:
            ans_mat[i][w - j - 1] = 1
        elif mat[i][w - j - 1] == -1:
            tl = 0

for j in range(w):
    tl = 0
    for i in range(h):
        if mat[i][j] == 1:
            tl = 1
            ans_mat[i][j] = 1
        elif tl == 1 and mat[i][j] == 0:
            ans_mat[i][j] = 1
        elif mat[i][j] == -1:
            tl = 0

for j in range(w):
    tl = 0
    for i in range(h):
        if mat[h - i - 1][j] == 1:
            tl = 1
            ans_mat[h - i - 1][j] = 1
        elif tl == 1 and mat[h - i - 1][j] == 0:
            ans_mat[h - i - 1][j] = 1
        elif mat[h - i - 1][j] == -1:
            tl = 0

ans = 0
for i in range(h):
    for j in range(w):
        if ans_mat[i][j] == 1:
            ans += 1

print(ans)
