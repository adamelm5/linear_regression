import numpy as np
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'general_case'))
from general_case import linear_regression
import pandas as pd



def viscosity(data):
    Y = np.log(np.array(data['viscosidad_mPa_s']))
    
    X_features = np.array([
        data['temperature_Celsius'], 
        data['presion_MPa'], 
        data['volumen_cm3_mol'], 
        data['densidad_g_cm3']
    ]).T
    
    beta_hat, R2 = linear_regression(X_features, Y)

    print(f"beta_hat = {beta_hat} \nR2 = {R2}")
    return beta_hat
    

def draw_graph2(beta_hat, data):
    variables = ['temperature_Celsius', 'presion_MPa', 'volumen_cm3_mol', 'densidad_g_cm3']
    labels = ['Température (°C)', 'Pression (MPa)', 'Volume molaire (cm³/mol)', 'Densité (g/cm³)']
    symbols = ['T', 'P', 'Vm', 'ρ']

    means = data[variables].mean().values
    beta_0 = beta_hat[0]
    betas = beta_hat[1:].flatten()

    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    axs = axs.flatten()

    for i, var in enumerate(variables):
        x = np.linspace(data[var].min(), data[var].max(), 100)
        X_ref = np.tile(means, (100, 1))
        X_ref[:, i] = x

        Y_pred = beta_0 + X_ref @ betas

        axs[i].plot(x, Y_pred, color='royalblue', linewidth=2)
        axs[i].set_xlabel(labels[i])
        axs[i].set_ylabel("ln(Viscosité)")
        
        fixed_vars = []
        for j, fixed_var in enumerate(variables):
            if j != i:
                fixed_vars.append(f"{symbols[j]} = {means[j]:.1f}")
        
        title = f"ln(η) vs {symbols[i]}\n({', '.join(fixed_vars)})"
        axs[i].set_title(title)
        axs[i].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("applications/physics/graphs/graph_for_viscosity.png")
    print(f"\nGraph saved in applications/physics/graphs/graph_for_viscosity.png")
    plt.close()


if __name__ == '__main__':

    print("\n\n##############   Viscosity experience   #############\n")

    csv_path = "applications/physics/viscosity_experience.csv"
    data = pd.read_csv(csv_path)

    beta_hat = viscosity(data)
    draw_graph2(beta_hat, data)
