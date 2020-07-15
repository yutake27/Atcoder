N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

conf_max = 0
for i in range(1, N):
    conf_max += A[i//2]

print(conf_max)