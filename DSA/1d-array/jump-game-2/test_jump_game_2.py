import pytest
from jump_game_2 import JumpGame2

@pytest.mark.parametrize("nums,expected", [

    ([2, 3, 1, 0, 4], 2)
    ,
    # Test case with exact jumps needed
    ([1, 1, 1, 1], 3),  # Must make exactly 1-step jumps
    
    # Test case with decreasing values 
    ([4, 3, 2, 1, 0], 1),  # Can jump directly to end
    
    # Test case with long jump at start
    ([5, 0, 0, 0, 0, 0], 1),  # Can jump over all zeros
    
    # Test case with multiple possible paths but minimum jumps
    ([2, 3, 1, 1, 4], 2),  # Best path is index 0->1->4
    
    # Test case with minimum required jumps
    ([1, 2, 3], 2),  # Must jump 1->2->3
    
    # Test case with large numbers
    ([10, 0, 0, 0, 0, 0, 0, 0, 0, 0], 1),  # Large initial jump
    
    # Test case with optimal path requiring multiple small jumps
    ([1, 2, 1, 1, 1], 3),  # Best path is 0->1->2->4
    
    # Single element array
    ([0], 0),  # Already at destination
    
    # Two element array
    ([1, 0], 1)  # Simple one jump case
])
def test_Jump(nums, expected):
    assert JumpGame2().jump(nums) == expected

