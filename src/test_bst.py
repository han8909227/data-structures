"""Test for bst class."""
import pytest
from bst import BinarySearchTree
from bst import Node
from types import GeneratorType


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


def test_insert_duplicate_vals():
    """Test if we can insert duplicate value into the tree."""
    bst = BinarySearchTree()
    bst.insert(15)
    bst.insert(15)
    bst.insert(15)
    assert bst.size() == 1


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


def test_search_on_twp_deep_bst(bst_2):
    """Test if searching a val from two deep tree returns node with the val."""
    result = bst_2.search(12)
    assert isinstance(result, Node)
    assert result.data == 12


def test_searching_invalid_on_two_deep_bst(bst_2):
    """Test if searching val not in tree from a two deep bst return None."""
    result = bst_2.search(200)
    assert result is None


def test_size_method_on_mt_bst():
    """Test if the size method works on mt bst."""
    new_bst = BinarySearchTree()
    assert new_bst.size() == 0


def test_size_method_on_populated_bst(bst_2):
    """Test if the size method works on a populated bst."""
    assert bst_2.size() == 7


def test_size_method_on_root_only_bst(bst):
    """Test if the size method works on a bst with only the root."""
    assert bst.size() == 1


def test_contain_method_on_populated_bst_return_true(bst_2):
    """Test if the contain method works properly, and return True for containing value."""
    for num in range(8, 14):
        assert bst_2.contains(num)


def test_contain_method_on_populated_bst_return_false(bst_2):
    """Test if the contian method returns False for non containing value."""
    assert not bst_2.contains(15)


def test_depth_method_on_mt_bst():
    """Test if the depth method return 0 on mt bst from root."""
    new_bst = BinarySearchTree()
    assert new_bst.depth(new_bst.root) == 0


def test_depth_method_on_single_depth_bst(bst):
    """Test if the depth method return 0 on single level bst."""
    assert bst.depth(bst.root) == 0


def test_depth_method_on_populated_bst(bst_2):
    """Test if the depth method return correct depth."""
    assert bst_2.depth(bst_2.root) == 2


def test_balance_method_on_balanced_bst(bst_2):
    """Test the balance method on a balanced bst."""
    assert bst_2.balance() == 0


def test_balance_method_on_mt_bst():
    """Test the balane method on a mt bst."""
    new_bst = BinarySearchTree()
    assert new_bst.balance() == 0


def test_balance_method_on_neg_balance():
    """Test the balance method on a negatively balanced bst."""
    new_bst = BinarySearchTree(10)
    new_bst.insert(20)
    new_bst.insert(30)
    assert new_bst.balance() == -2


def test_balance_method_on_neg_balance_with_two_sides():
    """Test the balance method on a negatively balanced bst."""
    new_bst = BinarySearchTree(10)
    new_bst.insert(20)
    new_bst.insert(30)
    new_bst.insert(0)
    assert new_bst.balance() == -1


def test_balance_method_on_pos_balance():
    """Test the balance method on a positively balanced bst."""
    new_bst = BinarySearchTree(10)
    new_bst.insert(0)
    new_bst.insert(-10)
    new_bst.insert(-20)
    assert new_bst.balance() == 3


def test_balance_method_on_pos_balance_with_two_sides():
    """Test the balance method on a positively balanced bst."""
    new_bst = BinarySearchTree(10)
    new_bst.insert(0)
    new_bst.insert(-10)
    new_bst.insert(-20)
    new_bst.insert(20)
    assert new_bst.balance() == 2


def test_in_order_forms_generator_obj(bst_2):
    """Test if the method returns a generator obj."""
    a = bst_2.in_order(bst_2.root)
    assert isinstance(a, GeneratorType)


def test_post_order_forms_generator_obj(bst_2):
    """Test if the method returns a generator obj."""
    a = bst_2.post_order(bst_2.root)
    assert isinstance(a, GeneratorType)


def test_pre_order_forms_generator_obj(bst_2):
    """Test if the method returns a generator obj."""
    a = bst_2.pre_order(bst_2.root)
    assert isinstance(a, GeneratorType)


def test_in_order_method(bst_2):
    """Test the in order method."""
    a = bst_2.in_order(bst_2.root)
    result = []
    for _ in range(7):
        result.append(next(a))
    assert result == [7, 8, 9, 10, 11, 12, 13]


def test_post_order_method(bst_2):
    """Test the post order method."""
    a = bst_2.post_order(bst_2.root)
    result = []
    for _ in range(7):
        result.append(next(a))
    assert result == [7, 9, 8, 11, 13, 12, 10]


def test_pre_order_method(bst_2):
    """Test the pre order method."""
    a = bst_2.pre_order(bst_2.root)
    result = []
    for _ in range(7):
        result.append(next(a))
    assert result == [10, 8, 7, 9, 12, 11, 13]


