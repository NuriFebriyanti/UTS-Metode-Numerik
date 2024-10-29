import numpy as np

# Konstanta
L = 0.5  # Induktansi dalam H
C = 10e-6  # Kapasitansi dalam F
pi = np.pi

# Fungsi untuk menghitung frekuensi resonansi f(R)
def f(R):
    return (1 / (2 * pi)) * np.sqrt((1 / (L * C)) - (R**2 / (4 * L**2)))

# Fungsi untuk menghitung turunan frekuensi resonansi f'(R)
def f_prime(R):
    # Menghitung f(R) untuk digunakan dalam turunan
    frequency = f(R)
    # Menghitung turunan menggunakan rumus turunan
    # f'(R) = - (1 / (2 * pi)) * (1 / sqrt((1 / (LC)) - (R^2 / (4L^2)))) * (-R / (2L^2))
    return - (1 / (2 * pi)) * (1 / np.sqrt((1 / (L * C)) - (R**2 / (4 * L**2)))) * (-R / (2 * L**2))

# Contoh penggunaan
R_value = 10  # Contoh nilai R dalam Ohm
frequency = f(R_value)
frequency_derivative = f_prime(R_value)

print(f"f(R) untuk R = {R_value} Ohm: {frequency:.4f} Hz")
print(f"f'(R) untuk R = {R_value} Ohm: {frequency_derivative:.4f} Hz/Ohm")