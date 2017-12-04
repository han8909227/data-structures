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

    def __init__(self, iterable=()):
        """Init a trie instance."""
        self.root = Node()
        self.size = 0
        if isinstance(iterable, (str, list, tuple)):
            for word in iterable:
                self.insert(word)

    def insert(self, string):
        """Insert a word into the tree."""
        if not isinstance(string, str):
            raise ValueError('can only insert string')
        curr = self.root
        for letter in string:
            if letter not in curr.children:
                curr.children[letter] = Node()
            curr = curr.children[letter]
            curr.prefix_count += 1
        curr.assert_end = True
        self.size += 1

    def contains(self, string):
        """Search for a word in the tree."""
        if not isinstance(string, str):
            raise ValueError('can only search string')
        curr = self.root
        for letter in string:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return curr.assert_end

    def remove(self, string):
        """Remove an word from the tree."""
        curr = self.root
        stack = []
        for letter in string:
            if letter not in curr.children:
                raise ValueError('no such word exist in trie')
            stack.append(curr)
            curr = curr.children[letter]
        if curr.assert_end:
            self._erase_children(stack, string)
        else:
            raise ValueError('no such word exist in trie')

    def _erase_children(self, stack, string):
        """Remove the word in the tree."""
        reverse_word = string[::-1]
        i = -1
        for letter in reverse_word:
            if len(stack[i].children[letter].children) == 0:
                del stack[i].children[letter]
            else:
                stack[i].children[letter].assert_end = False
                break
            i -= 1
        self.size -= 1

    def size(self):
        """Return the size of current prefix tree."""
        return self.size
