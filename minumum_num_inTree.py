class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()


def min_num(node):
    current = node
    if current:
        while current.left is not None:
            print("current.left:", current.left.data)
            current = current.left
            print("current", current.data)
        return current.data


root = Node(12)
root.left = Node(11)
root.left.left = Node(10)
root.left.left.left = Node(8)
root.left.right = Node(14)
root.right = Node(18)
root.right.right = Node(20)
root.right.left = Node(15)

root.print_tree()

print("minimum number in tree is %d" % (min_num(root)))
