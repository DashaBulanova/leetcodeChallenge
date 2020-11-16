import pytest

from addAndSearchWord.solution import WordDictionary


# @pytest.mark.parametrize("input, expected",
#                          [
#                              # ("a", False),
#                              # (".at", True),
#                              # (".ad", True),
#                              # ("b..", True),
#                              # ("3.x", True),
#                           ])
def test_is_palindrome():
    sut = WordDictionary()
    sut.addWord("at")
    sut.addWord("and")
    sut.addWord("an")
    sut.addWord("add")
    assert  sut.search("a") == False
    assert  sut.search(".at") == False
    sut.addWord("bat")
    assert sut.search(".at") == True
    assert sut.search("an.") == True
    assert sut.search("a.d.") == False
    assert sut.search("b.") == False
    assert sut.search("a.d") == True
    assert sut.search(".") == False
