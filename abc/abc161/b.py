n, m = map(int, input().split())
a = list(map(int, input().split()))

a_sort = sorted(a, reverse=True)
a_sum = sum(a)

if a_sort[m - 1] < a_sum / (4 * m):
    print('No')
else:
    print('Yes')