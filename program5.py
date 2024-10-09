class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0  # To keep track of the queue's size

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:  # If the queue is empty
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1  # Increment size when enqueuing

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None
        
        self._size -= 1  # Decrement size when dequeuing
        return temp.value

    def size(self):
        return self._size

# Main program to handle multiple test cases
if __name__ == "__main__":
    t = int(input("Enter the number of test cases: "))  # Number of test cases

    for _ in range(t):
        queue = LinkedListQueue()  # Create a new queue for each test case
        n = int(input())  # Number of commands for this test case
        
        for _ in range(n):
            command = input().strip().split()
            
            if command[0] == "enqueue":
                value = int(command[1])
                queue.enqueue(value)
            
            elif command[0] == "dequeue":
                dequeued_value = queue.dequeue()
                if dequeued_value is not None:
                    print(dequeued_value)  # Output the dequeued value
            
            elif command[0] == "size":
                print(queue.size())  # Output the size of the queue
