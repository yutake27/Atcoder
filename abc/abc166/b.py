n, k = map(int, input().split())

treat_array = [0]*n
for i in range(k):
    d = int(input())
    for j in map(int, input().split()):
        treat_array[j-1] += 1

ans = 0
for i in range(n):
    if treat_array[i] == 0:
        ans += 1

print(ans)
