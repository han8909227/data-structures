"""BST data structure."""
import timeit


class Node(object):
    """Node class used for the bst."""

    def __init__(self, data=None):
        """Init node."""
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


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
        elif self.search(item):
            return
        elif isinstance(item, int) or isinstance(item, float):
            curr_data = self.root
            while curr_data is not None:
                if item < curr_data.data:
                    if curr_data.left is None:
                        curr_data.left = Node(item)
                        curr_data.left.parent = curr_data
                        self.count += 1
                        return
                    else:
                        curr_data = curr_data.left
                else:  # greater than current node
                    if curr_data.right is None:
                        curr_data.right = Node(item)
                        curr_data.right.parent = curr_data
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
            if node.data == int(item):  # in py2.6 item is str & node.data is int
                return node
            elif node.data < int(item):
                node = node.right
                continue
            else:
                node = node.left
                continue
        return

    def delete(self, item):
        """Delete a node from the tree."""
        target = self.search(item)
        if target is None:
            raise ValueError('val not in bst')
        elif target.left is None and target.right is None:
            if item > target.parent.data:
                target.parent.right = None
            else:
                target.parent.left = None
            return
        elif target.left is None or target.right is None:
            if target.left:
                replacer = target.left
            else:
                replacer = target.right
            if target.parent:
                if target.parent.left is target:
                    target.parent.left = replacer
                else:
                    target.parent.right = replacer
                replacer.parent = target.parent
            else:
                self.root = replacer
                self.root.parent = None
            return
        else:
            replacer = self._delete_helper(target.right)
            target.data = replacer.data
            if replacer is target.right:
                replacer.parent.right = None
            else:
                replacer.parent.left = None
            return

    def _delete_helper(self, node):
        """Return the smallest node on right side of bst from the biggest right side node(passed in)."""
        if node.left is None:
            return node
        return self._delete_helper(node.left)

    def size(self):
        """Return the size of the current tree."""
        return self.count

    def contains(self, item):
        """Return a boolean value if a node is in the tree."""
        return isinstance(self.search(item), Node)

    def depth(self, root):
        """Return the depth of the current tree (o for root only tree)."""
        return max(0, self._depth(root) - 1)

    def _depth(self, root):
        """Return the depth of the current tree internal use only."""
        if root is None:
            return 0
        else:
            return max(self._depth(root.left), self._depth(root.right)) + 1

    def balance(self):
        """Return the current balance of the tree."""
        if self.root is None:
            return 0
        else:
            left_depth = self._depth(self.root.left)
            right_depth = self._depth(self.root.right)
            return left_depth - right_depth

    def in_order(self, root):
        """Return val of tree in-order traversal one at a time."""
        if root is not None:
            for val in self.in_order(root.left):
                yield val
            yield root.data
            for val in self.in_order(root.right):
                yield val

    def post_order(self, root):
        """Return val of tree post-order traversal one at a time."""
        if root is not None:
            for val in self.post_order(root.left):
                yield val
            for val in self.post_order(root.right):
                yield val
            yield root.data

    def pre_order(self, root):
        """Return val of tree pre-order traversal one at a time."""
        if root is not None:
            yield root.data
            for val in self.pre_order(root.left):
                yield val
            for val in self.pre_order(root.right):
                yield val

if __name__ == '__main__':  # pragma: no cover
    b = BinarySearchTree(20)  # balanced tree depth 3
    b.insert(10)
    b.insert(5)
    b.insert(15)
    b.insert(3)
    b.insert(7)
    b.insert(13)
    b.insert(17)
    b.insert(30)
    b.insert(25)
    b.insert(23)
    b.insert(27)
    b.insert(35)
    b.insert(37)
    b.insert(33)

    a = BinarySearchTree(0)  # all right node tree
    for num in range(1, 15):
        a.insert(num)

    t_s = timeit.timeit('b.search(30) ', setup='from __main__ import b')
    print('shortest search time for my unbalanced tree of size 15 is ' + str(t_s) + ' seconds')
    t_l = timeit.timeit('a.search(14)', setup='from __main__ import a')
    print('longest search time for my unbalanced tree of size 15 is ' + str(t_l) + ' seconds')

