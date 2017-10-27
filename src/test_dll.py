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


def test_dll_push(dll):
    """Will test the .push() function of dll."""
    for num in range(20):
        old_head = dll.head
        dll.push(num)
        assert dll.head.data == num
        assert dll.head.next == old_head
        try:
            assert old_head.previous == dll.head
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


def test_dll_append(dll):
    """Will test the append() function of dll."""
    for num in range(20):
        old_tail = dll.tail
        dll.append(num)
        try:
            dll.tail.previous == old_tail
        except AttributeError:
            if dll.tail == dll.head:
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
