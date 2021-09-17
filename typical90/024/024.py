_, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

diff_sum = sum([abs(a - b) for a, b in zip(A, B)])

if diff_sum <= k and (k - diff_sum) % 2 == 0:
    print('Yes')
else:
    print('No')
