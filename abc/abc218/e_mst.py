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


n, m = map(int, input().split())
E = []

sum_c = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    E.append((c, a, b))
    sum_c += c

uf = UnionFind(n + 1)
for c, a, b in sorted(E):
    if uf.root(a) != uf.root(b):
        uf.unite(a, b)
        sum_c -= c
    elif c < 0:
        sum_c -= c

print(sum_c)
