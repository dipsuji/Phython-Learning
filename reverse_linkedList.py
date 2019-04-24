class Node:

    def __init__(self, data):
        """
        Constructor to initialize the node object
        :param data:
        """
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def push(self, new_data):
        """
        Function to insert a new node at the beginning
        :param new_data:
        :return:
        """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def reverse(self):
        """
        Function to reverse the linked list
        :return:
        """
        prev = None
        current = self.head
        while (current is not None):
            next1 = current.next #2
            current.next = prev #none
            prev = current
            current = next1
        self.head = prev

    def print_list(self):
        """
        Utility function to print the linked LinkedList
        :return:
        """
        temp = self.head
        while (temp):
            print(temp.data),
            temp = temp.next


# Driver program to test above functions
llist = LinkedList()
llist.push(2)
llist.push(4)
llist.push(5)
llist.push(8)

print("Given Linked List is: ")
llist.print_list()
llist.reverse()
print("\nReversed Linked List is: ")
llist.print_list()