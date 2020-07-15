L, R, d = list(map(int, input().split()))

num = 0
for i in range(L, R+1):
    if i%d == 0:
        num += 1

print(num)