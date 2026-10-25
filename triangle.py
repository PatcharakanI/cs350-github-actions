def triangle(a, b, c):
 if a < 0 or b < 0 or c < 0:
    return -1
 elif a + b < c or b + c < a or c + a < b:
    return -1 #invalid
 elif a == b and b == c:
     return 2 # equilateral
 elif a == b or b == c or c == a:
    return 1 # isoceles
 elif a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or c ** 2 + a ** 2 == b ** 2:
    return 3 # right triangle
 else:
    return 4