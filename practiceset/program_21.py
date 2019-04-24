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


def sum_nodes(node):
    if node is None:
        return 0
    if node.data <= 14:
        return sum_nodes(node.left) + sum_nodes(node.right)
    else:
        return node.data + sum_nodes(node.left) + sum_nodes(node.right)


def even_node(node):
    if node is None:
        return 0
    if node.data % 2 == 0:
        print(node.data)

    even_node(node.left)
    even_node(node.right)


# A utility function to check if a given node is leaf or not
def isLeaf(node):
    if node is None:
        return False
    if node.left is None and node.right is None:
        return True
    return False


# This function return sum of all left leaves in a
# given binary tree
def leftLeavesSum(root):
    # Initialize result
    res = 0

    # Update result if root is not None
    if root is not None:

        # If left of root is None, then add key of
        # left child
        if isLeaf(root.left):
            res += root.left.data
        else:
            # Else recur for left child of root
            res += leftLeavesSum(root.left)

            # Recur for right child of root and update res
        res += leftLeavesSum(root.right)
    return res


root = Node(12)
root.left = Node(11)
root.left.left = Node(10)
root.left.right = Node(14)
root.right = Node(18)
root.right.right = Node(20)
root.right.left = Node(15)

root.print_tree()

print("Sum of left leaves is", leftLeavesSum(root))

print("Sum of num greater than given number is : ", sum_nodes(root))

even_node(root)
