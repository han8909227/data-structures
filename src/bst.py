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
        self.depth = 1

    def _set_child(self, child):
        """Set child to the parent(leaf node)."""
        if self.parent:
            if self.parent.left is self:
                self.parent.left = child
            else:
                self.parent.right = child

    def children(self):
        """Return all children node of the current node."""
        return [child for child in [self.right, self.left] if child]


class BinarySearchTree(object):
    """Binary search tree class."""

    def __init__(self, iterable=()):
        """Init the bst class."""
        self.root = None
        self.count = 0
        self.rotation = 0
        if isinstance(iterable, (str, list, tuple)):
            for val in iterable:
                if isinstance(val, int) or isinstance(val, float):
                    self.insert(val)
                else:
                    raise ValueError('value(s) must be a number!')
        else:
            raise ValueError('must be a list, str or tuple')

    def insert(self, item):
        """Insert a value/node into the tree."""
        if self.root is None:
            self.root = Node(item)
            self.count += 1
        elif self.search(item):
            return
        elif isinstance(item, int) or isinstance(item, float):
            curr_data = self.root
            new_node = None
            while curr_data is not None:
                if item < curr_data.data:
                    if curr_data.left is None:
                        curr_data.left = Node(item)
                        curr_data.left.parent = curr_data
                        self.count += 1
                        new_node = curr_data.left
                        return
                    else:
                        curr_data = curr_data.left
                else:  # greater than current node
                    if curr_data.right is None:
                        curr_data.right = Node(item)
                        curr_data.right.parent = curr_data
                        self.count += 1
                        new_node = curr_data.right
                        return
                    else:
                        curr_data = curr_data.right

            root = self._find_unbalanced(new_node)
            if root:
                self._rebalance(root)
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
            if target is self.root:
                self.root = None
                self.count = 0
                return
            elif item > target.parent.data:
                target.parent.right = None
            else:
                target.parent.left = None
            self.count -= 1
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
            self.count -= 1
            return
        else:
            replacer = self._delete_helper(target.right)
            target.data = replacer.data
            if replacer is target.right:
                replacer.parent.right = None
            else:
                replacer.parent.left = None
            self.count -= 1
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
        """Return the depth of the current tree (0 for root only tree as required by assignment)."""
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

    def _balance(self, node='root'):
        """Ck balance of the node to decide rotation."""
        if node == 'roto':
            node = self.root
        if node is None:
            return 0
        left_depth = self._depth(node.left)
        right_depth = self._depth(node.right)
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

    def _rotate_left(self, root):
        """Rotate left.."""
        new_root = root.right
        root.right = new_root.left
        if new_root.left:
            new_root.left.parent = root
        if root.parent is None:
            self.root = new_root
        root._set_child(new_root)
        new_root.parent = root.parent
        new_root.left = root
        root.parent = new_root
        return new_root

    def _rotate_right(self, root):
        """Rotate right."""
        new_root = root.left
        root.left = new_root.root
        if new_root.right:
            new_root.right.parent = root
        if root.parent is None:
            self.root = new_root
        root._set_child(new_root)
        new_root.right = root
        new_root.parent = root.parent
        root.parent = new_root
        return new_root

    def _rotate_lr(self, root):
        """Rotate left and right."""
        left_root = root.left
        new_root = left_root.right
        left_root.right = new_root.left
        root.left = new_root.right
        if new_root.left:
            new_root.left.parent = left_root
        if new_root.right:
            new_root.right.parent = root
        root._set_child(new_root)
        if root.parent is None:
            self.root = new_root
        new_root.parent = root.parent
        new_root.right = root
        new_root.left = left_root
        root.parent = new_root
        left_root.parent = new_root
        return new_root

    def _rotate_rl(self, root):
        """"Rotate right and left."""
        right_root = root.right
        new_root = right_root.left
        right_root.left = new_root.right
        root.right = new_root.left
        if new_root.right:
            new_root.right.parent = right_root
        if new_root.left:
            new_root.left.parent = root
        root._set_child(new_root)
        if root.parent is None:
            self.root = new_root
        new_root.parent = root.parent
        new_root.left = root
        new_root.right = right_root
        root.parent = new_root
        right_root.parent = new_root
        return new_root

    def _rebalance(self, node):
        """Rebalance the tree from self.root."""
        self.rotation += 1
        if self._balance(node) < 0:
            if self._balance(node.right) <= 0:
                root = self._rotate_left(node)
            else:
                root = self._rotate_rl(node)
        else:
            if self._balance(node.left) >= 0:
                root = self._rotate_right(node)
            else:
                root = self._rotate_lr(node)
        self._traverse_depth(root)
        next_ = self._find_unbalance(node)
        if next_:
            self._rebalance(next_)

    def _traverse_depth(self, node):
        """Traverse up to find the depth."""
        children = node.children()
        node.depth = 1
        if children:
            node.depth += max(child.depth for child in children)
        if node.parent:
            self._traverse_depth(node.parent)

    def _find_unbalanced(self, node):
        """Ck if tree is unbalanced."""
        while node:
            if abs(self.balance(node)) > 1:
                return node
            node = node.parent

if __name__ == '__main__':  # pragma: no cover
    b = BinarySearchTree([20, 10, 5, 15, 3, 7, 13, 17, 30, 25, 23, 27, 35, 37, 23])  # balanced tree depth 3

    a = BinarySearchTree()  # all right node tree
    for num in range(0, 15):
        a.insert(num)

    t_s = timeit.timeit('b.search(30) ', setup='from __main__ import b')
    print('shortest search time for my unbalanced tree of size 15 is ' + str(t_s) + ' seconds')
    t_l = timeit.timeit('a.search(14)', setup='from __main__ import a')
    print('longest search time for my unbalanced tree of size 15 is ' + str(t_l) + ' seconds')

