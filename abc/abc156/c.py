n = int(input())
x_list = list(map(int, input().split()))

p = sum(x_list) / n
if abs(int(p) + 1 - p) < abs(int(p) - p):
    p = int(p) + 1
else:
    p = int(p)

ans = 0
for x in x_list:
    ans += pow(x - p, 2)

print(ans)