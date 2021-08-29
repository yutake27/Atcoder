# not AC code
h, w = map(int, input().split())
Q = int(input())
mat = [[0] * (w + 2) for _ in range(h + 2)]
mem = [[[[0] * (w + 1) for _ in range(h + 1)] for _ in range(w + 1)] for _ in range(h + 1)]


def bfs(ra, ca, rb, cb):
    if mat[ra][ca] == 0 or mat[rb][cb] == 0:
        return 0
    if mem[ra][ca][rb][cb]:  # キャッシュを確認
        return 1
    elif (ra == rb and ca == cb):  # ゴールだったら
        return 1
    for x, y in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
        mem[ra][ca][rb][cb] = bfs(ra + x, ca + y, rb, cb)
        if mem[ra][ca][rb][cb] == 1:
            return bfs(ra + x, ca + y, rb, cb)
    return 0


for i in range(Q):
    q = list(map(int, input().split()))
    print(q)
    if q[0] == 1:
        mat[q[1]][q[2]] = 1
    elif q[0] == 2:
        _, ra, ca, rb, cb = q
        ans = bfs(ra, ca, rb, cb)
        print('Yes' if ans else 'No')
