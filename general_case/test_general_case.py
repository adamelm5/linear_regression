from general_case import linear_regression
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":

    print("\n\n##############    General Case Test   #############\n\n")
    
    X = np.array([
        [1, 1, 2],
        [1, 2, 3],
        [1, 3, 4],
        [1, 4, 5]
    ])
    b = np.array([1, 2, 3])
    Y = X @ b
    print("-> Y = X @ B :")
    print(f"X =\n{X}\nY =\n{Y.reshape(-1,1)}\n")
    beta_hat, R2 = linear_regression(X, Y)
    print(f"beta_hat =\n{beta_hat}\nR2 = {R2}\n\n")

    X = np.array([[1, i] for i in range(1, 11)])
    Y = np.array([8, 3, 6, 2, 7, 1, 9, 4, 5, 2])
    print("-> Y != X @ B :")
    print(f"X =\n{X}\nY = {Y}\n")
    beta_hat, R2 = linear_regression(X, Y)
    print(f"beta_hat =\n{beta_hat}\nR2 = {R2}\n\n")


    x = np.array([[1], [2], [3], [4], [5]])
    y = np.array([2, 4, 6, 8, 10])
    print("-> 1 dimension :")
    print(f"x =\n{x}\ny = {y}\n")
    beta_hat, R2 = linear_regression(x, y)
    print(f"beta_hat = {beta_hat.ravel()}\nR2 = {R2}\n\n")
