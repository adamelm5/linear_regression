import numpy as np

def linear_regression(X, Y, add_intercept=True):
    X = np.asarray(X, dtype=float)
    Y = np.asarray(Y, dtype=float).reshape(-1, 1)

    if add_intercept:
        X = np.hstack((np.ones((X.shape[0], 1)), X))

    beta_hat = np.linalg.pinv(X.T @ X) @ X.T @ Y

    Y_pred = X @ beta_hat
    residus = Y - Y_pred

    SS_res = float(residus.T @ residus)
    SS_tot = float(((Y - np.mean(Y))**2).sum())
    R2 = 1 - SS_res / SS_tot

    return beta_hat, R2
