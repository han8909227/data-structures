"""Test my quick sort algorithm tests."""
from quick_sort import quick_sort, _quicksort
import pytest
from random import randint


@pytest.fixture(scope='function')
def list_ten():
    """Make a list of 10 vals."""
    return [x for x in range(10)]


@pytest.fixture(scope='function')
def rand_ten():
    """Make a random list of length 10."""
    return [randint(0, 1000) for _ in range(10)]


def test_sort_nums_in_list_random_case(rand_ten):
    """Test quick sort function."""
    result = quick_sort(rand_ten)
    key = sorted(rand_ten)
    assert result == key


def test_sort_nums_in_tuple_random_case(rand_ten):
    """Test quick sort function."""
    rand = tuple(rand_ten)
    result = quick_sort(rand)
    key = sorted(rand)
    assert result == key


def test_sort_nums_in_list_wrose_case(list_ten):
    """Test quick sort function."""
    reverse = list(reversed(list_ten))
    result = quick_sort(reverse)
    assert result == list_ten


def test_sort_nums_in_tuple_wrose_case(list_ten):
    """Test quick sort function."""
    reverse = tuple(reversed(list_ten))
    result = quick_sort(reverse)
    assert result == list_ten


def test_sort_method_raises_error():
    """Test if error gets raised for invalid type."""
    with pytest.raises(ValueError):
        quick_sort('12345')


def test_sort_method_raises_error_val():
    """Test if error gets raised for invalid type."""
    with pytest.raises(ValueError):
        quick_sort([1, 2, '3'])


def test_sort_method_raise_error_dic():
    """Test if error gets raised for invalid type."""
    with pytest.raises(ValueError):
        quick_sort({1, 2, 3})


def test_sort_method_raise_error_fun():
    """Test if error gets raised for invalid type."""
    with pytest.raises(ValueError):
        quick_sort([1, 2, 3, 'p'])


def test_sort_nums_in_list_random_case_helper(rand_ten):
    """Test quick sort function."""
    result = quick_sort(rand_ten)
    key = sorted(rand_ten)
    assert result == key


def test_sort_nums_in_list_wrose_case_helper(list_ten):
    """Test _quick sort function."""
    reverse = list(reversed(list_ten))
    result = _quicksort(reverse)
    assert result == list_ten

