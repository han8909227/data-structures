"""Create a deque class."""


class Deque(object):
    """Will create a instance of Deque."""

    def __init__(self, iterable=None):
        """Will init a new instance of the Stack class."""
        from dll import DoubleLinkedList
        self._dll = DoubleLinkedList()
        self._counter = 0

    def append(self, data):
        """Will push a new element into the Deque."""
        self._dll.append(data)
        self._counter += 1

    def pop_left(self):
        """Will remove the head value."""
        if self._dll.head:
            self._counter -= 1
        else:
            raise ValueError('no value left to pop')
        return self._dll.pop()

    def append_left(self, data):
        """Append a value to the head."""
        self._dll.push(data)
        self._counter += 1

    def pop(self):
        """Pop a value from the end."""
        if self._dll.tail:
            self._counter -= 1
        else:
            raise ValueError('no value left to pop')
        return self._dll.shift()

    def peek_left(self):
        """Will return the value that pop_left would return."""
        if self._dll.head:
            return self._dll.head.data
        else:
            raise ValueError('no value in the deque to peek')

    def peek(self):
        """Will return the value that pop would return."""
        if self._dll.head:
            return self._dll.tail.data
        else:
            raise ValueError('no value in the deof correct typeque to peek')

    def size(self):
        """Return the size of the deque."""
        return self._counter

    def __len__(self):
        """Will return the length of the deque using len()."""
        return self._counter
