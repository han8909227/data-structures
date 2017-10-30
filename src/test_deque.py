"""Tests for DLL module."""
import pytest
from deque import Deque


@pytest.fixture(scope='function')
def deque():
    """Making one mt dll instance per test."""
    from deque import Deque
    return Deque()


@pytest.fixture(scope='function')
def deque_20():
    """Making one dll instance with len of 20 per test."""
    from deque import Deque
    dq = Deque()
    for num in range(20):
        dq.append(num)
    return dq


def test_init_new_dll(deque):
    """Will test that the instance is initialized."""
    assert isinstance(deque, Deque)


def test_deque_append_left(deque):
    """Will test the .append_left() function of deque append new value to end."""
    for num in range(20):
        old_head = deque._dll.head
        deque.append_left(num)
        assert deque._dll.head.data == num
        assert deque._dll.head.next == old_head
        try:
            assert old_head.previous == deque._dll.head
        except AttributeError:
            if num == 0:
                pass


def test_deque_append(deque):
    """Will test the append() function of deque."""
    for num in range(20):
        old_tail = deque._dll.tail
        deque.append(num)
        try:
            deque._dll.tail.previous == old_tail
        except AttributeError:
            if deque._dll.tail == dll.head:
                pass


def test_deque_pop(deque):
    """Will test the pop() function of deque will return and remove the tail value."""
    deque.append(1)
    assert deque.pop() == 1
    assert deque.size() == 0



def test_deque_pop_left(deque):
    """Testing the pop_left() function of deque will return and remove the head value."""
    deque.append(1)
    deque.append(2)
    assert deque.pop_left() == 1
    assert deque.size() == 1


def test_deque_peek(deque):
    """Testing for the peek() function of deque."""
    deque.append(1)
    deque.append(2)
    assert deque.peek() == 2


def test_deque_peek_after_pop(deque):
    """Testing for the peek() function of deque."""
    deque.append(1)
    deque.append(2)
    deque.append(3)
    deque.pop()
    assert deque.peek() == 2

def test_deque_peek_left(deque):
    """Testing for the peek_left() function of deque."""
    deque.append(1)
    deque.append(2)
    assert deque.peek_left() == 1


def test_deque_peek_left_after_pop_left(deque):
    """Testing for the peek_left() function of deque."""
    deque.append(1)
    deque.append(2)
    deque.append_left(3)
    deque.append_left(4)
    deque.pop_left()
    assert deque.peek_left() == 3


def test_deque_size_after_append(deque):
    """Testing for the peek_left() function of deque."""
    deque.append(1)
    deque.append(2)
    assert deque.size() == 2


def test_deque_size_is_none_when_zero(deque):
    """Testing for the peek_left() function of deque."""
    assert deque.size() == 0


def test_deque_size_after_appending_and_popping(deque):
    """Testing for the peek_left() function of deque."""
    deque.append(1)
    deque.append(2)
    deque.pop()
    assert deque.size() == 1


def test_deque_size_after_appending_and_popping_left(deque):
    """Testing for the peek_left() function of deque."""
    deque.append(1)
    deque.append(2)
    deque.pop_left()
    assert deque.size() == 1


def test_len_method_works_on_empty_deque(deque):
    """Testing that len() returns 0 on empty deque."""
    assert len(deque) == 0


def test_len_method_works_on_appended_list(deque):
    """Testing that len()returns proper length after appending."""
    deque.append(1)
    deque.append(2)
    assert len(deque) == 2

def test_len_method_works_on_append_left_list(deque):
    """Testing that len()returns proper length after appending."""
    deque.append_left(1)
    deque.append_left(2)
    assert len(deque) == 2

