import numpy as np
import matplotlib.pyplot as plt
from one_dimension import a_b_linear_regression1

def draw_graph(x, y, a, b, title):
    plt.title(title)
    x = np.array(x)
    y = np.array(y)
    plt.plot(x, y, 'o')
    plt.plot(x, a * x + b, 'r')
    plt.show()
