"""Priority Queue data strcture."""


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
        """."""
        try:
            del self.graph[data]
        except KeyError:
            raise KeyError('no such node exists')

    def del_edge(self, data_1, data_2):
        """."""
        for edge in self.graph[data_1]:
            if data_2 == edge:
                return edge.remove(edge)
        raise KeyError('no such edge exists')

    def has_node(self, data):
        """."""
        for key in self.graph:
            if key == data:
                return True
        return False

    def nodes(self):
        """Return a list of all nodes in the graph."""
        nodes = []
        for node in self.graph:
            nodes.append(node)
        return nodes

    def edges(self):
        """."""
        edges = []
        for edge in self.graph.values():
            if edge != []:
                edges.append(edge)
        return edges

    def neighbors(self, data):
        """."""
        try:
            return self.graph[data]
        except KeyError:
            raise KeyError('no such node exists')

    def adjacent(self, data_1, data_2):
        """."""
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

