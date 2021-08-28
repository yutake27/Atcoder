n = int(input())
p_sum1 = [0] * (n + 1)
p_sum2 = [0] * (n + 1)

for i in range(n):
    c, p = map(int, input().split())
    if c == 1:
        p_sum1[i + 1] = p_sum1[i] + p
        p_sum2[i + 1] = p_sum2[i]
    else:
        p_sum1[i + 1] = p_sum1[i]
        p_sum2[i + 1] = p_sum2[i] + p

q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    a = p_sum1[r] - p_sum1[l - 1]
    b = p_sum2[r] - p_sum2[l - 1]
    print(a, b)
