import pytest
from search_position import SearchPosition  # Import the function from your module

@pytest.mark.parametrize(
    "nums, value, target",
    [
        ([1,3,5,6], 5, 2),
        ([1,3,5,6], 2, 1),
        ([1,3,5,6], 7, 4),
        ([2,3,5,6], 2, 0),
        ([2,3,5,6], 1, 0),
        ([2,3,5,6], 6, 3),
        ([2], 0, 0)
    ]
)
def test_searchInsertPosition(nums, value, target):
    obj = SearchPosition()
    assert  obj.searchInsertPositionImproved(nums, value) == target
