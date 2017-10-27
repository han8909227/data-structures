"""Tests for DLL module."""
import pytest
from dll import DoubleLinkedList


@pytest.fixture(scope='function')
def dll():
    """Making one mt dll instance per test."""
    from dll import DoubleLinkedList
    return DoubleLinkedList()


@pytest.fixture(scope='function')
def dll_20():
    """Making one dll instance with len of 20 per test."""
    from dll import DoubleLinkedList
    dll = DoubleLinkedList()
    for num in range(20):
        dll.push(num)
    return dll


def test_init_new_dll(dll):
    """Will test that the instance is initialized."""
    assert hasattr(dll, 'head')
    assert hasattr(dll, 'tail')
    assert isinstance(dll, DoubleLinkedList)


@pytest.mark.parametrize('n', range(20))
def test_dll_push(n):
    """Will test the .push() function of dll."""
    l = DoubleLinkedList()
    for num in range(n):
        old_head = l.head
        l.push(num)
        assert l.head.data == num
        assert l.head.next == old_head
        try:
            assert old_head.previous == l.head
        except AttributeError:
            if num == 0:
                pass


def test_dll_pop(dll_20):
    """Will test the pop() function of dll."""
    for _ in range(20):
        next_head = dll_20.head.next
        dll_20.pop()
        assert dll_20.head == next_head
    try:
        dll_20.pop()
    except ValueError:
        pass


@pytest.mark.parametrize('n', range(20))
def test_dll_append(n):
    """Will test the append() function of dll."""
    l = DoubleLinkedList()
    for num in range(n):
        old_tail = l.tail
        l.append(num)
        try:
            l.tail.previous == old_tail
        except AttributeError:
            if l.tail == l.head:
                pass


def test_dll_shift(dll_20):
    """Testing the shift() function of dll."""
    for num in range(20):
        new_tail = dll_20.tail.previous
        dll_20.shift()
        assert dll_20.tail == new_tail
    try:
        dll_20.shift()
    except ValueError:
        pass


def test_dll_delete(dll_20):
    """Testing for the delete() function of dll."""
    for num in range(20):
        dll_20.delete(num)
        temp = dll_20.head
        try:
            while temp.next:
                assert num != temp
                temp = temp.next
        except AttributeError:
            if dll_20.head == dll_20.tail:
                pass
    try:
        dll_20.pop()
    except ValueError:
        pass
