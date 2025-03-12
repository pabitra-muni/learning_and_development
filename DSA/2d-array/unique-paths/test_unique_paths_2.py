import pytest
from unique_paths_2 import UniquePath2

@pytest.mark.parametrize("grid,expected", [
    ([[0,0,0],
      [0,1,0],
      [0,0,0]], 2),
    ([[0,1],
      [0,0]], 1),
    ([[0,0],
      [0,1]], 0),
    ([[0]], 1),
    ([[1]], 0),
    ([[0,0],
      [0,0]], 2),
    ([[0,1,0],
      [0,1,0],
      [0,0,0]], 1),
    ([[0,0,0,0],
      [0,1,0,0],
      [0,0,1,0],
      [0,0,0,0]], 4),
    ([[0,0,0],
      [1,1,0],
      [0,0,0]], 1),
    ([[0,0,0,0],
      [0,0,0,0],
      [0,0,0,0]], 10),
    ([[1,0,0],
      [0,0,0],
      [0,0,0]], 0),
    ([[0,0,0],
      [0,0,0],
      [0,0,1]], 0),
    ([[0,1,0,0],
      [1,0,0,0],
      [0,0,1,0],
      [0,0,0,0]], 0)
])
def test_unique_paths_with_obstacles(grid, expected):
    solution = UniquePath2()
    assert solution.uniquePathsWithObstacles(grid) == expected


