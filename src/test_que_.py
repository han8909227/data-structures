"""Will test the Queue module."""
import pytest
from que_ import Queue


@pytest.fixture(scope='function')
def q():
    """Making one mt queue instance per test."""
    from que_ import Queue
    return Queue()


@pytest.fixture(scope='function')
def q_20():
    """Making one queue instance with len of 20 per test."""
    from que_ import Queue
    q = Queue()
    for num in range(20):
        q.enqueue(num)
    return q


def test_queue_class_init(q):
    """Will test that an instance of Queue is created."""
    assert isinstance(q, Queue)
    assert hasattr(q, '_dll')


def test_enqueue_adds_to_the_queue(q):
    """Will test that a value is added to the queue."""
    for num in range(20):
        old_tail = q._dll.tail
        q.enqueue(num)
        assert old_tail == q._dll.tail.previous


def test_dequeue_removes_first_in_item(q_20):
    """Will test that the first in item is removed from the queue."""
    for num in range(20):
        new_head = q_20._dll.head.next
        q_20.dequeue()
        assert q_20._dll.head == new_head


def test_dequeue_raises_error_if_no_item_left(q):
    """Will test that an error is raised if no value left to dequeue."""
    with pytest.raises(ValueError):
        q.dequeue()


def test_peek_raises_error_if_no_item_there(q):
    """Test if peek raises an error if there is nothing in the queue."""
    with pytest.raises(ValueError):
        q.peek()


def test_that_peek_returns_the_next_value(q_20):
    """Will test that the peek method returns the next value, the next to be dequeued."""
    for num in range(20):
        peek = q_20.peek()
        dequeued = q_20.dequeue()
        assert peek == dequeued


def test___len___returns_length_using_len(q_20):
    """Will test that you can use the len() on the instance of Queue to find the length."""
    for num in range(20):
        q_20.dequeue()
        length = 19 - num
        assert len(q_20) == length


def test_size_returns_length(q_20):
    """Will test that you can use the len() on the instance of Queue to find the length."""
    for num in range(20):
        q_20.dequeue()
        length = 19 - num
        assert q_20.size() == length
