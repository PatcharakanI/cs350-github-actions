from triangle import triangle
def test_invalid1():
    assert triangle(-2, 3, 4) == -1
    assert triangle(2,-3,4) == -1
    assert triangle(2,3,-4) == -1

def test_equilateral():
    assert triangle(3, 3, 3) == 2