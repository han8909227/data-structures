"""Binheap data structure."""


class Binheap(object):
    """Binheap class for min heap."""

    def __init__(self, iterable=None):
        """Will init a new instance of the min heap."""
        self.list = [None]
        self.size = 0

    def push(self, data):
        """Will push a value into the Binheap class."""
        self.list.append(data)
        self.size += 1
        self._perc_up(self.size)

    def _swap(self, a, b):
        """Swap function for swapping parent and child(internal use)."""
        self.list[a], self.list[b] = self.list[b], self.list[a]

    def _perc_up(self, i):
        """Bubble up the heap."""
        while i // 2 > 0:
            if self.list[i] < self.list[i // 2]:
                tmp = self.list[i // 2]
                self.list[i // 2] = self.list[i]
                self.list[i] = tmp
            i = i // 2

    def _perc_down(self, i):
        """Bubble down the heap."""
        while (i * 2) <= self.size:
            min_child = self._min_child(i)
            if self.list[i] > self.list[min_child]:
                temp = self.list[i]
                self.list[i] = self.list[min_child]
                self.list[min_child] = temp
            i = min_child

    def _min_child(self, i):
        """Find the min child amount all children."""
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.list[i * 2] < self.list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def pop(self):
        """Pop from the heap."""
        if self.size == 0:
            raise IndexError
        root_val = self.list[1]
        self.list[1] = self.list[self.size]
        self.size -= 1
        self.list.pop()
        self._perc_down(1)
        return root_val
