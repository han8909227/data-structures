"""BST data structure."""


class Node(object):
    """Node class used for the bst."""

    def __init__(self, data=None, left=None, right=None):
        """Init node."""
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree(object):
    """Binary search tree class."""

    def __init__(self, root=None):
        """Init the bst class."""
        self.count = 0
        if root is None:
            self.root = root
        elif isinstance(root, int) or isinstance(root, float):
            self.root = Node(root)
            self.count += 1
        else:
            raise ValueError('root value must be a number!')

    def insert(self, item):
        """Insert a value/node into the tree."""
        if self.root is None:
            self.root = Node(item)
            self.count += 1
        elif isinstance(item, int) or isinstance(item, float):
            curr_data = self.root
            while curr_data is not None:
                if item < curr_data.data:
                    if curr_data.left is None:
                        curr_data.left = Node(item)
                        self.count += 1
                        return
                    else:
                        curr_data = curr_data.left
                else:  # greater than current node
                    if curr_data.right is None:
                        curr_data.right = Node(item)
                        self.count += 1
                        return
                    else:
                        curr_data = curr_data.right
        else:
            raise ValueError('can only insert number')

    def search(self, item):
        """Search a value in the tree."""
        node = self.root
        while node is not None:
            if node.data == item:
                return node
            elif node.data < item:
                node = node.right
                continue
            else:
                node = node.left
                continue
        return

    def size(self):
        """Return the size of the current tree."""
        return self.count

    def contains(self, item):
        """Return a boolean value if a node is in the tree."""
        return isinstance(self.search(item), Node)

    def depth(self, root):
        """Return the depth of the current tree."""
        if self.count == 0 or self.count == 1:
            return 0
        elif root is None:
            return -1
        else:
            return max(self.depth(root.left), self.depth(root.right)) + 1

    def balance(self):
        """Return the current balance of the tree."""
        if self.root is None:
            return 0
        elif hasattr(self.root, 'left') and hasattr(self.root, 'right'):
            left_depth = self.depth(self.root.left)
            right_depth = self.depth(self.root.right)
            return left_depth - right_depth
        elif hasattr(self.root, 'right'):
            return self.depth(self.root.right)
        else:
            return self.depth(self.root.left)
