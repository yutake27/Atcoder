n = int(input())

A = list(range(2, n + 1))
p = []
while A[0]**2 <= n:
    tmp = A[0]
    p.append(tmp)
    A = [i for i in A if i%tmp != 0]
p = p + A

def get_fact(num):
    pattern = 1
    i = 0
    div = p[i]
    while div**2 <= num:
        div_cnt = 0
        while num % div == 0:
            div_cnt += 1
            num //= div
        if div_cnt != 0:
            pattern *= (div_cnt + 1)
        i += 1
        div = p[i]
    if num > 1:
        pattern *= 2
    if pattern == 1:
        if num != 1:
            pattern += 1
    return pattern

ans = 0
for c in range(1, n):
    ans += get_fact(n - c)
print(ans)



