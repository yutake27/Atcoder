n = int(input())
D = [list(map(int, input().split())) for _ in range(n)]

count = 0
ans = 'No'
for dd in D:
    d1, d2 = dd
    if d1 == d2:
        count += 1
    else:
        count = 0
    if count == 3:
        ans = 'Yes'

print(ans)