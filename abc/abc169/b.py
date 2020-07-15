N = int(input())
A = list(map(int, input().split()))

mod = 10**18
ans = 1
for i in range(N):
    ans *= A[i]
    if ans > mod:
        if 0 in A:
            print(0)
        else:
            print(-1)
        exit()

print(ans)