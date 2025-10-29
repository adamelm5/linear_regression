import numpy as np

# Function that computes the linear regression of a set of points
def linear_regression(X, Y):

    XtX = X.T @ X
    XtY = X.T @ Y

    if np.linalg.det(XtX) == 0:
        beta_hat = np.linalg.pinv(XtX) @ XtY
    else:
        beta_hat = np.linalg.inv(XtX) @ XtY

    residus = Y - X @ beta_hat
    SS_res = float(residus.T @ +residus)
    Y_mean = np.mean(Y)
    SS_tot = float((Y - Y_mean).T @ (Y - Y_mean))
    
    R2 = 1 - (SS_res / SS_tot)
    
    return beta_hat, R2