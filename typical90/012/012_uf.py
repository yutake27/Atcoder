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


def solve(h, w, Q):
    uf = UnionFind((h + 2) * (w + 2))
    mat = [[0] * (w + 2) for _ in range(h + 2)]

    def getNodeNum(r, c):
        return r * (w + 2) + c

    for i in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            _, r, c = q
            mat[r][c] = 1
            n = getNodeNum(r, c)
            for x, y in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
                if mat[r + x][c + y]:
                    nc = getNodeNum(r + x, c + y)
                    uf.unite(n, nc)
        elif q[0] == 2:
            _, ra, ca, rb, cb = q
            na = getNodeNum(ra, ca)
            nb = getNodeNum(rb, cb)
            if uf.root(na) == uf.root(nb) and mat[ra][ca] and mat[rb][cb]:
                print('Yes')
            else:
                print('No')


def main():
    h, w = map(int, input().split())
    Q = int(input())
    solve(h, w, Q)


if __name__ == '__main__':
    main()
