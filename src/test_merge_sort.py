"""Test my merge sort algorithm tests."""
from merge_sort import merge_sort, _merge_sort, _merge
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
    """Test merge sort function."""
    result = merge_sort(rand_ten)
    key = sorted(rand_ten)
    assert result == key


def test_sort_nums_in_tuple_random_case(rand_ten):
    """Test merge sort function."""
    rand = tuple(rand_ten)
    result = merge_sort(rand)
    key = sorted(rand)
    assert result == key


def test_sort_nums_in_list_wrose_case(list_ten):
    """Test merge sort function."""
    reverse = list(reversed(list_ten))
    result = merge_sort(reverse)
    assert result == list_ten


def test_sort_nums_in_tuple_wrose_case(list_ten):
    """Test merge sort function."""
    reverse = tuple(reversed(list_ten))
    result = merge_sort(reverse)
    assert result == list_ten


def test_sort_method_raises_error():
    """Test if error gets raised for invalid type."""
    with pytest.raises(ValueError):
        merge_sort('12345')


def test_sort_method_raises_error_val():
    """Test if error gets raised for invalid type."""
    with pytest.raises(ValueError):
        merge_sort([1, 2, '3'])


def test_sort_method_raise_error_dic():
    """Test if error gets raised for invalid type."""
    with pytest.raises(ValueError):
        merge_sort({1, 2, 3})


def test_sort_method_raise_error_fun():
    """Test if error gets raised for invalid type."""
    with pytest.raises(ValueError):
        merge_sort([1, 2, 3, 'p'])


def test_helper_method_merge_sort(list_ten):
    """Test the helper method _merge sort works properly."""
    reverse = list(reversed(list_ten))
    result = _merge_sort(reverse)
    assert result == list_ten


def test_helper_method_merge_sort_single_val(list_ten):
    """Test the helper method _merge sort works properly."""
    result = _merge_sort([1])
    assert result == [1]


def test_helper_method_sort_single_vals():
    """Test the helper method _merge works properly."""
    result = _merge([8], [6])
    assert result == [6, 8]


def test_helper_method_sort_larger_half():
    """Test the helper method _merge works properly."""
    result = _merge([8, 7, 6], [5, 4, 3])
    assert result == [5, 4, 3, 8, 7, 6]


