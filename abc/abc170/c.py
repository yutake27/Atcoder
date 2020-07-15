X, N = list(map(int, input().split()))
if N!=0:
    p = list(map(int, input().split()))
else:
    print(X)
    exit()

abs_diff = 1000
p = set(p)
for i in range(102):
    if not i in p:
        if abs(X-i)<abs_diff:
            ans = i
            abs_diff = abs(X-i)

print(ans)