from triangle import triangle
def test_invalid1():
    assert triangle(-2, 3, 4) == -1
    assert triangle(2,-3,4) == -1
    assert triangle(2,3,-4) == -1

def test_equilateral():
    assert triangle(3, 3, 3) == 2

def test_isoceles():
    assert triangle(3, 3, 4) == 1
    assert triangle(3, 4, 3) == 1
    assert triangle(4, 3, 3) == 1

def test_right_triangle():
    assert triangle(3, 4, 5) == 3
    assert triangle(5, 12, 13) == 3
    assert triangle(8, 15, 17) == 3