x, y, a, b = map(int, input().split())

st = x
ex = 0
while st < y:
    if st * a <= st + b:
        if st * a >= y:
            break
        st *= a
        ex += 1
    else:
        break

ans = ex + (y - st - 1) // b
print(int(ans))