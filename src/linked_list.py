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


class LinkedList(object):
    """Linked-List class."""

    def __init__(self, iterable=None):
        """Initialize the LinkedList as an instance."""
        self.head = None
        if isinstance(iterable, (str, tuple, list)):
            for item in iterable:
                self.insert(item)

    def insert(self, data):
        """Insert or push a value into the linked-list."""
        new_node = Node(data, self.head)
        new_node.set_next(self.head)
        self.head = new_node

    def display(self):
        """Display the current lnked-list."""
        current = self.head
        final_str = '('
        while current:
            current_data = current.get_data()
            final_str += '{}, '.format(current_data)
            current = current.get_next()
        final_str += ')'
        return final_str

    def size(self):
        """Return the size of the current linked-list."""
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        """Search for an value in the linked-list."""
        current = self.head
        match = False
        while current and not match:
            if current.get_data() == data:
                match = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError('Value not in the linked-list')
        return current.data

    def delete(self, data):
        """Delete an value from the linked-list."""
        current = self.head
        previous = None
        while current:
            if current.get_data() == data:
                    break
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Value not in the linked-list")
        elif previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def pop(self):
        """Pop the head of the linked-list."""
        try:
            output = self.head.data
            self.head = self.head.get_next()
            return output
        except AttributeError:
            raise Exception('No value left to pop!')

    def __len__(self):
        """Return the length of linked-list."""
        return self.size()

    def __print__(self):
        """Print out the current linked-list."""
        return self.display()
