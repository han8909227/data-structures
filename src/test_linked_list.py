"""Tests for the mailroom module."""
import pytest
from linked_list import LinkedList
from linked_list import Node


def test_noe_and_ll_class_init():
    """Test the instance is initialized."""
    t = LinkedList()
    n = Node()
    assert not n.data
    assert hasattr(n, 'get_next')
    assert isinstance(t, LinkedList)
    assert t.head is None


display_test = [('20', '(0, 2, )'), ('wo', '(o, w, )'), ([1, 2], '(2, 1, )'), ('hi', ('(i, h, )'))]


@pytest.mark.parametrize('head, result', display_test)
def test_display(head, result):
    """Test display method."""
    a = LinkedList(head)
    assert a.display() == result

s_1 = LinkedList()


@pytest.mark.parametrize('n', range(1, 51))
def test_insert(n):
    """Test insert method."""
    s_1.insert(str(n))
    assert s_1.head.data == str(n)
    assert s_1.size() == n


@pytest.mark.parametrize('n', range(50))
def test_size(n):
    """Test size method."""
    l = LinkedList()
    for num in range(n):
        l.insert(num)
    assert l.size() == n
    assert hasattr(l, 'size')
    assert len(l) == n


@pytest.mark.parametrize('n, search, exist', [(10, 5, True), (5, 6, False), (100, 888, False), (8, -2, False), (20, 10, True)])
def test_search(n, search, exist):
    """Test search method."""
    s_2 = LinkedList()
    for num in range(n):
        s_2.insert(num)
    assert hasattr(s_2, 'search')
    try:
        assert s_2.search(search) == search
    except ValueError:
        if not exist:
            pass


@pytest.mark.parametrize('n', [num ** 2 for num in range(10)])
def test_pop(n):
    """Test pop method."""
    s_3 = LinkedList()

    try:
        for num in range(n):
            s_3.insert(num)
        for i in range(n):
            pop = s_3.pop()
            assert type(pop) == int
    except AttributeError:
        if s_3.head is None:
            pass


@pytest.mark.parametrize('n', [i ** 2 for i in range(10)])
def test_delete(n):
    """Test delete method."""
    s_4 = LinkedList()
    for num in range(n):
        s_4.insert(num)
    for num in range(n):
        assert s_4.search(num) == num
        s_4.delete(num)
    assert s_4.size() == 0
