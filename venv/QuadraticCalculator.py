from sys import version_info
import cmath


def quadratic_calculator():
    # py3 = version_info[0] > 2

    # if py3:
    #     a = int(input("a: "))
    #     b = int(input("b: "))
    #     c = int(input("c: "))
    #     return solve_formula(a, b, c)
    # else:
    #     a = int(raw_input("a: "))
    #     b = int(raw_input("b: "))
    #     c = int(raw_input("c: "))
    #     return solve_formula(a, b, c)
    return solve_formula(2, -12, 16)


def solve_formula(a, b, c):
    d = (b ** 2) - (4 * a * c)
    x1 = (-b - cmath.sqrt(d)) / (2 * a)
    x2 = (-b + cmath.sqrt(d)) / (2 * a)
    vx = find_vx(a, b)
    vy = find_vy(a, b, c)
    return [x1, x2, vx, vy]


def find_vx(a, b):
    vx = -b / (2 * a)
    print("vx(h) value is", vx)
    return vx


def find_vy(a, b, c):
    ass = -b / (2 * a)
    vy = a * ass * ass + b * ass + c
    print("vy(k) value is", vy)
    return vy
