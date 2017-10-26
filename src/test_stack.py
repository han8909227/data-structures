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


@pytest.mark.parametrize('n', range(20))
def test_stack_init_with_iterable(n):
    """Will test that input is iterable."""
    a = Stack(range(n))
    assert len(a) == n


@pytest.mark.parametrize('n', range(20))
def test_stack_will_push_into_stack(n):
    """Will test that you can .push() into the stack."""
    a = Stack()
    a.push(n)
    assert a._linked_list.head.data == n


@pytest.mark.parametrize('n', range(20))
def test_stack_pop(n):
    """Will test that the top stack element is popped."""
    a = Stack(range(n))
    for _ in range(n):
        to_be_pop = a._linked_list.head.next_node
        a.pop()
        assert a._linked_list.head == to_be_pop
    assert not a._linked_list.head
    try:
        a.pop()
    except ValueError:
        pass




