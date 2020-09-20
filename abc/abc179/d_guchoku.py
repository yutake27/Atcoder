n, k = map(int, input().split())
mod = 998244353

s_list = []
for _ in range(k):
    l, r = map(int, input().split())
    s_list += list(range(l, r + 1))
S = set(sorted(s_list))

ans_array = [0] * (n + 1)
ans_array[1] = 1
for i in range(1, n):
    for d in S:
        if d + i > n:
            break
        ans_array[d + i] = (ans_array[d + i] + ans_array[i]) % mod


print(ans_array[n])