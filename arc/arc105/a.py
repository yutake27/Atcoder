abcd = list(map(int, input().split()))

flag = False
for i in range(pow(2, 4)):
    eat = 0
    res = 0
    for j in range(4):
        if i >> j & 1:
            eat += abcd[j]
        else:
            res += abcd[j]
    if eat == res:
        flag = True
        break

if flag:
    print('Yes')
else:
    print('No')