class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    # Insert method to create nodes
    def insert(self, data):

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

    # findval method to compare the value with nodes
    def find_value(self, value):
        if value < self.data:
            if self.left is None:
                return str(value) + " Not Found"
            return self.left.find_value(value)
        elif value > self.data:
            if self.right is None:
                return str(value) + " Not Found"
            return self.right.find_value(value)
        else:
            print(str(self.data) + ' is found')

    # Print the tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()


def sum_nodes(node):
    if node is None:
        return 0
    return node.key + sum_nodes(node.left) + sum_nodes(node.right)

root = Node(12)
root.left = Node(11)
root.left.left = Node(10)
root.right = Node(13)
root.right.right = Node(14)
print(root.find_value(7))
print(root.find_value(14))
print(sum_nodes(12))


