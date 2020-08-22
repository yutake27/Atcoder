n, m = map(int, input().split())
a_array = list(map(int, input().split()))

sum_a = sum(a_array)

if n - sum_a < 0:
    ans = -1
else:
    ans = n - sum_a

print(ans)