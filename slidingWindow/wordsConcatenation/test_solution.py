import pytest

from .solution import Solution


@pytest.mark.parametrize("input, words, expected",
                         [
                             ("barfoothefoobarman", ["foo", "bar"], [0, 9]),
                             ("barfoofoobarthefoobarman", ["bar", "foo", "the"], [6, 9, 12]),
                             ("catfoxcat", ["cat", "fox"], [0, 3]),
                             ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"], []),
                             # ("aaaaaaaaaaaaaa", ["aa", "aa"], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
                         ])
def test_number_of_bits(input, words, expected):
    actual = Solution().findSubstring(input, words)
    assert actual == expected
