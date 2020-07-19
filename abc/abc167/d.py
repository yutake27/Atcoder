n, k = map(int, input().split())
A = list(map(int, input().split()))

now = A[0]
root_set = set([now])
root_array = [now]
if k<= n:
    for i in range(k-1):
        now = A[now-1]
        root_set.add(now)
        root_array.append(now)
    print(root_array[-1])
else:
    for i in range(n-1):
        now = A[now-1]
        if not now in root_set:
            root_set.add(now)
            root_array.append(now)
        else:
            index = root_array.index(now)
            f = root_array[:index]
            loop = root_array[index:]
            break
    len_f = len(f)
    len_loop = len(loop)
    print(loop[(k-len_f)%len_loop-1])