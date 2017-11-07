"""Test for Graph_1."""
import pytest
from graph_1 import Graph


@pytest.fixture(scope='function')
def graph_1():
    """Making one mt priority queue instance per test."""
    return Graph()


@pytest.fixture(scope='function')
def graph_5():
    """Making one priority queue instance with len of 5 per test."""
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(5, 6)
    return g


def test_add_node(graph_1):
    """Test the add_node method."""
    for num in range(1, 7):
        graph_1.add_node(num)
    assert graph_1.nodes() == [1, 2, 3, 4, 5, 6]


def test_add_edge(graph_1):
    """Test adding a edge to the graph."""
    g = graph_1
    g.add_edge(1, 2)
    assert 2 in g.graph[1]


def test_del_node(graph_5):
    """Test if del node method works."""
    for num in range(1, 7):
        graph_5.del_node(num)
    assert graph_5.nodes() == []


def test_when_node_deleted_removed_from_neighbor(graph_1):
    """Test that after a node is deleted it is removed from neighbor list."""
    g = graph_1
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.del_node(1)
    assert g.edges() == []


def test_delete_node_from_empty_graph(graph_1):
    """Test key error is raised when no node to delete."""
    with pytest.raises(KeyError):
        graph_1.del_node(3)


def test_del_edges(graph_5):
    """Test if the del edge method works."""
    for num in range(1, 6):
        graph_5.del_edge(num, num + 1)
    assert all([graph_5.graph[num] == [] for num in graph_5.graph])


def test_has_node(graph_5):
    """Test if the has_node method works."""
    for num in range(1, 6):
        assert graph_5.has_node(num)


def test_nodes(graph_1):
    """Test if the node method works."""
    graph_1.add_node(200)
    graph_1.add_node(300)
    assert graph_1.nodes() == [200, 300]


def test_edges(graph_5):
    """Test if the edges method works."""
    assert graph_5.edges() == [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]


def test_neighbors(graph_5):
    """Test if the neighbors methods works."""
    assert graph_5.neighbors(1) == [2]


def test_adjacent(graph_5):
    """Test if the adjacent method works."""
    assert graph_5.adjacent(1, 2)
