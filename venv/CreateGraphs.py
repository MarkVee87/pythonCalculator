import matplotlib.pyplot as plt
import numpy


def quadratic_graph(x1, x2):
    plt.plot([numpy.real(x1), 0], [numpy.real(x2), 0], 'ro')
    plt.show()
