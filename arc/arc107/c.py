import math

class union_find:
    def __init__(self, node_num):
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


n, k = map(int, input().split())
a_list = [list(map(int, input().split())) for _ in range(n)]

uf = union_find(2 * n)

for i in range(n):
    for j in range(i + 1, n):
        column_flag = True
        for l in range(n):
            if a_list[i][l] + a_list[j][l] > k:
                column_flag = False
                break
        if column_flag:
            uf.unite(i, j)
        row_flag = True
        for l in range(n):
            if a_list[l][i] + a_list[l][j] > k:
                row_flag = False
                break
        if row_flag:
            uf.unite(n + i, n + j)


ans = 1
mod = 998244353
counted = set()
for i in range(2 * n):
    root = uf.root(i)
    if root in counted: continue
    counted.add(root)
    ans = (ans * math.factorial(uf.size(root))) % mod

print(ans)