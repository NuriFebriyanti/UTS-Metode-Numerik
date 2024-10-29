import numpy as np
import numpy as sp

# Fungsi untuk menghitung resistansi R berdasarkan temperatur T
def R(T):
    return 5000 * np.exp(3500 * (1/T - 1/298))

# Metode selisih maju
def forward_difference(f, T, h):
    return (f(T + h) - f(T)) / h

# Metode selisih mundur
def backward_difference(f, T, h):
    return (f(T) - f(T - h)) / h

# Metode selisih tengah
def central_difference(f, T, h):
    return (f(T + h) - f(T - h)) / (2 * h)

# Menghitung turunan eksak
def exact_derivative():
    T = sp.symbols('T')
    R = 5000 * sp.exp(3500 * (1/T - 1/298))
    dR_dT = sp.diff(R, T)
    return dR_dT

# Rentang temperatur dari 250K hingga 350K dengan interval 10K
temperatures = np.arange(250, 360, 10)
h = 10  # Langkah untuk selisih

# Menyimpan hasil
results = []

# Menghitung dR/dT untuk setiap temperatur
for T in temperatures:
    dR_forward = forward_difference(R, T, h)
    dR_backward = backward_difference(R, T, h)
    dR_central = central_difference(R, T, h)
    exact_dR_dT = exact_derivative().subs(sp.symbols('T'), T)

    results.append({
        'Temperature (K)': T,
        'Forward Difference (Ohm/K)': dR_forward,
        'Backward Difference (Ohm/K)': dR_backward,
        'Central Difference (Ohm/K)': dR_central,
        'Exact (Ohm/K)': exact_dR_dT.evalf()
    })

# Menampilkan hasil
for result in results:
    print(f"Temperature: {result['Temperature (K)']} K")
    print(f"  Forward Difference: {result['Forward Difference (Ohm/K)']:.4f} Ohm/K")
    print(f"  Backward Difference: {result['Backward Difference (Ohm/K)']:.4f} Ohm/K")
    print(f"  Central Difference: {result['Central Difference (Ohm/K)']:.4f} Ohm/K")
    print(f"  Exact: {result['Exact (Ohm/K)']:.4f} Ohm/K")
    print()