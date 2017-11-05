"""Priority Queue data strcture."""


class Graph:
    """Directive graph."""
    def __init__(self, value=None, pri=0):
        """Create a instance of the priority class."""
        self.q = {}




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
