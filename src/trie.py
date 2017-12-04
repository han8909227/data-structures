"""Trie in python."""


class Node(object):
    """Node class for trie."""

    def __init__(self, end_node=False):
        """Init instance of node."""
        self.assert_end = end_node
        self.prefix_count = 0
        self.children = {}


class Trie(object):
    """Trie (prefix tree) in python."""

    def __init__(self):
        """Init a trie instance."""
        self.root = Node()
        self.size = 0

    def insert(self, string):
        """Insert a word into the tree."""
        if not isinstance(string, str):
            raise ValueError('can only insert string')
        curr = self.root
        for letter in string:
            if letter not in curr.children:
                curr[letter] = Node()
            curr = curr.children[letter]
            curr.prefix_count += 1
        curr.assert_end = True
        self.size += 1

    def search(self, string):
        """Search for a word in the tree."""
        if not isinstance(string, str):
            raise ValueError('can only search string')
        curr = self.root
        for letter in string:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return curr.assert_end

    def size(self):
        """Return the size of current prefix tree."""
        return self.size

# insert(self, string)
# contains(self, string)
# size(self)
# remove(self, string)