"""Test my bubble sort algorithm."""
from bubble_sort import bubble_sort
import pytest
from random import randint


@pytest.fixture(scope='function')
def list_ten():
    """Making one empty BinarySearchTree instance per test."""
    return [x for x in range(10)]


@pytest.fixture(scope='function')
def rand_ten():
    """Make a random list of length 10."""
    return [randint(0, 1000) for _ in range(10)]


def test_sort_nums_in_list_random_case(rand_ten):
    """Test bubble sort function."""
    result = bubble_sort(rand_ten)
    key = sorted(rand_ten)
    assert result == key


def test_sort_nums_in_tuple_random_case(rand_ten):
    """Test bubble sort function."""
    rand = tuple(rand_ten)
    result = bubble_sort(rand)
    key = sorted(rand)
    assert result == key


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


def test_sort_method_raise_error_dic():
    """Test if error gets raised for invalid type."""
    with pytest.raises(ValueError):
        bubble_sort({1, 2, 3})


def test_sort_method_raise_error_fun():
    """Test if error gets raised for invalid type."""
    with pytest.raises(ValueError):
        bubble_sort([1, 2, 3, 'p'])
