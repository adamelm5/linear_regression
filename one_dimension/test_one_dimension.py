import numpy as np
from one_dimension import average, a_b_linear_regression1, R2, linear_function
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'graph_tools'))
from graph import draw_graph


if __name__ == '__main__':

    print("\n\n##############    one dimension test   #############")

    # a linear function y = 2 * x
    print("\n 1. points that belong to the linear function :")
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    print(f"    x = {x} and y = {y}")
    a, b = a_b_linear_regression1(x, y)
    print(f"    a = {a} and b = {b}")
    draw_graph(x, y, a, b, "linear regression for aligned points")
    print(f"    R2 = {R2(x, y, a, b)}")

    # random points
    print("\n 2. random points :")
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 6, 9, 10]
    print(f"    x = {x} and y = {y}")
    a, b = a_b_linear_regression1(x, y)
    print(f"    a = {a} and b = {b}")
    draw_graph(x, y, a, b, "linear regression for non aligned points")
    print(f"    R2 = {R2(x, y, a, b)}\n\n")