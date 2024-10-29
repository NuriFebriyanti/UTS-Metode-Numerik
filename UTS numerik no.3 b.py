import numpy as np

# Fungsi untuk menghitung R(T)
def R(T):
    return 5000 * np.exp(3500 / T - 1)

# Fungsi untuk menghitung turunan eksak dR/dT
def exact_derivative(T):
    # Menghitung dR/dT secara eksak
    dR_dT = 5000 * np.exp(3500 / T - 1) * (-3500 / T**2)
    return dR_dT

# Contoh penggunaan
T = 298  # Temperatur dalam Kelvin

# Menghitung turunan eksak
dR_exact = exact_derivative(T)

print(f"Turunan eksak dR/dT pada T = {T} K: {dR_exact}")