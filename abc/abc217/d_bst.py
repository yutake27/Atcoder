l, q = map(int, input().split())


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self, root_data):
        self.root = Node(root_data)

    def insert(self, data):
        e = self.root
        new_node = Node(data)
        while True:
            if e.data < data:
                if e.right is None:
                    e.right = new_node
                    return
                else:
                    e = e.right
            else:
                if e.left is None:
                    e.left = new_node
                    return
                else:
                    e = e.left

    def search(self, data):
        e = self.root
        right = self.root.data
        left = self.root.data
        while True:
            # print('r:l', right, left)
            if e.data < data:
                left = e.data
                if e.right is None:
                    return right - left
                e = e.right
            else:
                right = e.data
                if e.left is None:
                    return right - left
                else:
                    e = e.left


bst = BST(l)
bst.insert(0)

for _ in range(q):
    l, q = map(int, input().split())
    if l == 1:
        bst.insert(q)
    elif l == 2:
        print(bst.search(q))
