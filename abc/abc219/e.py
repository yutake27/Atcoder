A = [list(map(int, input().split())) for _ in range(4)]


class UnionFind:
    def __init__(self, node_num):
        self.node_num = node_num
        self.root_array = [-1] * node_num

    def root(self, x):
        if self.root_array[x] < 0:
            return x
        else:
            self.root_array[x] = self.root(self.root_array[x])
            return self.root_array[x]

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        if self.root_array[x] > self.root_array[y]:
            x, y = y, x
        self.root_array[x] += self.root_array[y]
        self.root_array[y] = x

    def size(self, x):
        return -self.root_array[self.root(x)]


def nodeNum(i, j):
    return 6 * i + j


def judge(mat):
    uf = UnionFind(36)
    # 連結判定のためにUnite
    for i in range(6):
        for j in range(6):
            if 1 <= i < 5 and 1 <= j < 5 and A[i - 1][j - 1] == 1:  # 村の場合
                if mat[i][j] != 1:
                    return False
            node_num = nodeNum(i, j)
            if i != 0 and mat[i][j] == mat[i - 1][j]:
                uf.unite(node_num, nodeNum(i - 1, j))
            if j != 0 and mat[i][j] == mat[i][j - 1]:
                uf.unite(node_num, nodeNum(i, j - 1))
            if i != 5 and mat[i][j] == mat[i + 1][j]:
                uf.unite(node_num, nodeNum(i + 1, j))
            if j != 5 and mat[i][j] == mat[i][j + 1]:
                uf.unite(node_num, nodeNum(i, j + 1))
    # 連結要素数が二つならOK
    root_set = set()
    for i in range(6 * 6):
        root_set.add(uf.root(i))
    if len(root_set) == 2:
        return True
    else:
        return False


# bit全探索
ans = 0
for i in range(pow(2, 16)):
    mat = [[0] * 6 for _ in range(6)]
    for j in range(16):
        j_use = (i >> j) & 1
        mat[j // 4 + 1][j % 4 + 1] = j_use
    if judge(mat):
        ans += 1
print(ans)
