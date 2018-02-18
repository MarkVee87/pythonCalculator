import matplotlib.pyplot as plt
import numpy


def quadratic_graph(x1, x2, vx, vy):
    plt.plot([numpy.real(x1), numpy.real(x2), vx], [0, 0, vy], 'ro')
    plt.axis([-10, 10, -10, 10])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Quadratic Equation Calculator')
    plt.grid(True)
    plt.show()
