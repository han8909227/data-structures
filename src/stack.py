"""Create a Stack class."""


class Stack(object):
    """Will create a instance of Stack and allow push(), pop() and len() to work properly."""

    def __init__(self, iterable=()):
        """Will init a new instance of the Stack class."""
        from linked_list import LinkedList
        self.top_stack = None
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

