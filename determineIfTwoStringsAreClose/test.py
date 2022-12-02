import pytest
from .solution import Solution

@pytest.mark.parametrize("word1, word2, expected", [
("abc", "bca", True),
("a", "aa", False),
("cabbba", "abbccc", True),
("cabdba", "abbccc", False),
("abbzzca","babzzcz", False),
("zzazicgvzwntnneauziwfzlrzkynzschzdkbmpqbolwgvxjava", "uequrwuzhaudmnuqjuolkeszcyfqzqizrdrxpuvuygytbucwog", True)
])
def test(word1, word2, expected):
    actual = Solution().closeStrings(word1, word2)
    assert actual == expected
