"""Tests for stack module."""
import pytest
from linked_list import LinkedList
from linked_list import Node

init_and_insert = [(221, 221), ('word', 'word'), ([1, 2], [1, 2]), (('hi'), ('hi'))]


@pytest.mark.parametrize('head, result', init_and_insert)
def test_noe_and_ll_class_init(head, result):
    """Test the instance is initialized."""

    t = LinkedList(head)
    n = Node(head)
    assert n.data == head
    assert hasattr(n, 'get_next')
    assert isinstance(t, LinkedList)
    assert isinstance(t.head, Node)
    assert t.head.data == result


display_test = [(221, '(221, )'), ('word', '(word, )'), ([1, 2], '([1, 2], )'), ('hi', ('(hi, )'))]


@pytest.mark.parametrize('head, result', display_test)
def test_display(head, result):
    """."""
    a = LinkedList(head)
    assert a.display() == result

starter_0 = LinkedList('pos_one')


@pytest.mark.parametrize('insert, result', init_and_insert)
def test_insert(insert, result):
    """."""
    starter_0.insert(insert)
    assert isinstance(starter_0.head, Node)
    assert starter_0.head.data == result
    assert starter_0.size() > 1


starter_1 = LinkedList('pos_one')
starter_1.insert('pos_two')
starter_1.insert('pos_three')
starter_1.insert('pos_four')
starter_1.insert('pos_five')


@pytest.mark.parametrize('n', range(50))
def test_size(n):
    """."""
    l = LinkedList()
    for num in range(n):
        l.insert(num)
    assert l.size() == n + 1
    assert hasattr(l, 'size')
    assert len(l) == n + 1


@pytest.mark.parametrize('one, two, three, search, result', [('1', 4, [33], [33], True), ('word', 33, 3, 88, False), ('po', (22), ('w'), 'pos', True)])
def test_search(one, two, three, search, result):
    """."""
    starter_2 = LinkedList(one)
    starter_2.insert(two)
    starter_2.insert(three)

    assert hasattr(starter_2, 'search')
    try:
        assert starter_2.search(search)
    except ValueError:
        if not result:
            pass


@pytest.mark.parametrize('one, two, result', [(88, '22', '(88, )'), ([22,33], 'hello', '([22, 33], )'), (99, 192, '(99, )')])
def test_pop(one, two, result):
    """."""
    starter_3 = LinkedList(one)
    starter_3.insert(two)
    starter_3.pop()
    assert starter_3.size() == 1
    assert not starter_3.head.next_node
    assert starter_3.display() == result
    try:
        starter_3.pop()
    except ValueError:
        pass


@pytest.mark.parametrize('one, two, de, exist, result', [(77, 'cat', 'cat', True,  '(77, )'), ([3], 1, [33], False, '([3], 1, )')])
def test_delete(one, two, de, exist, result):
    """."""
    starter_3 = LinkedList(one)
    starter_3.insert(two)
    assert hasattr(starter_3, 'delete')
    try:
        starter_3.delete(de)
        assert starter_3.display() == result
    except ValueError:
        if not exist:
            pass

