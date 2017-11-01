"""Priority Queue data strcture."""


class Priorityq:
    """Priority Que class."""

    def __init__(self, value=None, pri=0):
        """."""
        self.q = {}

    def insert(self, data, pri=0):
        """."""
        from que_ import Queue
        if not data:
            raise ValueError('need value to push')
        try:
            self.q[pri]
        except KeyError:
            self.q[pri] = Queue()
        self.q[pri].enqueue(data)

    def pop(self):
        """."""
        if self.q == {}:
            raise ValueError('need value to pop')
        pri_to_pop = sorted(self.q.keys())[-1]
        q_pop = self.q[pri_to_pop].dequeue()
        try:
            self.q[pri_to_pop].peek()
        except AttributeError:
            del self.q[pri_to_pop]
        return q_pop
