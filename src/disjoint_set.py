"""
Disjoint set data structure.
Disjoint Set data structure (Union–Find), is a data structure that keeps track of a
set of elements partitioned into a number of disjoint (nonoverlapping) subsets.
"""


class DisjointSet(object):
    """Disjoint set class."""

    def __init__(self, iterable=None):
        """Init disjoint set."""
        self._sets = []
        if not all(isinstance(val, (int, float)) for val in iterable):
            raise ValueError('all items in list must be a number')
        for val in iterable:
            self._sets.append([val])

    def _find_index(self, val):
        for item in self._sets:
            if val in item:
                return self._sets.index(item)
        return None

    def find(self, val):
        """Find set a val belongs to."""
        for item in self._sets:
            if val in item:
                return self._sets[self._sets.index(item)]
        return None

    def union(self, val_1, val_2):
        """Union two val, putting into one subset."""
        index_1 = self._find_index(val_1)
        index_2 = self._find_index(val_2)
        if index_1 != index_2 and index_1 is not None and index_2 is not None:
            self._sets[index_2] = self._sets[index_2] + self._sets[index_1]
            del self._sets[index_1]
        return self._sets

    def get(self):
        """Return the current sets."""
        return self._sets
