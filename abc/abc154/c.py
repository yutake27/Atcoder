n = int(input())
a_list = list(map(int, input().split()))
a_set = set(a_list)

if n == len(a_set):
    print('YES')
else:
    print('NO')