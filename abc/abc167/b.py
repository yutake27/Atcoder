a, b, c, k = map(int, input().split())


sum = 0
rest_k = k

if rest_k <= a:
    sum += rest_k
    rest_k = 0
else:
    sum += a
    rest_k -= a

if rest_k <= b:
    rest_k = 0
else:
    rest_k -= b

sum -= rest_k

print(sum)