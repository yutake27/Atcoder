N, M, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_sum = [0]
B_sum = [0]
for i in range(N):
    A_sum.append(A_sum[i]+A[i])
for i in range(M):
    B_sum.append(B_sum[i]+B[i])

num = 0
J = M
for i in range(N+1):
    if A_sum[i] > K:
        break
    for j in reversed(range(J+1)):
        if A_sum[i] + B_sum[j] <= K:
            if num < i+j:
                num = i+j
            J = j
            break

print(num)
