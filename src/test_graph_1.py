"""Test for Graph_1."""
import pytest
from graph_1 import Graph


@pytest.fixture(scope='function')
def graph_1():
    """Making one empty graph instance per test."""
    return Graph()


@pytest.fixture(scope='function')
def graph_5():
    """Making one graph instance with len of 5 per test."""
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(5, 6)
    return g


@pytest.fixture()
def t_graph():
    """Make a graph for traversal and weights."""
    g = Graph()
    g.add_edge(1, 2, 5)
    g.add_edge(1, 3, 9)
    g.add_edge(2, 4, 4)
    g.add_edge(2, 5, 2)
    g.add_edge(3, 6, 1)
    g.add_edge(3, 7)
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


def test_when_node_deleted_removed_from_edges(graph_1):
    """Test that after a node is deleted it is removed from edges list."""
    g = graph_1
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.del_node(1)
    assert g.edges() == []


def test_delete_node_from_empty_graph(graph_1):
    """Test key error is raised when no node to delete."""
    with pytest.raises(ValueError):
        graph_1.del_node(3)


def test_del_edges(graph_1):
    """Test if the del edge method works."""
    graph_1.add_edge(1, 2)
    graph_1.add_edge(1, 3)
    graph_1.del_edge(1, 3)
    assert graph_1.edges() == [(1, 2, 0)]


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
    result = [(1, 2, 0), (2, 3, 0), (3, 4, 0), (4, 5, 0), (5, 6, 0)]
    assert graph_5.edges() == result


def test_del_edge_with_val_not_in_graph(graph_5):
    """Test if we can del node not in the graph."""
    with pytest.raises(ValueError):
        graph_5.del_edge(100, 200)


def test_del_edge_from_no_edge_nodes(graph_5):
    """Test if can delete an edge that doesn't exist."""
    with pytest.raises(ValueError):
        graph_5.del_edge(1, 6)


def test_neighbors(graph_5):
    """Test if the neighbors methods works."""
    assert graph_5.neighbors(1) == {2: 0}


def test_adjacent(graph_5):
    """Test if the adjacent method works."""
    assert graph_5.adjacent(1, 2)


def test_adjacent_method_on_not_error(graph_5):
    """Test if key error gets raised if val not in graph."""
    with pytest.raises(ValueError):
        graph_5.adjacent(200, 300)


def test_bft_no_node_exist(graph_1):
    """Test bft for key error when node doesn't exist."""
    with pytest.raises(ValueError):
        graph_1.breadth_first_traversal(3)


def test_dft_no_node_exist(graph_1):
    """Test dft for key error when node doesn't exist."""
    with pytest.raises(ValueError):
        graph_1.depth_first_traversal(3)


def test_bft_returns_proper_path(t_graph):
    """Test bft returns proper path with unique neighbors from start point of 1."""
    result = [1, 2, 3, 4, 5, 6, 7]
    assert t_graph.breadth_first_traversal(1) == result


def test_bft_returns_proper_path_after_deleting_edge(t_graph):
    """Test bft returns proper path with unique neighbors after deleting edge starting at 1."""
    t_graph.del_edge(1, 3)
    result = [1, 2, 4, 5]
    assert t_graph.breadth_first_traversal(1) == result


def test_bft_returns_proper_path_after_deleting_node(t_graph):
    """Test bft returns proper path with unique neighbors after deleting node starting at 1."""
    t_graph.del_node(5)
    result = [1, 2, 3, 4, 6, 7]
    assert t_graph.breadth_first_traversal(1) == result


def test_bft_returns_proper_path_without_repeating_nodes(t_graph):
    """Test bft returns proper path with non unique neighbors from start point of 1."""
    t_graph.add_edge(7, 1)
    result = [1, 2, 3, 4, 5, 6, 7]
    assert t_graph.breadth_first_traversal(1) == result


def test_bft_returns_only_start_if_no_neighbors(t_graph):
    """Test that only the start node is returned when no neighbors."""
    t_graph.add_node(9)
    assert t_graph.breadth_first_traversal(9) == [9]


