"""."""


class Node(object):
    """."""
    def __init__(self, data=None):
        """."""
        self.data = data
        self.next_node = None

    def get_data(self):
        """."""
        return self.data

    def get_next(self):
        """."""
        return self.next_node

    def set_data(self, newdata):
        """."""
        self.data = newdata

    def set_next(self, new_next):
        """."""
        self.next_node = new_next


class Linked_list(object):
    """."""
    def __init__(self, head=None):
        """."""
        self.head = head

    def insert(self, data):
        """."""
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def display(self):
        """."""
        print('({})'.format(self.head))
        current = Node(self.head)
        result = []

        while current:
            result.append(current.get_data())
            current = current.get_next()
        return result

