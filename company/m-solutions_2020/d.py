N = int(input())
A = list(map(int, input().split()))


m = 1000
k = 0

for i in range(N-1):
    if A[i] < A[i+1]:
        p = int(m//A[i])
        k += p
        m -= A[i]*p
    elif A[i] > A[i+1]:
        m += A[i]*k
        k = 0

m += A[N-1]*k
print(m)