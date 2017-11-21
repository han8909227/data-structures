"""Test for bst class."""
import pytest
from bst import BinarySearchTree
from bst import Node


@pytest.fixture(scope='function')
def bst():
    """Making one empty BinarySearchTree instance per test."""
    return BinarySearchTree(10)


@pytest.fixture(scope='function')
def bst_2():
    """Making one BinarySearchTree instance, full tree depth 2."""
    bst = BinarySearchTree(10)
    bst.insert(8)
    bst.insert(7)
    bst.insert(9)
    bst.insert(12)
    bst.insert(11)
    bst.insert(13)
    return bst


def test_init_bst_with_no_root():
    """Test init with no root."""
    new_bst = BinarySearchTree()
    assert new_bst.root is None


def test_init_bst_with_root(bst):
    """Test the insert method."""
    assert isinstance(bst.root, Node)


def test_init_bst_with_root_can_be_accessed(bst):
    """Test if we can access the root value."""
    assert bst.root.data == 10


def test_init_with_non_numeric():
    """Test if value error gets raised with non numeric root."""
    with pytest.raises(ValueError):
        BinarySearchTree('root')


def test_insertion_to_left_of_tree_works(bst):
    """Test if we can insert to left of the tree."""
    bst.insert(5)
    assert isinstance(bst.root.left, Node)
    assert bst.root.left.data == 5


def test_insertion_to_right_of_tree_works(bst):
    """Test if we can insert to right of the tree."""
    bst.insert(15)
    assert isinstance(bst.root.right, Node)
    assert bst.root.right.data == 15


def test_insert_non_numeric(bst):
    """Test if value error gets raised with non numeric root."""
    with pytest.raises(ValueError):
        bst.insert('value')


def test_search_on_empty_bst():
    """Test if searching a val from mt tree returns None."""
    new_bst = BinarySearchTree()
    assert new_bst.search(10) is None


def test_search_on_single_depth_bst(bst):
    """Test if searching a val from single depth tree returns node with the val."""
    result = bst.search(10)
    assert isinstance(result, Node)
    assert result.data == 10


def test_search_on_four_deep_bst(bst_2):
    """Test if searching a val from two deep tree returns node with the val."""
    result = bst_2.search(12)
    assert isinstance(result, Node)
    assert result.data == 12


def test_searching_invalid_on_single_depth_bst(bst):
    """Test if searching val from single depth."""
    with pytest.raises(ValueError):
        bst.search('non_exist_val')


# def test_add_edge(graph_1):
#     """Test adding a edge to the graph."""
#     g = graph_1
#     g.add_edge(1, 2)
#     assert 2 in g.graph[1]


# def test_del_node(graph_5):
#     """Test if del node method works."""
#     for num in range(1, 7):
#         graph_5.del_node(num)
#     assert graph_5.nodes() == []


# def test_when_node_deleted_removed_from_edges(graph_1):
#     """Test that after a node is deleted it is removed from edges list."""
#     g = graph_1
#     g.add_edge(1, 2)
#     g.add_edge(1, 3)
#     g.del_node(1)
#     assert g.edges() == [(2, {}), (3, {})]
