n, a, b = map(int, input().split())

mod = pow(10, 9) + 7

comb_all = pow(2, n, mod) - 1

nca_numerator = 1
nca_denominator = 1
ncb_numerator = 1
ncb_denominator = 1

for i in range(1, a + 1):
    nca_numerator = (nca_numerator * i) % mod

for i in range(n - a + 1, n + 1):
    nca_denominator = (nca_denominator * i) % mod

for i in range(1, b + 1):
    ncb_numerator = (ncb_numerator * i) % mod

for i in range(n - b + 1, n + 1):
    ncb_denominator = (ncb_denominator * i) % mod

nca = nca_denominator * pow(nca_numerator, mod - 2, mod) % mod
ncb = ncb_denominator * pow(ncb_numerator, mod - 2, mod) % mod
ans = (comb_all - nca - ncb) % mod
print(ans)