n, k = map(int, input().split())

mod = pow(10, 9) + 7

a = list(range(n+1))

def cumulative_sum(array):
    ret = []
    for index, a in enumerate(array):
        if index != 0:
            ret.append(ret[-1] + a)
        else:
            ret.append(a)
    return ret

a_cumulative_sum = cumulative_sum(a)
a_rev_cumulative_sum = cumulative_sum(a[::-1])

ans = 0
for i in range(k, n + 2):
    ans += (a_rev_cumulative_sum[i - 1] - a_cumulative_sum[i - 1] + 1) % mod

ans %= mod
print(ans)