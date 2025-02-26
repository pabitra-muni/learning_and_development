import pytest
from remove_element import RemoveElement  # Import the function from your module

@pytest.mark.parametrize(
    "nums, value, expected",
    [
        ([3,2,2,3], 3, 2),
        ([0,1,2,2,3,0,4,2], 2, 5),
        ([0,1,2,3,4], 7, 5),
        ([0,1,2,3,4], 4, 4),
        ([0], 4, 1),
        ([0,2], 4, 2)
    ]
)
def test_removeDuplicateElement(nums, value, expected):
    obj = RemoveElement()
    actual = obj.removeDuplicateElement(nums, value)
    print('after processing: ', nums)
    assert  actual == expected
