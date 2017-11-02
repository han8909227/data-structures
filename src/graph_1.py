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
        edges = []
        for edge in self.graph.values():
            if edge != []:
                edges.append(edge)
        return edges

    def neighbors(self, data):
        """."""
        for node in self.graph:
            for

"""
g.nodes(): return a list of all nodes in the graph
g.edges(): return a list of all edges in the graph
g.add_node(val): adds a new node with value ‘n’ to the graph
g.add_edge(val1, val2): adds a new edge to the graph connecting the node containing ‘val1’ and the node containing ‘val2’. If either val1 or val2 are not already present in the graph, they should be added. If an edge already exists, overwrite it.
g.del_node(val): deletes the node containing ‘val’ from the graph; raises an error if no such node exists
g.del_edge(val1, val2): deletes the edge connecting ‘val1’ and ‘val2’ from the graph; raises an error if no such edge exists
g.has_node(val): True if node containing ‘val’ is contained in the graph, False if not.
g.neighbors(val): returns the list of all nodes connected to the node containing ‘val’ by edges; raises an error if val is not in g
g.adjacent(val1, val2): returns True if there is an edge connecting val1 and val2, False if not; raises an error if either of the supplied values are not in g
