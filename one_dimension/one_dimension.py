def average(x):
    return sum(x) / len(x)

def a_b_linear_regression1(x, y): 
    av_x = average(x)
    av_y = average(y)
    a = 0
    ap = 0
    b = 0
    for i in range(len(x)):
        a = a + (x[i] - av_x) * (y[i] - av_y)
        ap = ap + (x[i] - av_x)**2
    a = a / ap
    b = av_y - a * av_x
    return a, b

def linear_function(x, a, b):
    return a * x + b

def R2(x, y, a, b):
    e = 0
    f = 0
    av_y = average(y)
    for i in range(len(x)):
        e = e + (y[i] - linear_function(x[i], a, b))**2
        f = f + (y[i] - av_y)**2
    return 1 - e / f


import numpy as np
import matplotlib.pyplot as plt
import sys
import os
def draw_graph(x, y, a, b, title, file_name):
    plt.title(title)
    x = np.array(x)
    y = np.array(y)
    plt.plot(x, y, 'o')
    plt.plot(x, a * x + b, 'r')
    # sauvegarder dans un fichier
    plt.savefig(file_name)
    plt.close()
    print(f"\nGraph saved in {file_name}")
