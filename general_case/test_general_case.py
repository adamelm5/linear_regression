from general_case import linear_regression
import numpy as np
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'graph_tools'))
#from graph import draw_graph_g
import matplotlib.pyplot as plt


# === Exemple d'utilisation ===
if __name__ == "__main__":

    print("\n\n##############    general case test   #############\n")
    
    # exemple de données où Y = X @ B
    X = np.array([
        [1, 1, 2],
        [1, 2, 3],
        [1, 3, 4],
        [1, 4, 5]
    ])
    b = np.array([1, 2, 3])
    Y = X @ b
    print(f"-> Exemple where Y = X @ B :\n")
    print(f"    X = \n{X} \n    Y = \n{Y.reshape(4, 1)}\n")
    beta_hat, R2 = linear_regression(X, Y)
    beta_hat = beta_hat.reshape(3, 1)
    print(f"beta_hat = \n{beta_hat} \nand R2 = {R2}\n\n")

    # exemple de données où Y != X @ B
    X = np.array([
        [1, 1], [1, 2], [1, 3], [1, 4], [1, 5],
        [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]
    ])
    Y = np.array([8, 3, 6, 2, 7, 1, 9, 4, 5, 2])
    print(f"-> Exemple where Y != X @ B :\n")
    print(f"    X = \n{X} \n    Y = \n{Y}\n")

    beta_hat, R2 = linear_regression(X, Y)
    beta_hat = beta_hat
    print(f"beta_hat = \n{beta_hat} \nand R2 = {R2}")

    # cas de dimension 1
    print("\n\n-> One dimension case :")
    x = [[1], [2], [3], [4], [5]]
    y = [2, 4, 6, 8, 10]
    print(f"    X = \n{X} \n    Y = \n{Y}\n")
    x, y = np.array(x), np.array(y)
    beta_hat, R2 = linear_regression(x, y)
    print(f"beta_hat = {beta_hat} and R2 = {R2}")
