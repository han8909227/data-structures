"""Binheap data structure."""


class Binheap(object):
    """Binheap class."""

    def __init__(self, iterable=None):
        """Will init a new instance of the Binheap class."""
        self.list = [None]
        self.size = 0

    def push(self, data):
        """Will push a value into the Binheap class."""
        self.list.append(data)
        self.size += 1
        self._perc_up(self.size)

    def _swap(self, last, parent):
        """."""
        self.list[last], self.list[parent] = self.list[parent], self.list[last]

    def _perc_up(self, i):
        """."""
        while i // 2 > 0:
            if self.list[i] < self.list[i // 2]:
                tmp = self.list[i // 2]
                self.list[i // 2] = self.list[i]
                self.list[i] = tmp
            i = i // 2
