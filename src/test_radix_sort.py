"""Test my radix sort algorithm tests."""
from radix_sort import radix_sort, _populate_sets, _dequeue_sets
import pytest
from random import randint


@pytest.fixture(scope='function')
def list_hundred():
    """Make a list of 100 vals."""
    return [x for x in range(100)]


@pytest.fixture(scope='function')
def rand_hundred():
    """Make a random list of length 100."""
    return [randint(0, 1000) for _ in range(100)]


@pytest.fixture(scope='function')
def rand_neg():
    """Make a random list of neg value list len 100."""
    return [randint(-1000, 0) for _ in range(100)]


def test_sort_list_with_neg_values(rand_neg):
    """Test if sorting method sorts negative values."""
    key = sorted(rand_neg)
    result = radix_sort(rand_neg)
    assert key == result


def test_sort_nums_in_list_random_case(rand_hundred):
    """Test radix sort function."""
    result = radix_sort(rand_hundred)
    key = sorted(rand_hundred)
    assert result == key


def test_sort_nums_in_tuple_random_case(rand_hundred):
    """Test radix sort function."""
    rand = tuple(rand_hundred)
    result = radix_sort(rand)
    key = sorted(rand)
    assert result == key


def test_sort_nums_in_list_wrose_case(list_hundred):
    """Test radix sort function."""
    reverse = list(reversed(list_hundred))
    result = radix_sort(reverse)
    assert result == list_hundred


def test_sort_nums_in_tuple_wrose_case(list_hundred):
    """Test radix sort function."""
    reverse = tuple(reversed(list_hundred))
    result = radix_sort(reverse)
    assert result == list_hundred


def test_sort_method_raises_error():
    """Test if error gets raised for invalid type."""
    with pytest.raises(ValueError):
        radix_sort('12345')


def test_sort_method_raises_error_val():
    """Test if error gets raised for invalid type."""
    with pytest.raises(ValueError):
        radix_sort([1, 2, '3'])


def test_sort_method_raise_error_dic():
    """Test if error gets raised for invalid type."""
    with pytest.raises(ValueError):
        radix_sort({1, 2, 3})


def test_sort_method_raise_error_fun():
    """Test if error gets raised for invalid type."""
    with pytest.raises(ValueError):
        radix_sort([1, 2, 3, 'p'])


# def test_populated_set_method():
#     """Test helper method populate sets."""
#     str_inputs = ['']
#     _populate_sets(str_inputs, indx, q_set)