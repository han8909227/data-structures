"""Doubly Linked List Data Structure."""


class Node(object):
    """Create a Node class."""

    def __init__(self, data, next_data=None, previous_data=None):
        """Initialize a Node instance."""
        self.data = data
        self.next = next_data
        self.previous = previous_data


class DoubleLinkedList(object):
    """Create a doubly linked list class."""

    def __init__(self):
        """Initialize a double link list instance."""
        self.head = None
        self.tail = None

    def push(self, data):
        """Add a value to the head of the dll."""
        if not self.head:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(data)
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        """Pop the first value from the dll."""
        if not self.head:
            raise IndexError('No val to pop')
        elif self.head == self.tail:
            result = self.head.data
            self.head = None
            self.tail = None
            return result
        else:
            result = self.head.data
            self.head = self.head.next
            return result

    def shift(self):
        """Pop the last value from the dll."""
        if not self.tail:
            raise IndexError('No tail to shift')
        else:
            if self.head == self.tail:
                result = self.tail
                self.tail = None
                self.head = None
            else:
                result = self.tail.data
                self.tail = self.tail.previous
                self.tail.next = None
            return result

    def append(self, data):
        """Add a value to the end of dll."""
        if not self.head:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(data)
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.previous = temp
            self.tail = new_node

    def remove(self, data):
        """Delete a specific value from the dll."""
        temp = self.head
        if not self.head or not self.tail:
            raise ValueError('No value in the list to remove.')
        if temp.data == data == self.tail.data:
            self.head = None
            self.tail = None
            return
        elif temp.data == data:
            self.head = self.head.next
            return
        elif self.tail.data == data:
            self.tail = self.tail.previous
            return
        else:
            while temp.next:
                if(temp.data == data):
                    break
                temp = temp.next
            if temp.next:
                temp.previous.next = temp.next
                temp.next.previous = temp.previous
                return
            else:
                temp.previous.next = None
                return
        if not temp:
            raise ValueError('Delete value does not exist in DLL')

    def printdll(self):
        """Print the dll."""
        temp = self.head
        final_str = '('
        while temp:
            final_str += '{}, '.format(temp.data)
            temp = temp.next
        final_str += ')'
        return final_str

    def __len__(self):
        """Length of the list."""
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count
