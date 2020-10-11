h, w = map(int, input().split())

s_list = [list(input()) for _ in range(h)]

ans = 0
for i in range(h):
    for j in range(w):
        if j != w - 1 and s_list[i][j] == '.' and s_list[i][j + 1] == '.':
            ans += 1
        if i != h - 1 and s_list[i][j] == '.' and s_list[i + 1][j] == '.':
            ans += 1
print(ans)