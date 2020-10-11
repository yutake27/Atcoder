h, w = map(int, input().split())
s_list = [list(input()) for _ in range(h)]

mod = 1000000007

k = 0
for i in range(h):
    for j in range(w):
        if s_list[i][j] == '.':
            k += 1

thre = 2100
l = [[0] * thre for _ in range(thre)]
r = [[0] * thre for _ in range(thre)]
u = [[0] * thre for _ in range(thre)]
d = [[0] * thre for _ in range(thre)]


for i in range(h):
    tl = 0
    for j in range(w):
        if s_list[i][j] == '#': tl = 0
        else: tl += 1
        l[i][j] = tl

for i in range(h):
    tr = 0
    for j in range(w):
        if s_list[i][w - j - 1] == '#': tr = 0
        else: tr += 1
        r[i][w - j - 1] = tr

for j in range(w):
    td = 0
    for i in range(h):
        if s_list[i][j] == '#': td = 0
        else: td += 1
        d[i][j] = td

for j in range(w):
    tu = 0
    for i in range(h):
        if s_list[h - i - 1][j] == '#': tu = 0
        else: tu += 1
        u[h - i - 1][j] = tu

pow2_list = [0] * pow(thre, 2)
pow2_list[0] = 1
for i in range(1, pow(thre, 2)):
    pow2_list[i] = pow2_list[i - 1] * 2 % mod

ans = k * pow2_list[k]
for i in range(h):
    for j in range(w):
        if s_list[i][j] == '#': continue
        cnt = l[i][j] + r[i][j] + u[i][j] + d[i][j] - 3
        ans -= pow2_list[k - cnt]

ans %= mod
print(ans)