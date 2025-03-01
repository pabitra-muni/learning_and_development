import pytest
from container_with_most_water import WaterContainer

@pytest.mark.parametrize("heights,expected", [
    # Regular case with multiple heights
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),  # Area between height[1]=8 and height[8]=7
    
    # Two equal heights
    ([4, 4], 4),  # Area between the two heights of 4
    
    # Ascending heights
    ([1, 2, 3, 4, 5], 6),  # Area between height[0]=1 and height[4]=5
    
    # Descending heights
    ([5, 4, 3, 2, 1], 6),  # Area between height[0]=5 and height[4]=1
    
    # Heights with zeros
    ([0, 7, 0, 4, 0, 8, 0], 28),  # Area between height[1]=7 and height[5]=8
    
    # All same heights
    ([5, 5, 5, 5, 5], 20),  # Area between first and last height
])
def test_max_area(heights, expected):
    water_container = WaterContainer()
    assert water_container.maxArea(heights) == expected

