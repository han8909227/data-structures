"""Test my insertion sort algorithm tests."""
from insertion_sort import insertion_sort
import pytest


@pytest.fixture(scope='function')
def list_ten():
    """Make a list of 10 vals."""
    return [x for x in range(10)]


def test_sort_nums_in_list(list_ten):
    """Test bubble sort function."""
    reverse = list(reversed(list_ten))
    result = insertion_sort(reverse)
    assert result == list_ten


def test_sort_nums_in_tuple(list_ten):
    """Test bubble sort function."""
    reverse = tuple(reversed(list_ten))
    result = insertion_sort(reverse)
    assert result == list_ten


def test_sort_method_raises_error():
    """Test if error gets raised for invalid type."""
    with pytest.raises(ValueError):
        insertion_sort('12345')


def test_sort_method_raises_error_val():
    """Test if error gets raised for invalid type."""
    with pytest.raises(ValueError):
        insertion_sort([1, 2, '3'])


def test_sort_method_raise_error_dic():
    """Test if error gets raised for invalid type."""
    with pytest.raises(ValueError):
        insertion_sort({1, 2, 3})


def test_sort_method_raise_error_fun():
    """Test if error gets raised for invalid type."""
    with pytest.raises(ValueError):
        insertion_sort([1, 2, 3, 'p'])


