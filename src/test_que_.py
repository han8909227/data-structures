"""Will test the Queue module."""
from que_ import Queue

def test_queue_class_init():
    """Will test that an instance of Queue is created."""
    q = Queue()
    assert q._dll.head == None

def test_enqueue_adds_to_the_queue():
    """Will test that a value is added to the queue."""
    q = Queue()
    q.enqueue(1)
    assert len(q) == 1

def test_dequeue_removes_first_in_item():
    """Will test that the first in item is removed from the queue."""
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.dequeue()
    assert len(q) == 1

def test_that_peek_returns_the_next_value():
    """Will test that the peek method returns the next value, the next to be dequeued."""
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.peek() == 1

def test___len___returns_length_using_len():
    """Will test that you can use the len() on the instance of Queue to find the length."""
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert len(q) == 3