"""Create a queue class."""


class Queue(object):
    """Will create a instance of Queue and allow enqueue(), dequeue(), peek(), size() and len() methods to work."""

    def __init__(self, iterable=None):
        """Will init a new instance of the Stack class."""
        from dll import DoubleLinkedList
        self._dll = DoubleLinkedList()
        self._counter = 0

    def enqueue(self, data):
        """Will push a new element into the Queue."""
        self._dll.append(data)
        self._counter += 1

    def dequeue(self):
        """Will remove the first element in the Queue."""
        if self._dll.head:
            self._counter -= 1
        return self._dll.pop()

    def peek(self):
        """Will return the next value in the Queue."""
        return self._dll.head.data

    def __len__(self):
        """Will return the length of the stack using len()."""
        return self._counter
