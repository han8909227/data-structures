"""Graph_1 data strcture."""


class Graph:
    """Directive graph."""

    def __init__(self):
        """Create a instance of the graph class."""
        self.graph = {}

    def add_node(self, *argv):
        """Add a new node with value: data."""
        for data in argv:
            self.graph.setdefault(data, [])

    def add_edge(self, data_1, data_2):
        """Add a new edge between 2 nodes, creates nodes if not present."""
        self.add_node(data_1, data_2)
        self.graph[data_1].append(data_2)

    def del_node(self, data):
        """Delete a particular node from the graph."""
        try:
            del self.graph[data]
            for key in self.graph:
                if data in self.graph[key]:
                    self.graph[key].remove(data)
        except KeyError:
            raise ValueError('no such node exists')

    def del_edge(self, data_1, data_2):
        """Delete a edge between data_1 and data_2."""
        if data_1 not in self.graph:
            raise ValueError('node ' + str(data_1) + ' does not exist')
        if data_2 not in self.graph:
            raise ValueError('node ' + str(data_2) + ' does not exist')
        for edge in self.graph[data_1]:
            if data_2 == edge:
                return self.graph[data_1].remove(edge)
        raise ValueError('no such edge exists')

    def has_node(self, data):
        """Check if node is in graph."""
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
            raise ValueError('no such node exists')

    def adjacent(self, data_1, data_2):
        """Check that two nodes are adjacent."""
        if data_2 in self.graph:
            try:
                return data_2 in self.graph[data_1]
            except KeyError as err:
                raise ValueError('node ' + str(err.args[0]) + ' does not exist')
        else:
            raise ValueError('node ' + str(data_2) + ' does not exist')
