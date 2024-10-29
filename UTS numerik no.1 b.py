import numpy as np

# Konstanta
L = 0.5  # Induktansi dalam H
C = 10e-6  # Kapasitansi dalam F
target_frequency = 1000  # Target frekuensi dalam Hz
tolerance = 0.1  # Toleransi error dalam Ohm
interval = [0, 100]  # Interval awal

# Fungsi untuk menghitung frekuensi resonansi f(R)
def f(R):
    return (1 / (2 * np.pi)) * np.sqrt((1 / (L * C)) - (R**2 / (4 * L**2)))

# Fungsi untuk mencari akar menggunakan metode biseksi
def bisection_method(f, target, interval, tolerance):
    a, b = interval
    if f(a) > target or f(b) < target:
        print("Akar tidak terletak di interval yang diberikan.")
        return None

    while (b - a) / 2 > tolerance:
        midpoint = (a + b) / 2
        if f(midpoint) == target:
            return midpoint  # Jika kita menemukan akar persis
        elif f(midpoint) < target:
            a = midpoint  # Akar terletak di sebelah kanan
        else:
            b = midpoint  # Akar terletak di sebelah kiri

    return (a + b) / 2  # Mengembalikan nilai tengah sebagai akar

# Mencari nilai R yang menghasilkan frekuensi resonansi 1000 Hz
R_solution = bisection_method(f, target_frequency, interval, tolerance)

if R_solution is not None:
    print(f"Nilai R yang menghasilkan frekuensi resonansi {target_frequency} Hz: {R_solution:.4f} Ohm")