def test_dft_returns_proper_path(t_graph):
    """Test dft returns proper path with unique neighbors starting at 1."""
    result = [1, 2, 4, 5, 3, 6, 7]
    assert t_graph.depth_first_traversal(1) == result


def test_dft_returns_proper_path_without_repeating_nodes(t_graph):
    """Test dft returns proper path with non unique neighbors from start point of 1."""
    t_graph.add_edge(7, 1)
    result = [1, 2, 4, 5, 3, 6, 7]
    assert t_graph.depth_first_traversal(1) == result


def test_dft_returns_only_start_if_no_neighbors(t_graph):
    """Test that only the start node is returned when no neighbors."""
    t_graph.add_node(9)
    assert t_graph.depth_first_traversal(9) == [9]


def test_dft_returns_proper_path_after_deleting_edge(t_graph):
    """Test dft returns proper path with unique neighbors after deleting edge starting at 1."""
    t_graph.del_edge(1, 3)
    result = [1, 2, 4, 5]
    assert t_graph.depth_first_traversal(1) == result


def test_dft_returns_proper_path_after_deleting_node(t_graph):
    """Test dft returns proper path with unique neighbors after deleting node starting at 1."""
    t_graph.del_node(5)
    result = [1, 2, 4, 3, 6, 7]
    assert t_graph.depth_first_traversal(1) == result


def test_non_int_entered_for_weight(graph_1):
    """Test that value error is raised when A is weight."""
    with pytest.raises(ValueError):
        graph_1.add_edge(1, 2, 'A')


def test_non_int_entered_for_weight_next(graph_1):
    """Test that value error is raised when A is weight."""
    with pytest.raises(ValueError):
        graph_1.add_edge(1, 2, '&')


def test_wieght_defaults_to_zero(graph_1):
    """Test that the defalut wieght is applied to edge."""
    graph_1.add_edge(1, 2)
    assert graph_1.edges() == [(1, 2, 0)]


def test_added_weight_displayed(graph_1):
    """Test weight is added to edge."""
    graph_1.add_edge(1, 2, 10)
    assert graph_1.edges() == [(1, 2, 10)]


def test_weight_removed_when_edge_deleted(graph_1):
    """Test that weight is removed after deleting edge."""
    graph_1.add_edge(1, 2, 9)
    graph_1.del_edge(1, 2)
    assert graph_1.edges() == []


def test_weight_removed_when_node_deleted(graph_1):
    """Test that weight is removed after deleting node."""
    graph_1.add_edge(1, 2, 9)
    graph_1.add_edge(1, 3, 6)
    graph_1.del_node(1)
    assert graph_1.edges() == []


# def test_dijkstra_with_wrong_node(t_graph):
#     """Test dijkstra work properly."""
#     with pytest.raises(ValueError):
#         t_graph.sp_dijkstra(1, 100)


# def test_bellman_ford_with_wrong_node(t_graph):
#     """Test bellman_ford work properly."""
#     with pytest.raises(ValueError):
#         t_graph.sp_bellman_ford(1, 100)


# def test_dijkstra_find_path(t_graph):
#     """Test dijkstra work properly."""
#     path = t_graph.sp_dijkstra(1, 4)
#     assert path == 9


# def test_bellman_ford_find_path(t_graph):
#     """Test bellman_ford work properly."""
#     path = t_graph.sp_bellman_ford(1, 4)
#     assert path == 9


# def test_dijkstra_find_path_1(t_graph):
#     """Test dijkstra work properly."""
#     path = t_graph.sp_dijkstra(1, 6)
#     assert path == 10


# def test_bellman_ford_find_path_1(t_graph):
#     """Test bellman_ford work properly."""
#     path = t_graph.sp_bellman_ford(1, 6)
#     assert path == 10


# def test_dijkstra_find_path_self(t_graph):
#     """Test dijkstra work properly."""
#     path = t_graph.sp_dijkstra(1, 1)
#     assert path == 0


# def test_bellman_ford_find_path_self(t_graph):
#     """Test bellman_ford work properly."""
#     path = t_graph.sp_bellman_ford(1, 1)
#     assert path == 0


