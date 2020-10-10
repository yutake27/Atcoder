a_mat = [list(map(int, input().split())) for _ in range(3)]
n = int(input())


a_hit = [False] * 9
for i in range(n):
    b = int(input())
    for j in range(9):
        if a_mat[j // 3][j % 3] == b:
            a_hit[j] = True

ans = 'No'
for i in range(3):
    if a_hit[i] and a_hit[i + 3] and a_hit[i + 6]:
        ans = 'Yes'
    elif a_hit[i * 3] and a_hit[i * 3 + 1] and a_hit[i * 3 + 2]:
        ans = 'Yes'

if a_hit[0] and a_hit[4] and a_hit[8]:
    ans = 'Yes'
elif a_hit[2] and a_hit[4] and a_hit[6]:
    ans = 'Yes'

print(ans)