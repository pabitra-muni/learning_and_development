import pytest
from jump_game import JumpGame

@pytest.mark.parametrize("nums,expected", [
    ([2], True),
    ([2, 3], True),
    ([0, 3], False),
    ([2, 3, 1, 0, 4], True),
    # Test case with zeros in the middle
    ([3, 2, 1, 0, 4], False),  # Cannot jump over the zero
    
    # Test case with exact jumps needed
    ([1, 1, 1, 1], True),  # Must make exactly 1-step jumps
    
    # Test case with decreasing values
    ([4, 3, 2, 1, 0], True),  # Can jump directly to end
    
    # Test case with long jump at start
    ([5, 0, 0, 0, 0, 0], True),  # Can jump over all zeros
    
    # Test case with multiple possible paths
    ([2, 3, 1, 1, 4], True),  # Can take different paths to reach end
    
    # Test case with trap
    ([3, 2, 1, 0, 0], False),  # Gets stuck at second-to-last position
    
    # Test case with minimum jumps
    ([1, 0, 1, 0], False),  # Cannot reach end due to zero
    
    # Test case with large numbers
    ([10, 0, 0, 0, 0, 0, 0, 0, 0, 0], True)  # Large initial jump
])
def test_CanJump(nums, expected):
    assert JumpGame().canJump(nums) == expected

