n = int(input())
a = sorted(list(map(int, input().split())))

q = int(input())
b = sorted([(int(input()), j) for j in range(q)])

i = 0
ans = [-1] * q
for bj, j in b:
    while True:
        if i + 1 < n and abs(a[i] - bj) >= abs(a[i + 1] - bj):
            i += 1
        else:
            ans[j] = abs(a[i] - bj)
            break

print(*ans, sep='\n')
