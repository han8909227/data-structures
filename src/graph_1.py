"""Graph_1 data strcture."""


class Graph:
    """Directive graph."""

    def __init__(self):
        """Create a instance of the priority class."""
        self.graph = {}

    def add_node(self, *argv):
        """Add a new node with value: data."""
        for data in argv:
            try:
                self.graph[data]
            except KeyError:
                self.graph[data] = []

    def add_edge(self, data_1, data_2):
        """Add a new edge between 2 nodes."""
        self.add_node(data_1, data_2)
        self.graph[data_1].append(data_2)

    def del_node(self, data):
        """Delete a particular node from the graph."""
        try:
            del self.graph[data]
        except KeyError:
            raise KeyError('no such node exists')

    def del_edge(self, data_1, data_2):
        """."""
        try:
            self.graph[data_1],
            self.graph[data_2]
        except KeyError:
            raise KeyError('no such nodes exists')

        for edge in self.graph[data_1]:
            if data_2 == edge:
                return self.graph[data_1].remove(edge)
        raise KeyError('no such edge exists')

    def has_node(self, data):
        """."""
        return data in self.graph

    def nodes(self):
        """Return a list of all nodes in the graph."""
        return list(self.graph.keys())

    def edges(self):
        """Return a list of tuples showing the relations."""
        result = []
        for node, edges in self.graph.items():
            for edge in edges:
                result.append((node, edge))
        return result

    def neighbors(self, data):
        """Return all the nodes the data is pointing to."""
        try:
            return self.graph[data]
        except KeyError:
            raise KeyError('no such node exists')

    def adjacent(self, data_1, data_2):
        """Return all adjacent nodes."""
        try:
            for edge in self.graph[data_1]:
                if data_2 == edge:
                    return True
            for edge in self.graph[data_2]:
                if data_1 == edge:
                    return True
            return False
        except KeyError as err:
            raise KeyError('node ' + str(err.args[0]) + ' does not exist')

