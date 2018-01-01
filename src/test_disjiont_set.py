"""Tests for disjoint set data structure."""
import pytest
from disjoint_set import DisjointSet


@pytest.fixture(scope='function')
def disjoint_set():
    """Making one mt dll instance per test."""
    return DisjointSet([val for val in range(10)])


def test_error_raise_if_init_with_wrong_data_type():
    """Assert proper error is raised with wrong data."""
    with pytest.raises(ValueError):
        DisjointSet(['1', 2, 3, 4, 5])


def test_get_method_return_set_list(disjoint_set):
    """Test get method function properly."""
    result = [[val] for val in range(10)]
    assert disjoint_set.get() == result


def test_union_method_with_non_union_paris(disjoint_set):
    """Test union method function properly."""
    disjoint_set.union(1, 3)
    assert [3, 1] in disjoint_set.get()
    assert [1] and [3] not in disjoint_set.get()


def test_union_method_with_unioned_paris(disjoint_set):
    """Test union method function properly."""
    disjoint_set.union(1, 3)
    ds_len = len(disjoint_set.get())
    disjoint_set.union(3, 1)
    assert len(disjoint_set.get()) == ds_len  # no extra pair created


def test_find_method_with_val_in_union(disjoint_set):
    """Test find method function properly."""
    assert disjoint_set.find(5) == [5]


def test_find_method_with_val_not_in_union(disjoint_set):
    """Test find method function properly."""
    assert disjoint_set.find(50) is None


def test_dun_find_method_with_val_in_union(disjoint_set):
    """Test find method function properly."""
    assert disjoint_set._find_index(5) == 5


def test_dun_find_method_with_val_not_in_union(disjoint_set):
    """Test find method function properly."""
    assert disjoint_set._find_index(50) is None







