n = int(input())
a, b, c = sorted(list(map(int, input().split())))
max_cnt = 9999


cnt = float('inf')
for i in range(max_cnt + 1):
    ati = a * i
    for j in range(max_cnt + 1 - i):
        btj = b * j
        if ati + btj > n:
            break
        rem = n - ati - btj
        div, mod = divmod(rem, c)
        if mod == 0:
            cnt = min(cnt, i + j + div)


print(cnt)
