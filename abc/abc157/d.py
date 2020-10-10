n, m, k = map(int, input().split())

class union_find:
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

uf = union_find(n)
fb_list = [set() for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    fb_list[a].add(b)
    fb_list[b].add(a)
    uf.unite(a, b)

for _ in range(k):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if uf.root(c) == uf.root(d):
        fb_list[c].add(d)
        fb_list[d].add(c)


for i in range(n):
    ans = uf.size(i) - len(fb_list[i]) - 1
    print(ans, end=' ')