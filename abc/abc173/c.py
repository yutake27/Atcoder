import numpy as np
import itertools


def conv(l, n):
    a = [True]*n
    for i in l:
        a[i] = False
    return a

H, W, K = list(map(int, input().split()))
c = [input().split() for _  in range(H)]
c = np.array([list(c[i][0]) for i in range(H)])

path = 0
H_array = range(H)
W_array = range(W)
for n_i in range(H+1):
    for n_j in range(W):
        for comb_i in itertools.combinations(H_array, n_i):
            for comb_j in itertools.combinations(W_array, n_j):
                black = np.count_nonzero(c[conv(comb_i, H)][:, conv(comb_j, W)] == '#')
                if black == K:
                    path += 1

print(path)
