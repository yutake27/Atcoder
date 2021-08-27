h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]

h_sum = [0] * h
w_sum = [0] * w

for i in range(h):
    for j in range(w):
        h_sum[i] += A[i][j]
        w_sum[j] += A[i][j]

for i in range(h):
    for j in range(w):
        print(h_sum[i] + w_sum[j] - A[i][j], end=' ')
    print()
