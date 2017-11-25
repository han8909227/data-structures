"""Graph_1 data strcture."""
from numbers import Number


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
            raise KeyError('no such node exists')

    def del_edge(self, data_1, data_2):
        """Delete a edge between data_1 and data_2."""
        for edge in self.graph[data_1]:
            if data_2 == edge:
                del self.graph[data_1][data_2]
                return
        raise KeyError('no such edge exists')

    def has_node(self, data):
        """Check if node is in graph."""
        return data in self.graph

    def nodes(self):
        """Return a list of all nodes in the graph."""
        return list(self.graph.keys())

    def edges(self):
        """Return node, edge, weight relation in a tuple."""
        result = []
        for node in self.graph:
            for edge in self.graph[node]:
                result.append((node, edge, self.graph[node][edge]))
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
        repeat = set()
        if not self.has_node(start):
            raise KeyError('no such node in the graph')
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
            raise KeyError('no such node in the graph')
        while que:
            node = que.pop(0)
            if node not in result:
                result.append(node)
                que = [key for key in self.graph[node]] + que
        return result

    def sp_dijkstra(self, start, end):
        """Return shortest path using dijkstra."""
        visited = set()
        dist = {}
        for node in self.nodes():
            dist[node] = float("inf")
        dist[start] = 0
        curr = start
        min_path = [start]
        min_dist = float("inf")
        if start not in self.graph or end not in self.graph:
            raise ValueError('no such node exist')
        while curr != end:
            neighbors = self.neighbors(curr)

            for neighbor in neighbors:
                dist_curr_to_neigh = self.graph[curr][neighbor]
                if dist[neighbor] > (dist[curr] + dist_curr_to_neigh):
                    dist[neighbor] = (dist[curr] + dist_curr_to_neigh)
            visited.add(curr)
            for key in dist:
                if key not in visited:
                    if dist[key] < min_dist:
                        min_dist = dist[key]
                        min_key = key
            curr = min_key
            if curr is not None:
                min_path.append(curr)
        return list(min_path)

    def sp_bellman_ford(self, start, end):
            """Return shortest path using bellman ford."""
            if start not in self.graph or end not in self.graph:
                raise ValueError('no such node exist')
            if start == end:
                return [start]

            prev = {n: None for n in self.graph}
            dist = {n: float('inf') for n in self.graph}
            dist[start] = 0

            for _ in range(len(self.graph) - 1):
                for edge_start, edge_end, weight in self.edges():
                    if dist[edge_end] > dist[edge_start] + weight:
                        dist[edge_end] = dist[edge_start] + weight
                        prev[edge_end] = edge_start

            min_path = []
            curr = end
            if prev[curr] is None:
                raise ValueError('no path between these nodes')
            while curr is not None:
                min_path.append(curr)
                curr = prev[curr]
            return list(reversed(min_path))

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

