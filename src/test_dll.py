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
    assert isinstance(dll, DoubleLinkedList)


def test_dll_push(dll):
    """Will test the .push() function of dll."""
    for num in range(20):
        old_head = dll.head
        dll.push(num)
        assert dll.head.data == num
        assert dll.head.next == old_head


def test_dll_pop(dll_20):
    """Will test the pop() function of dll."""
    for _ in range(20):
        next_head = dll_20.head.next
        dll_20.pop()
        assert dll_20.head == next_head
    with pytest.raises(IndexError):
        dll_20.pop()


def test_dll_append(dll):
    """Will test the append() function of dll."""
    for num in range(20):
        old_tail = dll.tail
        dll.append(num)
        assert dll.tail.previous == old_tail


def test_dll_shift(dll_20):
    """Testing the shift() function of dll."""
    for num in range(20):
        new_tail = dll_20.tail.previous
        dll_20.shift()
        assert dll_20.tail == new_tail
    with pytest.raises(IndexError):
        dll_20.shift()


def test_dll_remove(dll_20):
    """Testing for the remove() function of dll."""
    for num in range(20):
        dll_20.remove(num)
        temp = dll_20.head
        while temp:
            assert num != temp
            temp = temp.next
    with pytest.raises(IndexError):
        dll_20.pop()


def test_dll_remove_tail_val(dll_20):
    """Assert if tail gets re-assigned after old tail is removed."""
    dll_20.remove(0)
    assert dll_20.tail.data == 1


def test_dll_remove_head_val(dll_20):
    """Assert if head gets re-assigned after old head is removed."""
    dll_20.remove(20)
    assert dll_20.head.data == 19


def test_len_function(dll_20):
    """Test the length function works."""
    assert len(dll_20) == 20
