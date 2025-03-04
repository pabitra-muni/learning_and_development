import pytest
from image_rotation import ImageRotation

@pytest.mark.parametrize(
    "matrix, expected",
    [
        ([[1]], [[1]]),
        ([[1,2,3],[4,5,6],[7,8,9]], [[7,4,1],[8,5,2],[9,6,3]])
    ]
)
def test_rotate(matrix, expected):
    ImageRotation().rotate(matrix)
    assert matrix == expected
