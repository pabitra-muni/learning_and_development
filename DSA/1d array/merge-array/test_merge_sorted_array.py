import pytest
from merge_sorted_array import MergeArray

@pytest.mark.parametrize(
    "nums1, m, nums2, n, expected",
    [
        ([2, 7, 0, 0], 2, [1, 6], 2, [1, 2, 6, 7])
    ]
)
def test_merge(nums1, m, nums2, n, expected):
    MergeArray().merge(nums1, m, nums2, n)
    assert  nums1 == expected