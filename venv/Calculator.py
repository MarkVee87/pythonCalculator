from MathsTools import *
from QuadraticCalculator import quadratic_calculator

num1 = 3
num2 = 7

print("Multiplying two numbers", multiply(num1, num2))
print("Adding two numbers", add(num1, num2))
print("Subtracting one number from another", subtract(num1, num2))
print("Dividing one number by another", divide(num1, num2))
print("Raising a number to a power", raiseToPowerOf(num1, num2))

print("\nQuadratic calculator:")
quadraticCoordinates = quadratic_calculator()
print('x1 = {0} and x2 = {1}'.format(quadraticCoordinates[0], quadraticCoordinates[1]))
