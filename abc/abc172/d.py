N = int(input())

ans = 0
for i in range(1,N+1):
    y = N/i
    ans += y*(y+1)*i/2

print(ans)

