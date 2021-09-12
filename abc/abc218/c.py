n = int(input())
s = [list(input()) for _ in range(n)]
t = [list(input()) for _ in range(n)]


def rotate(S):
    return list(zip(*S[::-1]))


def find_lefttop(M):
    for i in range(n):
        for j in range(n):
            if M[i][j] == '#':
                return i, j


def judge_match(S, T):
    si, sj = find_lefttop(S)
    ti, tj = find_lefttop(T)
    di, dj = si - ti, sj - tj
    for i in range(n):
        for j in range(n):
            ii, jj = i + di, j + dj
            if 0 <= ii < n and 0 <= jj < n:
                if S[ii][jj] != T[i][j]:
                    return False
            else:
                if S[ii % n][jj % n] == '#':
                    return False
                if T[i][j] == '#':
                    return False
    return True


for i in range(4):
    if judge_match(s, t):
        print('Yes')
        exit()
    s = rotate(s)
print('No')
