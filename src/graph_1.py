"""Graph_1 data strcture."""
from numbers import Number
from priorityq import Priorityq


class Graph:
    """Directive graph."""

    def __init__(self):
        """Create a instance of the graph class."""
        self.graph = {}

    def add_node(self, *argv):
        """Add a new node with value: data."""
        for data in argv:
            self.graph.setdefault(data, {})

    def add_edge(self, data_1, data_2, weight=0):
        """Add a new edge between 2 nodes, creates nodes if not present."""
        if not isinstance(weight, Number):
            raise ValueError('Weight needs to be a number')
        self.add_node(data_1, data_2)
        self.graph[data_1][data_2] = weight

    def del_node(self, data):
        """Delete a particular node from the graph."""
        try:
            del self.graph[data]
            for key in self.graph:
                if data in self.graph[key]:
                    del self.graph[key][data]
        except KeyError:
            raise ValueError('no such node exists')

    def del_edge(self, data_1, data_2):
        """Delete a edge between data_1 and data_2."""
        if not self.has_node(data_1) or not self.has_node(data_2):
            raise ValueError('node(s) must exist in the graph')
        for edge in self.graph[data_1]:
            if data_2 == edge:
                del self.graph[data_1][data_2]
                return
        raise ValueError('no such edge exist')

    def has_node(self, data):
        """Check if node is in graph."""
        return data in self.graph

    def nodes(self):
        """Return a list of all nodes in the graph."""
        return list(self.graph.keys())

    def edges(self):
        """Return a list of tuples showing the relations."""
        return list(self.graph.items())

    def neighbors(self, data):
        """Return all the nodes the data is pointing to."""
        try:
            return self.graph[data]
        except KeyError:
            raise ValueError('no such node exists')

    def adjacent(self, data_1, data_2):
        """Return all adjacent nodes."""
        if not self.has_node(data_1) or not self.has_node(data_2):
            raise ValueError('node does not exist')
        return data_2 in self.graph[data_1] or data_1 in self.graph[data_2]

    def breadth_first_traversal(self, start):
        """Return all value from the start using breadth first traversal."""
        result = []
        que = [start]
        repeat = set()
        if not self.has_node(start):
            raise ValueError('no such node in the graph')
        while que:
            pop = que.pop(0)
            edges = self.neighbors(pop)
            result.append(pop)
            repeat.add(pop)
            for edge in edges:
                if edge not in repeat:
                    que.append(edge)
        return result

    def depth_first_traversal(self, start):
        """Return all values from start using depth first traversal."""
        que = [start]
        result = []
        if not self.has_node(start):
            raise ValueError('no such node in the graph')
        while que:
            node = que.pop(0)
            if node not in result:
                result.append(node)
                que = [key for key in self.graph[node]] + que
        return result

    def sp_dijkstra(self, start, end=None):
        """Return shortest path using dijkstra alogorithem."""
        visited = set()
        dist = {}
        for node in self.nodes():
            dist[node] = float("inf")
        dist[start] = 0
        current = start

        while current != end:
            neighbors = self.neighbors(current)
            for neighbor in neighbors:
                dist_curr_to_neigh = self.graph[current][neighbor]
                if dist[neighbor] > (dist[current] + dist_curr_to_neigh):
                    dist[neighbor] = (dist[current] + dist_curr_to_neigh)
            visited.add(current)
            min_dist = float("inf")
            for key in dist:
                if key not in visited:
                    if dist[key] < min_dist:
                        min_dist = dist[key]
                        min_key = key
            current = min_key
        return dist[end]

    # def sp_bellmanford(self, start, end=None):
    #     """Return the shortest path value using bellmanford."""
    #     dist = {}
    #     for node in self.nodes():
    #         dist[node] = float("inf")
    #     dist[start] = 0
    #     for _ in range(len(self.nodes()) - 1):
    #         for u, v, w in self.edges():
    #             if dist[u] != float("inf") and (dist[u] + w) < dist[v]:
    #                 dist[v] = dist[u] + w
    #     for u, v, w in self.edges():
    #         if dist[u] + w < dist[v]:
    #             raise ValueError("negative weight in graph.")
    #     return dist[end]


if __name__ == '__main__':  # pragma: no cover
    g = Graph()
    g.add_edge('A', 'B', 2)
    g.add_edge('A', 'C', 3)
    g.add_edge('B', 'D', 3)
    g.add_edge('B', 'E', 1)
    g.add_edge('C', 'F', 2)
    g.add_edge('C', 'G', 8)
    g.add_edge('D', 'H', 6)
    g.add_edge('D', 'C', 4)
    g.add_edge('H', 'A', 1)
    g.add_edge('F', 'D', 2)

    print('Graph structure: ' + str(g.graph))
    print('List of edges: ' + str(g.edges()))
    print('Path using breadth_first_traversal starting at A:' + str(g.breadth_first_traversal('A')))
    print('Path using depth_first_traversal starting at A:' + str(g.depth_first_traversal('A')))

