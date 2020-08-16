x, k, d = map(int, input().split())
x = abs(x)

need, mod = divmod(x, d)
if k <= need:
    ans = x - k*d
else:
    amari = k - need
    if amari % 2 == 0:
        ans = mod
    else:
        ans = mod - d


print(abs(ans))