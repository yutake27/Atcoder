N, M = map(int, input().split())
gcp = [list(input()) for _ in range(2 * N)]


w = 1
a = 0
l = -1


def judge(at, bt):
    if at == 'G':
        if bt == 'C':
            return w
        elif bt == 'G':
            return a
        else:
            return l
    elif at == 'C':
        if bt == 'G':
            return l
        elif bt == 'C':
            return a
        else:
            return w
    elif at == 'P':
        if bt == 'G':
            return w
        elif bt == 'C':
            return l
        else:
            return a
    assert False


rank = [(0, i + 1) for i in range(2 * N)]
for i in range(M):
    rate = []
    for k in range(N):
        ak = 2 * k
        aw, ai = rank[ak]
        bk = 2 * k + 1
        bw, bi = rank[bk]
        at = gcp[ai - 1][i]
        bt = gcp[bi - 1][i]
        j = judge(at, bt)
        aw = aw - 1 if j == 1 else aw
        bw = bw - 1 if j == -1 else bw
        rate.append((aw, ai))
        rate.append((bw, bi))
    rank = sorted(rate)

for i in range(2 * N):
    print(rank[i][1])
