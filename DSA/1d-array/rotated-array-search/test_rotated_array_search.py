import pytest
from rotated_array_search import RotatedArraySearch

@pytest.mark.parametrize(
    "nums, target, expectedIndex",
    [
        
        ([5,1,3], 3, 2)
    ]
)
def test_search(nums, target, expectedIndex):
    assert RotatedArraySearch().search(nums, target) == expectedIndex
