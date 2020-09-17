from math import factorial

s = int(input())
mod = pow(10, 9) + 7


def nCr(n, r):
    return int(factorial(n) // factorial(r) // factorial (n - r) % mod)

ans = 0
seq_len = s // 3

for i in range(1, seq_len + 1):
    ans += nCr(s - 3 * i + (i - 1), i - 1)

print(ans % mod)
