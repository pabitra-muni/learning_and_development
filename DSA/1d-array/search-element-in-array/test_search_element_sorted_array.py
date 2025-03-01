import pytest
from search_element_sorted_array import ElementSearch

@pytest.mark.parametrize(
    "nums, target, expectedRange",
    [
        ([5,7,7,8,8,10], 8, [3, 4]),
        ([5,7,7,8,8,10], 10, [5, 5]),
        ([5,7,7,8,8,10], 5, [0, 0]),
        ([5], 8, [-1, -1]),
        ([5], 5, [0, 0]),
        ([5], 9, [-1, -1]),
        ([3,3,3], 3, [0, 2])
    ]
)
def test_search(nums, target, expectedRange):
    assert ElementSearch().searchRange(nums, target) == expectedRange
