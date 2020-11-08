h, n = map(int, input().split())
a_list = list(map(int, input().split()))

a_sum = sum(a_list)

if h <= a_sum:
    print('Yes')
else:
    print('No')