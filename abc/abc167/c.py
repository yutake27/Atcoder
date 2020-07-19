N, M, X = map(int, input().split())
CA = [list(map(int, input().split())) for _ in range(N)]

ans = float('inf')
for i in range(pow(2, N)):
    cost = 0
    x_array = [0]*M
    for j in range(N):
        if (i>>j & 1) == 1:
            cost += CA[j][0]
            for m in range(M):
                x_array[m] += CA[j][m+1]
    flag = True
    for m in range(M):
        if x_array[m] < X:
            flag = False
            break
    if flag:
        ans = min(ans, cost)

if ans == float('inf'):
    print(-1)
else:
    print(ans)