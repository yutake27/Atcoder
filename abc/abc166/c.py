N, M = map(int, input().split())
H = list(map(int, input().split()))
AB = [list(map(int, input().split())) for i in range(M)]

tf_array = [0]*N

for a, b in AB:
    if H[a-1] > H[b-1]:
        tf_array[b-1] += 1
    elif H[a-1] == H[b-1]:
        tf_array[a-1] += 1
        tf_array[b-1] += 1
    else:
        tf_array[a-1] += 1

print(tf_array.count(0))
