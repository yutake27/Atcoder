h = int(input())

count = 1
while h > 1:
    h = h // 2
    count += 1

ans = pow(2, count) - 1
print(ans)