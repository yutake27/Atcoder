x = int(input())

ans = 0
m = 100
while m < x:
    m += m//100
    ans += 1

print(ans)