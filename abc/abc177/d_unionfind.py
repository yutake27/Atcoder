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


def solve(n, m, ab_array):
    uf = union_find(n)
    for ab in ab_array:
        a, b = ab
        uf.unite(a - 1, b - 1)

    ans = 0
    for i in range(n):
        ans = max(ans, uf.size(i))

    return ans

if __name__ == '__main__':
    n, m = map(int, input().split())
    ab_array = [list(map(int, input().split())) for _ in range(m)]
    ans = solve(n, m, ab_array)
    print(ans)
