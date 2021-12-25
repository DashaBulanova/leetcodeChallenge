import pytest

from .solution import segment


@pytest.mark.parametrize("input, segment_lengh, expected", [
    ([8, 2, 4, 6], 2, 4),
    ([1, 2, 3, 1, 2], 1, 3),
    ([2, 5, 4, 6, 8], 3, 4)
])
def test_bst_to_gst(input, segment_lengh, expected):
    actual = segment(input, segment_lengh)
    assert actual == expected
