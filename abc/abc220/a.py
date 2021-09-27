a, b, c = map(int, input().split())
d = ((a - 1) // c + 1) * c
if d <= b:
    print(d)
else:
    print(-1)
