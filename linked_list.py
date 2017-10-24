"""."""


class Node(object):
    """."""
    def __init__(self, data=None, next_data=None):
        """."""
        self.data = data
        self.next_node = next_data

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
        self.head = Node(head)

    def insert(self, data):
        """."""
        new_node = Node(data, self.head)
        new_node.set_next(self.head)
        self.head = new_node

    def display(self):
        """."""
        current = self.head
        final_str = '('
        while current:
            current_data = current.get_data()
            final_str += '{}, '.format(current_data)
            current = current.get_next()
        final_str += ')'
        return final_str

    def size(self):
        """."""
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        """."""
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError('Value not in the linked-list')
        return current

    def delete(self, data):
        """."""
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Value not in the linked-list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

