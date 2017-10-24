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
        self.top_stack = None
        self._counter = 0
        if isinstance(iterable, (str, tuple, list)):
            for item in iterable:
                self.push(item)

    def push(self, new_stack):
        """Will push a new element into the Stack and add to the counter."""
        new_node = Node(new_stack, self.top_stack)
        new_node.set_next(self.top_stack)
        self.top_stack = new_node
        self._counter += 1

    def pop(self):
        """Will pop the element that is in the top stack position and subtract it from the counter."""
        try:
            output = self.top_stack.data
            self.top_stack = self.top_stack.get_next()
            self._counter -= 1
            return output
        except AttributeError:
            raise Exception('Nothing to pop.')

    def __len__(self):
        """Will return the length of the stack using len()."""
        return self._counter