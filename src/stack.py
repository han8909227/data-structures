"""."""


class Node(object):
    """Node class."""

    def __init__(self, data=None, next_data=None):
        """Initialize the node structure."""
        self.data = data
        self.next_node = next_data

    def get_data(self):
        """Return current data."""
        return self.data

    def get_next(self):
        """Return next data."""
        return self.next_node

    def set_data(self, newdata):
        """Set next data."""
        self.data = newdata

    def set_next(self, new_next):
        """."""
        self.next_node = new_next


class Stack(object):
    """."""

    def __init__(self, iterable=()):
        """Will init a new instance of the Stack class."""
        from linked_list import LinkedList
        self.top_stack = None
        self._counter = 0
        self._linked_list = LinkedList()
        if isinstance(iterable, (str, tuple, list)):
            for item in iterable:
                self.push(item)

    def push(self, new_stack):
        """Will push a new element into the Stack and add to the counter."""
        self._linked_list.insert(new_stack)

    def pop(self):
        """Will pop the element that is in the top stack position and subtract it from the counter."""
        return self._linked_list.pop()


    def __len__(self):
        """Will return the length of the stack using len()."""
        return self._linked_list.size()