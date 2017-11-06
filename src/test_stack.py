"""Tests for stack module."""
import pytest
from stack import Stack
from linked_list import LinkedList


def test_init_new_stack():
    """Will test that the instance is initialized."""
    a = Stack()
    assert hasattr(a, 'top_stack')
    assert isinstance(a, Stack)
    assert isinstance(a._linked_list, LinkedList)


def test_stack_init_with_iterable():
    """Will test that input is iterable."""
    a = Stack([n for n in range(20)])
    assert len(a) == 20


@pytest.mark.parametrize('n', range(20))
def test_stack_will_push_into_stack(n):
    """Will test that you can .push() into the stack."""
    a = Stack()
    a.push(n)
    assert a._linked_list.head.data == n


def test_stack_pop():
    """Will test that the top stack element is popped."""
    a = Stack([n for n in range(20)])
    for _ in range(20):
        a.pop()
    assert not a._linked_list.head
    try:
        a.pop()
    except ValueError:
        pass


def test_stack_pop_empty_stack_will_raise_index_error():
    """Will test that a IndexError is raised when popping from a empty stack."""
    with pytest.raises(ValueError):
        a = Stack()
        a.pop()


def test_stack_pop_multiple_times_will_raise_index_error():
    """Will test that a IndexError is raised after popping multiple times down to empty stck."""
    with pytest.raises(ValueError):
        a = Stack((1, 2, 3, 4))
        a.pop()
        a.pop()
        a.pop()
        a.pop()
        a.pop()
