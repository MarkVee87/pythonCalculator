import cmath


def quadCalc(a, b, c):
    middle = sqrtCalc(a, b, c)
    x1 = (-b + (cmath.sqrt(middle))) / (2 * a)
    x2 = (-b - (cmath.sqrt(middle))) / (2 * a)
    x_list = [x1, x2]
    return x_list


def sqrtCalc(a, b, c):
    b_squared = b ** b
    four_a_c = 4 * a * c
    return b_squared - four_a_c
