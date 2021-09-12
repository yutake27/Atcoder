P = list(map(int, input().split()))

for p in P:
    print(chr(ord('a') + p - 1), end='')
