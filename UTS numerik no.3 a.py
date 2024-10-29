import numpy as np

def R(T):
    """Menghitung resistansi R berdasarkan temperatur T."""
    return 5000 * np.exp(3500 * (1/T - 1/298))

def forward_difference(f, T, h):
    """Menghitung turunan menggunakan metode selisih maju."""
    return (f(T + h) - f(T)) / h

def backward_difference(f, T, h):
    """Menghitung turunan menggunakan metode selisih mundur."""
    return (f(T) - f(T - h)) / h

def central_difference(f, T, h):
    """Menghitung turunan menggunakan metode selisih tengah."""
    return (f(T + h) - f(T - h)) / (2 * h)

# Definisikan temperatur
T = 300  # dalam Kelvin
h = 0.01  # Langkah kecil

# Hitung turunan dengan ketiga metode
dR_forward = forward_difference(R, T, h)
dR_backward = backward_difference(R, T, h)
dR_central = central_difference(R, T, h)

# Tampilkan hasil
print(f"Selisih Maju: dR/dT = {dR_forward:.4f} Ohm/K")
print(f"Selisih Mundur: dR/dT = {dR_backward:.4f} Ohm/K")
print(f"Selisih Tengah: dR/dT = {dR_central:.4f} Ohm/K")