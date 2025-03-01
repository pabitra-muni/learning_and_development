import pytest
from pascal_triangle import PascalTriangle

@pytest.mark.parametrize(
    "num_rows,expected",
    [
        (1, [[1]]),
        (2, [[1], [1,1]]), 
        (3, [[1], [1,1], [1,2,1]]),
        (5, [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]),
        (7, [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1], [1,5,10,10,5,1], [1,6,15,20,15,6,1]])
    ]
)
def test_pascal_triangle(num_rows, expected):
    actual = PascalTriangle().createPascalTriangle(num_rows)
    assert actual == expected
