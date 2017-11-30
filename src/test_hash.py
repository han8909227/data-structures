"""Test for hash table class."""
import pytest
from hash_ import HashTable
from string import ascii_lowercase as letters


@pytest.fixture(scope='function')
def ht():
    """Making one empty HashTable instance per test."""
    return HashTable()


@pytest.fixture(scope='function')
def ht_26():
    """Making one Hash table instance with 26 key val pairs inserted."""
    ht = HashTable()
    count = 1
    for char in letters:
        ht.set(char, count)
        count += 1
    return ht


def test_init_with_int_size():
    """Test if init method work properly."""
    a = HashTable(1000)
    assert a.bucket_count == 1000


def test_init_with_str_size():
    """Test if init method work properly."""
    a = HashTable('1500')
    assert a.bucket_count == 1500


def test_get_method_with_valid_key(ht_26):
    """Test get method work properly."""
    assert ht_26.get('g') == 7


def test_get_method_with_invalid_str_key(ht_26):
    """Test get method raises error."""
    with pytest.raises(KeyError):
        ht_26.get('G')


def test_get_method_with_invalid_int_key(ht_26):
    """"Test get method raises error."""
    with pytest.raises(ValueError):
        ht_26.get(99)


def test_set_method_with_valid_key_str_val(ht):
    """Test set method works properly."""
    ht.set('HELLO', 'WORLD')
    assert ht.get('HELLO') == 'WORLD' and ht.size == 1


def test_set_method_with_valid_key_int_val(ht_26):
    """Test set method works properly."""
    ht_26.set('HELLO', 1234)
    assert ht_26.get('HELLO') == 1234


def test_set_method_with_valid_key_float_val(ht_26):
    """Test set method works properly."""
    ht_26.set('HELLO', 1.234)
    assert ht_26.get('HELLO') == 1.234


def test_set_method_with_invalid_key(ht):
    """Test set method raises proper method."""
    with pytest.raises(ValueError):
        ht.set(1234, 'hello')


def test__find_by_key_method(ht_26):
    """Test _find_by_key method finds the key."""
    cell, bucket = ht_26._find_by_key('a')
    assert cell == ['a', 1] and bucket in ht_26.data


def test__set_helper_method(ht):
    """Test _set helper method can set new key, val."""
    ht._set_helper(None, ht.data[0], 'new', 100)
    assert ht.data[0][0] == ['new', 100]


def test__set_helper_method_replaces(ht_26):
    """Test _set_helper method can replace val."""
    ht_26._set_helper(ht_26.data[97][0], None, 'a', 'new')
    assert ht_26.get('a') == 'new' and ht_26.size == 26


def test__get__helper_method(ht_26):
    """Test _get_helper work properly."""
    assert ht_26._get_helper(ht_26.data[97][0]) == 1


def test__get__helper_method_with_no_found_cell(ht_26):
    """Test _get_helper work properly."""
    with pytest.raises(KeyError):
        ht_26._get_helper(None)


def test__additive_hash(ht_26):
    """Test _addive_hash method work properly."""
    assert ht_26._additive_hash('a') == 97


def test__hash(ht_26):
    """Test _hash method work properly."""
    assert ht_26._hash('a') == 97


def test__djb2_hash(ht_26):
    """Test _hash_djb2 works properly."""
    assert ht_26._djb2_hash('a') == ht_26._djb2_hash('b') - 1


def test__jsw_hash(ht_26):
    """Test jsw hash works properly."""
    assert ht_26._hash_jsw('a') == ht_26._hash_jsw('b') + 3


def test_repr(ht_26):
    """Test the repr fun works properly."""
    result = '{ ' + ', '.join([char + ':' + str(ht_26.get(char)) for char in letters]) + ' }'
    assert repr(ht_26) == result










