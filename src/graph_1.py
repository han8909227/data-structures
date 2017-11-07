"""Graph_1 data strcture."""
import sys


class Graph:
    """Directive graph."""

    def __init__(self):
        """Create a instance of the graph class."""
        self.graph = {}
        self.result = []

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
            raise KeyError('no such node exists')

    def del_edge(self, data_1, data_2):
        """Delete a edge between data_1 and data_2."""
        for edge in self.graph[data_1]:
            if data_2 == edge:
                return self.graph[data_1].remove(edge)
        raise KeyError('no such edge exists')

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
            raise KeyError('no such node exists')

    def adjacent(self, data_1, data_2):
        """Return all adjacent nodes."""
        try:
            return data_2 in self.graph[data_1] or data_1 in self.graph[data_2]
        except KeyError as err:
            raise KeyError('node ' + str(err.args[0]) + ' does not exist')

    def breadth_first_traversal(self, start):
        """Return all value from the start using breadth first traversal."""
        result = []
        que = [start]
        node = start
        if self.has_node(node):
            while len(que):
                edges = self.neighbors(node)
                for edge in edges:
                    if edge in result or edge in que:
                        edges.remove(edge)
                result.append(que.pop(0))
                for edge in edges:
                    que.append(edge)
                if len(que):
                    node = que[0]
            return result
        else:
            raise KeyError('no such node in the graph')

    def depth_first_traversal(self, start):
        """."""
        que = [start]
        result = []
        while que:
            node = que.pop(0)
            if node not in result:
                result.append(node)
                que = self.graph[node] + que
        return result


if __name__ == '__main__':
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')
    g.add_edge('C', 'G')
    g.add_edge('D', 'H')
    g.add_edge('D', 'C')
    g.add_edge('H', 'A')
    g.add_edge('F', 'D')

    print('Graph structure: ' + str(g.graph))
    print('List of edges: ' + str(g.edges()))
    print('Path using breadth_first_traversal starting at A:' + str(g.breadth_first_traversal('A')))
    print('Path using depth_first_traversal starting at A:' + str(g.depth_first_traversal('A')))

