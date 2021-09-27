n = int(input())
A = list(map(int, input().split()))
x = int(input())

sum_A = sum(A)
div, mod = divmod(x, sum_A)

s = 0
for i in range(n):
    s += A[i]
    if mod < s:
        break

ans = div * n + i + 1
print(ans)
