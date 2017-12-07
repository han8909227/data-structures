"""Test my bubble sort algorithm."""
from bubble_sort import bubble_sort
import pytest


@pytest.fixture(scope='function')
def list_ten():
    """Making one empty BinarySearchTree instance per test."""
    return [x for x in range(10)]


def test_sort_nums_in_list(list_ten):
    """Test bubble sort function."""
    reverse = list(reversed(list_ten))
    result = bubble_sort(reverse)
    assert result == list_ten


def test_sort_nums_in_tuple(list_ten):
    """Test bubble sort function."""
    reverse = tuple(reversed(list_ten))
    result = bubble_sort(reverse)
    assert result == list_ten


def test_sort_method_raises_error():
    """Test if error gets raised for invalid type."""
    with pytest.raises(ValueError):
        bubble_sort('12345')


def test_sort_method_raises_error_val():
    """Test if error gets raised for invalid type."""
    with pytest.raises(ValueError):
        bubble_sort([1, 2, '3'])



