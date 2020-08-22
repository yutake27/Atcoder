from collections import deque

h, w = map(int, input().split())
ch, cw = map(int, input().split())
dh, dw = map(int, input().split())
S = [list(input()) for _ in range(h)]


def clear_maze(h, w, ch, cw, dh, dw, S):
    visited = [[-1] * w for _ in range(h)]
    visited[ch - 1][cw - 1] = 0
    queue = deque([[ch - 1 , cw - 1]])
    m_queue = deque([])
    while queue or m_queue:
        if queue:
            y, x = queue.popleft()
        else:
            n_y, n_x, y, x = m_queue.popleft()
            if visited[n_y][n_x] != -1:
                continue
            visited[n_y][n_x] = visited[y][x] + 1
            y, x = n_y, n_x
        if [y, x] == [dh - 1, dw - 1]:
            return visited[y][x]
        num = 0
        for i, j in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            n_y = y + i
            n_x = x + j
            if n_y >= 0 and n_y < h and n_x >= 0 and n_x < w and S[n_y][n_x] == '.' and visited[n_y][n_x] == -1:
                visited[n_y][n_x] = visited[y][x]
                queue.append([n_y, n_x])
        for i in range(-2, 2 + 1):
            for j in range(-2, 2 + 1):
                if not [i, j] in ([1, 0], [-1, 0], [0, 0], [0, 1], [0, -1]):
                    n_y = y + i
                    n_x = x + j
                    if n_y >= 0 and n_y < h and n_x >= 0 and n_x < w and S[n_y][n_x] == '.' and visited[n_y][n_x] == -1:
                        m_queue.append([n_y, n_x, y, x])
    return -1

print(clear_maze(h, w, ch, cw, dh, dw, S))