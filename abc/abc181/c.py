n = int(input())
xy_list = [list(map(int, input().split())) for _ in range(n)]

flag = False
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            xi, yi = xy_list[i]
            xj, yj = xy_list[j]
            xk, yk = xy_list[k]
            vec_ij = (xj - xi, yj - yi)
            vec_ik = (xk - xi, yk - yi)
            if vec_ij[1] * vec_ik[0] == vec_ij[0] * vec_ik[1]:
                flag = True
                break

if flag:
    print('Yes')
else:
    print('No')