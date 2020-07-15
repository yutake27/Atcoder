N = int(input())
H = list(map(int, input().split()))

for i in range(N-1):
    if H[-i-1] == H[-i-2]-1:
        H[-i-2] -= 1
    elif H[-i-1] < H[-i-2]:
        print('No')
        quit()
print('Yes')