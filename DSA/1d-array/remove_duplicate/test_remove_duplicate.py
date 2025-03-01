import pytest
from remove_duplicate import Duplicate

@pytest.mark.parametrize(
    "nums, expectedLength",
    [
        ([0,0,1,1,1,2,2,3,3,4], 5),
        ([1,1,2], 2)
    ]
)
def test_rearrangeDuplicates(nums, expectedLength):
    obj = Duplicate()
    actualLength = obj.rearrangeDuplicates(nums)
    assert  actualLength == expectedLength
