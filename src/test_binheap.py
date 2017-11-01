"""Test for Binheap."""
import pytest
from binheap import Binheap


@pytest.fixture(scope='function')
def binheap():
    """Making one mt Binheap instance per test."""
    return Binheap()


@pytest.fixture(scope='function')
def binheap_20():
    """Making one heap instance with len of 20 per test."""
    heap = Binheap()
    for num in range(20):
        heap.push(num)
    return heap


def test_new_heap(binheap):
    """Assert if the instance is initialited from Binheap class."""
    assert isinstance(binheap, Binheap)


def test_heap_push(binheap):
    """Assert if the insert is succesful."""
    for num in range(1, 21):
        binheap.push(num)
        assert binheap.size == num


def test_heap_pop(binheap_20):
    """Assert if the min value is pop every time a pop is trigger."""
    for num in range(20):
        assert binheap_20.pop() == num
