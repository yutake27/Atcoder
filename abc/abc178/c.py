n = int(input())

mod = pow(10, 9) + 7

ans = (pow(10, n, mod) - pow(9, n, mod) * 2 + pow(8, n, mod)) % mod
print(ans)