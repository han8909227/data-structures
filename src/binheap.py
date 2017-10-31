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

    def _perc_down(self, i):
        """."""
        while (i * 2) <= self.size:
            min_child = self._min_child(i)
            if self.list[i] > self.list[min_child]:
                temp = self.list[i]
                self.list[i] = self.list[min_child]
                self.list[min_child] = temp
            i = min_child

    def _min_child(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.list[i * 2] < self.list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def pop(self):
        """."""
        if self.size == 0:
            raise IndexError
        root_val = self.list[1]
        self.list[1] = self.list[self.size]
        self.size = self.size - 1
        self.list.pop()
        self._perc_down(1)
        return root_val