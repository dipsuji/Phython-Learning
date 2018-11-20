class Queue:

    # Constructor creates a list
    def __init__(self):
        self.queue = list()

    # Adding elements to queue
    def enqueue(self, data):
        """
        Enqueue elements to the beginning of the Queue and issue a warning if it's full
        :param data:
        :return:
        """
        # Checking to avoid duplicate entry (not mandatory)
        if data not in self.queue:
            self.queue.insert(0, data)
            return True
        return False

    # Removing the last element from the queue
    def dequeue(self):
        """
        Dequeue elements from the end of the Queue and issue a warning if it’s empty
        :return:
        """
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("Queue is Empty!")

    # Getting the size of the queue
    def size(self):
        """
        Assess the size of the Queue
        :return:
        """
        return len(self.queue)

    # printing the elements of the queue
    def printqueue(self):
        """
        Print all the elements of the Queue
        :return:
        """
        print("printing......")
        return self.queue


myQueue = Queue()

#

print(myQueue.enqueue(5))  # prints True
print(myQueue.enqueue(6))  # prints True
print(myQueue.enqueue(9))  # prints True
print(myQueue.enqueue(5))  # prints False
print(myQueue.enqueue(3))  # prints True

myQueue.printqueue()

print("size of queue:", myQueue.size())  # prints 4

print(myQueue.dequeue())  # prints 5

myQueue.printqueue()

print(myQueue.dequeue())  # prints 6
print(myQueue.dequeue())  # prints 9
print(myQueue.dequeue())  # prints 3

print("size of queue:", myQueue.size())  # prints 0

print(myQueue.dequeue())  # prints Queue Empty!
