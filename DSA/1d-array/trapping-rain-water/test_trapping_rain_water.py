import pytest
from trapping_rain_water import RainWaterTrap

@pytest.mark.parametrize("heights,expected", [
    ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
    ([4,2,0,3,2,5], 9),
    ([2,6,3,8,2,7,2,5,0], 11)
    
])
def test_max_area(heights, expected):
    assert RainWaterTrap().trap(heights) == expected

