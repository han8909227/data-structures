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

    a = Stack((1, 2, 3, 4))
    assert len(a) == 4


def test_stack_will_push_into_stack():
    """Will test that you can .push() into the stack."""

    a = Stack((1, 2, 3, 4))
    a.push(5)
    assert a._linked_list.head.data == 5


def test_stack_pop_will_pop_top_stack():
    """Will test that the top stack element is popped."""

    a = Stack((1, 2, 3, 4))
    a.pop()
    len(a) == 3


def test_stack_pop_returns_proper_item():
    """Will test that popped item is returned."""

    a = Stack((1, 2, 3, 4))
    assert a.pop() == 4



def test_stack_returns_stack_length():
    """Will test that the length of the stack is returned."""

    a = Stack()
    assert a._linked_list.size() == 0


def test_stack_can_use_len_function():
    """Will test that the len function will return proper length."""

    a = Stack()
    assert len(a) == a._linked_list.size()