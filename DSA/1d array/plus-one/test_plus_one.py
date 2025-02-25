import pytest
from plus_one import PlusOne

@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 7, 1, 5], [2, 7, 1, 6]),
        ([2, 7, 1, 9], [2, 7, 2, 0]),
        ([2, 7, 9, 9], [2, 8, 0, 0]),
        ([9], [1, 0])
    ]
)
def test_two_sum(nums, expected):
    actual = PlusOne().doPlusOne(nums)
    assert  actual == expected
