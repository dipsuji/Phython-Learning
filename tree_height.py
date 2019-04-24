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


def height_of_tree(node):
    if node is None:
        return 0
    else:
        lHeight = height_of_tree(node.left)
        print("lheight", lHeight)
        rHeight = height_of_tree(node.right)
        print("rheight", rHeight)

        if lHeight > rHeight:
            return lHeight + 1
        else:
            return rHeight + 1


root = Node(12)
root.left = Node(11)
root.left.left = Node(10)
root.left.left.left = Node(13)
root.left.right = Node(14)
root.right = Node(18)
root.right.right = Node(20)
root.right.left = Node(15)

root.print_tree()

print("Height of tree is %d" % (height_of_tree(root)))

print("minimum number in tree is %d" % (min_num(root)))
