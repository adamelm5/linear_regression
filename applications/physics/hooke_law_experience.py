import numpy as np
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'one_dimension'))
from one_dimension import a_b_linear_regression1, R2, linear_function, draw_graph
import pandas as pd

def hooke_law(data):
    x = data['Mass_kg']
    y = data['Stretch_m']
    a, b = a_b_linear_regression1(x, y)
    print(f"a = {a} and b = {b}")
    print(f"R2 = {R2(x, y, a, b)}")
    draw_graph(x, y, a, b, 
    "Linear regression applied to the datas of a Hooke's \nlaw experience : stretch = f(mass)",
     "applications/physics/graphs/graph_for_hooke_law.png")

if __name__ == '__main__':

    print("\n\n##############    Hooke's law experience  #############")

    data = pd.read_csv('applications/physics/hooke_law_experience.csv')
    hooke_law(data)