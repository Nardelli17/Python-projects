class CircularQueue:
    """Implementation of a circular queue."""

    def __init__(self, size):
        """
        Initializes the circular queue.

        Args:
            size (int): Maximum size of the queue.
        """
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        """Checks if the queue is empty."""
        return self.front == -1

    def is_full(self):
        """Checks if the queue is full."""
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, item):
        """
        Adds an element to the circular queue.

        Args:
            item (any): Element to be inserted.

        Returns:
            bool: True if the insertion was successful, False if the queue is full.
        """
        if self.is_full():
            print("Error: Queue is full!")
            return False

        if self.is_empty():
            self.front = 0  # Initialize the queue if empty

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item
        print(f"Element {item} inserted into the queue.")
        return True

    def dequeue(self):
        """
        Removes an element from the circular queue.

        Returns:
            any: The removed element or None if the queue is empty.
        """
        if self.is_empty():
            print("Error: Queue is empty!")
            return None

        item = self.queue[self.front]

        if self.front == self.rear:  # Only one element in the queue
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        print(f"Element {item} removed from the queue.")
        return item

    def peek(self):
        """
        Returns the first element of the queue without removing it.

        Returns:
            any: The first element of the queue or None if the queue is empty.
        """
        if self.is_empty():
            print("Error: Queue is empty!")
            return None
        return self.queue[self.front]

    def display(self):
        """Displays the elements of the circular queue."""
        if self.is_empty():
            print("Queue is empty!")
            return

        print("Queue:", end=" ")
        i = self.front
        while i != self.rear:
            print(self.queue[i], end=" ")
            i = (i + 1) % self.size
        print(self.queue[self.rear])  # Print the last element


def run_tests():
    """Runs tests on the circular queue implementation."""
    queue = CircularQueue(5)

    # Test enqueue operation
    assert queue.enqueue(10) == True
    assert queue.enqueue(20) == True
    assert queue.enqueue(30) == True
    assert queue.enqueue(40) == True
    assert queue.enqueue(50) == True
    assert queue.enqueue(60) == False  # Should fail (queue is full)

    queue.display()

    # Test dequeue operation
    assert queue.dequeue() == 10
    assert queue.dequeue() == 20

    queue.display()

    # Test enqueue after dequeue
    assert queue.enqueue(60) == True
    assert queue.enqueue(70) == True

    queue.display()

    # Test peek
    assert queue.peek() == 30

    print("All tests passed ✅")


if __name__ == "__main__":
    run_tests()
