N = int(input())
a = list(map(int, input().split()))

num = 0
for i in range(N):
    if (i+1)%2 == 1 and a[i] % 2 == 1:
        num += 1

print(num)