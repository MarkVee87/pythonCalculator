from sys import version_info
from MathsTools import *
from QuadraticCalculator import quadCalc

py3 = version_info[0] > 2

if py3:
    num1 = 2
    num2 = 6
    # num1 = int(input("num1: "))
    # num2 = int(input("num2: "))
else:
    num1 = 2
    num2 = 6
    # num1 = int(raw_input("num1: "))
    # num2 = int(raw_input("num2: "))

# print("Multiplying two numbers", multiply(num1, num2))
# print("Adding two numbers", add(num1, num2))
# print("Subtracting one number from another", subtract(num1, num2))
# print("Dividing one number by another", divide(num1, num2))
# print("Raising a number to a power", raiseToPowerOf(num1, num2))
# listOfNumbers = [1, 2, 3, 4, 5]
# print("Multiplying two numbers (using value from list)", multiply(listOfNumbers[2], num2))

print("Quadratic calculator code being called here")
if py3:
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
else:
    a = int(raw_input("a: "))
    b = int(raw_input("b: "))
    c = int(raw_input("c: "))
quadraticCoordinates = quadCalc(a, b, c)
# 1,2,3 = x1 = (-1+1.41421356237j) and x2 = (-1-1.41421356237j)
print('x1 = {0} and x2 = {1}'.format(quadraticCoordinates[0], quadraticCoordinates[1]))
