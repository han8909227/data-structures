"""Test for Trie class."""

from trie import Trie, Node
import pytest


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


def test_Trie_cannot_init_with_num():
    """Assert proper error gets raised with num init."""
    with pytest.raises(ValueError):
        Trie([1])

