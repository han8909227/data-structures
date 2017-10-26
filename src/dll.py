"""."""


class Node(object):
    """."""

    def __init__(self, data, next=None, previous=None):
        """."""
        self.data = data
        self.next = next
        self.previous = previous


class DoublyLinkedList(object):
    """."""

    def __init__(self):
        """."""
        self.head = None
        self.tail = None

    def push(self, data):
        """."""
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
        """."""
        if not self.head:
            raise ValueError('No val to pop')
        else:
            result = self.head.data
            self.head = self.head.next
            return result

    def shift(self):
        """."""
        if not self.tail:
            raise ValueError('No tail to shift')
        else:
            temp = self.head
            if not temp.next:
                result = self.head.data
                self.tail = None
                self.head = None
            else:
                while temp.next:
                    temp = temp.next
                result = temp.data
                self.tail = temp.previous
                temp.previous.next = None
            return result

    def append(self, data):
        """."""
        new_node = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.previous = temp

    def delete(self, data):
        """."""
        temp = self.head
        if temp.next:
            if(temp.data == data):
                temp.next.previous = None
                self.head = temp.next
                temp.next = None
                return
            else:
                while temp.next:
                    if(temp.data == data):
                        break
                    temp = temp.next
                if(temp.next):
                    temp.previous.next = temp.next
                    temp.next.previous = temp.previous
                    temp.next = None
                    temp.previous = None
                else:
                    temp.previous.next = None
                    temp.previous = None
                return

        if not temp:
            return

    def printdll(self):
        """."""
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
