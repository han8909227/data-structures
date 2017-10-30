"""Linked List Class."""


class Node(object):
    """Node class."""

    def __init__(self, data=None, next_data=None, previous_data=None):
        """Initialize the node structure."""
        self.data = data
        self.next_node = next_data


class LinkedList(object):
    """Linked-List class."""

    def __init__(self, iterable=None):
        """Initialize the LinkedList as an instance."""
        self.head = None
        self.count = 0
        if isinstance(iterable, (str, tuple, list)):
            for item in iterable:
                self.insert(item)
        elif iterable is None:
            pass
        else:
            raise TypeError('Either str, tuple or list!')

    def insert(self, data):
        """Insert or push a value into the linked-list."""
        old_head = self.head
        self.head = Node(data, self.head)
        self.head.next_node = old_head
        self.count += 1

    def display(self):
        """Display the current lnked-list."""
        current = self.head
        final_str = '('
        while current:
            current_data = current.data
            final_str += '{}, '.format(current_data)
            current = current.next_node
        final_str += ')'
        return final_str

    def size(self):
        """Return the size of the current linked-list."""
        return self.count

    def search(self, data):
        """Search for an value in the linked-list."""
        current = self.head
        match = False
        while current and not match:
            if current.data == data:
                match = True
            else:
                current = current.next_node
        if current is None:
            raise ValueError('Value not in the linked-list')
        return current.data

    def delete(self, data):
        """Delete an value from the linked-list."""
        current = self.head
        previous = None
        while current:
            if current.data == data:
                    break
            else:
                previous = current
                current = current.next_node
        if current is None:
            raise ValueError("Value not in the linked-list")
        elif previous is None:
            self.head = current.next_node
        else:
            previous.next_node = current.next_node
        self.count -= 1

    def pop(self):
        """Pop the head of the linked-list."""
        output = self.head
        if not self.head:
            raise ValueError("Nothing left to pop")
        self.head = self.head.next_node
        self.count -= 1
        return output.data

    def __len__(self):
        """Return the length of linked-list."""
        return self.size()

    def __print__(self):
        """Print out the current linked-list."""
        return self.display()
