import matplotlib.pyplot as plt
import numpy


def quadratic_graph(x1, x2, vx, vy):
    plt.plot([numpy.real(x1), vx, numpy.real(x2)], [0, vy, 0], lw=2)
    plt.axis([-10, 10, -10, 10])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Quadratic Equation Calculator')
    plt.grid(True)
    plt.show()
