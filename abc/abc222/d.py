N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
mod = 998244353

s_dict = {i: 0 for i in range(-1, b[N - 1] + 1)}
for i in range(N):
    for j in range(a[i], b[N - 1] + 1):
        if i == 0:
            if j <= b[i]:
                s_dict[j] = (1 + s_dict[j - 1]) % mod
            else:
                s_dict[j] = s_dict[j - 1]
        else:
            if j == a[i]:
                s_dict[j] = (s_dict[j]) % mod
            elif j <= b[i]:
                s_dict[j] = (s_dict[j] + s_dict[j - 1]) % mod
            else:
                s_dict[j] = s_dict[j - 1]

print(s_dict[b[N - 1]])
