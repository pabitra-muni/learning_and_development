import pytest
from two_sum import TwoSum

@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),        # Basic case
        ([1, 2, 3, 4, 5], 6, [1, 3]),       # Multiple elements
        ([-3, 4, 3, 90], 0, [0, 2]),        # Negative numbers
        ([1000000, 2000000, 3000000], 5000000, [1, 2]),  # Large numbers
        ([1, 2, 3, 4], 10, []),             # No solution case
        ([5], 5, []),                       # Single element
        ([3, 3], 6, [0, 1]),                # Duplicate elements
    ]
)
def test_two_sum(nums, target, expected):
    obj = TwoSum()
    assert obj.twoSumWithMap(nums, target) == expected
