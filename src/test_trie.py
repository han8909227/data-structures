"""Test for Trie class."""

from trie import Trie
import pytest
from types import GeneratorType


@pytest.fixture(scope='function')
def trie():
    """Making one empty Trie instance per test."""
    return Trie()


@pytest.fixture(scope='function')
def trie_5():
    """Making one Trie instance, with 5 words in."""
    trie = Trie(['hello', 'help', 'world', 'word', 'working'])
    return trie


def test_trie_can_init_with_str():
    """Test trie class can be init with iterablle."""
    a = Trie(['string'])
    assert a.size == 1


def test_trie_cannot_init_with_num():
    """Assert proper error gets raised with num init."""
    with pytest.raises(ValueError):
        Trie([1])


def test_trie_can_insert_str(trie):
    """Test if we can insert str into tree."""
    trie.insert('hello')
    assert trie.contains('hello')


def test_trie_cannot_insert_num(trie):
    """Assert proper error gets raised with num insertion."""
    with pytest.raises(ValueError):
        trie.insert(100)


def test_trie_contains_method(trie_5):
    """Test contain method."""
    assert trie_5.contains('hello')


def test_trie_contains_method_not_end(trie_5):
    """Test contain method."""
    assert not trie_5.contains('he')


def test_remove_existing_word(trie_5):
    """Test remove method."""
    trie_5.remove('hello')
    assert not trie_5.contains('hello')


def test_remove_existing_word_does_not_remove_words_with_same_prefix(trie_5):
    """Test remove method."""
    trie_5.remove('hello')
    assert trie_5.contains('help')


def test_remove_invalid_word(trie_5):
    """Test remove method."""
    with pytest.raises(ValueError):
        trie_5.remove('invisible')


def test_remove_invalid_type(trie_5):
    """Test remove method."""
    with pytest.raises(ValueError):
        trie_5.remove(100)


def test_size_method(trie_5):
    """Test size method."""
    assert trie_5.size == 5


def test_size_method_after_insertion(trie_5):
    """Test size method."""
    trie_5.insert('new')
    assert trie_5.size == 6


def test_size_method_after_deletion(trie_5):
    """Test size method."""
    trie_5.remove('hello')
    assert trie_5.size == 4


def test_traverse_method_on_partial_prefix(trie_5):
    """Test the traversal method works properly."""
    result = trie_5.traversal('he')
    assert 'hello' and 'help' in result


def test_traverse_method_word(trie_5):
    """Test the traversal method works properly."""
    assert next(trie_5.traversal('hello')) == 'hello'


def test_traverse_method_letter(trie_5):
    """Test the traversal method works properly."""
    result = trie_5.traversal('he')
    assert 'hello' or 'help' in next(result)


def test_traverse_method_non_existing_prefix(trie_5):
    """Test the traversal method works properly."""
    assert trie_5.traversal('nonexist') == []


def test_traverse_method_raise_error(trie_5):
    """Test the traversal method works properly."""
    with pytest.raises(ValueError):
        trie_5.traversal(100)


def test__dfs_method(trie_5):
    """Test _dfs method working properly."""
    node = trie_5.root.children['h'].children['e']
    result = trie_5._dfs(node, 'he')
    assert isinstance(result, GeneratorType)
    assert 'help' or 'hellow' in next(result)

