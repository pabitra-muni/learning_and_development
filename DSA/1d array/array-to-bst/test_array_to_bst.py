import pytest
from array_to_bst import ArrayToBst

@pytest.mark.parametrize(
    "nums, expected",
    [
        
    ]
)
def test_merge(nums, expected):
    actual = ArrayToBst().sortedArrayToBST(nums)
    assert  actual == expected