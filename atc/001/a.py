from collections import deque

h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]


def dfs(h, w, sh, sw, gh, gw, c):
    num = 0
    queue = deque([[sh, sw]])
    visited = [[-1] * w for _ in range(h)]
    visited[sh][sw] = -1
    while queue:
        y, x = queue.pop()
        if visited[y][x] != -1:
            continue
        else:
            num += 1
            visited[y][x] = num
        
        if [y, x] == [gh, gw]:
            return num
        
        for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            ny = y + i
            nx = x + j
            if (0 <= nx < w) and (0<= ny < h) and visited[ny][nx] == -1 and c[ny][nx] != '#':
                queue.append([ny, nx])
    return -1


def get_start_and_goal(h, w, c):
    for i in range(h):
        for j in range(w):
            if c[i][j] == 's':
                sh, sw = i, j
            elif c[i][j] == 'g':
                gh, gw = i, j
    return sh, sw, gh, gw


sh, sw, gh, gw = get_start_and_goal(h, w, c)
ans = dfs(h, w, sh, sw, gh, gw, c)
if ans < 0:
    print('No')
else:
    print('Yes')