"""Test for Priority Queue."""
import pytest
from priorityq import Priorityq


@pytest.fixture(scope='function')
def priorityq():
    """Making one mt priority queue instance per test."""
    return Priorityq()


@pytest.fixture(scope='function')
def priorityq_5():
    """Making one priority queue instance with len of 5 per test."""
    p_q = Priorityq()
    p_q.insert(1, 5)
    p_q.insert(2, 4)
    p_q.insert(3, 3)
    p_q.insert(4, 2)
    p_q.insert(5, 1)
    return p_q


def test_new_pq(priorityq):
    """Assert if the instance is initializted from Priority Queue class."""
    assert isinstance(priorityq, Priorityq)


def test_pq_insert(priorityq):
    """Assert if insert method works."""
    priorityq.insert(3)
    priorityq.insert(4, 4)
    assert priorityq.peek() == 4


def test_pq_pop(priorityq_5):
    """Assert if insert method works."""
    for num in range(1, 6):
        assert priorityq_5.pop() == num


def test_peek(priorityq_5):
    """Assert if peek method works."""
    for num in range(1, 6):
        assert priorityq_5.peek() == num
        priorityq_5.pop()
