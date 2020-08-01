n, k = map(int, input().split())
A = list(map(int, input().split()))

k_sum = sum(A[:k])

for i in range(k, n):
    k_sum_next = k_sum - A[i-k] + A[i]
    if k_sum < k_sum_next:
        print('Yes')
    else:
        print('No')
    k_sum = k_sum_next
