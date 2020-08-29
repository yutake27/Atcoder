import collections
from functools import reduce

n = int(input())
S = input()

c = collections.Counter(list(S))
ans = c['R'] * c['G'] * c['B']

for i in range(n):
    for j in range(i + 1, n):
        if 2 * j - i <= n - 1 and S[i] != S[j] and S[j] != S[2 * j - i] and S[2 * j - i] != S[i]:
            ans -= 1

print(ans)