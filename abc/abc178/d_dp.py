# 動的計画法による解法

s = int(input())
mod = pow(10, 9) + 7

A = [0] * (s + 1)

if s >= 3:
    A[3] = 1

for i in range(4, s + 1):
    A[i] = (A[i - 3] + A[i - 1]) % mod

print(A[s])