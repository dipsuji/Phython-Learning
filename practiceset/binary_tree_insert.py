print("Create Root")


class Node:

    def __init__(self, data):
        """
        We just create a Node class and add assign a value to the node. This becomes tree with only a root node.
        :param data:
        """
        self.left = None
        self.right = None
        self.data = data

    def PrintTree(self):
        print(self.data)


root = Node(10)

root.PrintTree()

print("Inserting into a Tree")


class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        """
        Inserting into a Tree
        :param data:
        :return:
        """
        # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()


def printInorder(root):
    if root:
        # First recur on left child
        printInorder(root.left)

        # then print the data of node
        print("val..... " + str(root.data))

        # now recur on right child
        printInorder(root.right)

    # Use the insert method to add nodes


# root = Node(12)
# root.insert(6)
# root.insert(14)
# root.insert(3)
#
# root.PrintTree()

root = Node(12)
root.left = Node(11)
root.left.left = Node(10)
root.right = Node(13)
root.right.right = Node(14)

printInorder(root)
