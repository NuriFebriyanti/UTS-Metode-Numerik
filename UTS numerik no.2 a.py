import numpy as np

def gauss_elimination(A, b):
    """
    Menyelesaikan sistem persamaan linear menggunakan metode eliminasi Gauss
    
    Parameters:
    A : array 2D numpy - Matriks koefisien
    b : array 1D numpy - Vektor hasil
    
    Returns:
    x : array 1D numpy - Solusi sistem persamaan
    """
    n = len(A)
    # Menggabungkan matriks A dan vektor b
    Ab = np.column_stack((A, b))
    
    # Forward elimination
    for i in range(n):
        # Mencari pivot
        pivot = Ab[i][i]
        
        # Membagi baris dengan pivot
        Ab[i] = Ab[i] / pivot
        
        # Eliminasi kolom di bawah pivot
        for j in range(i + 1, n):
            factor = Ab[j][i]
            Ab[j] = Ab[j] - factor * Ab[i]
    
    # Back substitution
    x = np.zeros(n)
    x[n-1] = Ab[n-1][n]
    
    for i in range(n-2, -1, -1):
        sum_ax = 0
        for j in range(i+1, n):
            sum_ax += Ab[i][j] * x[j]
        x[i] = Ab[i][n] - sum_ax
    
    return x

# Mendefinisikan matriks koefisien dan vektor hasil
A = np.array([[4, -1, -1],
              [-1, 3, -1],
              [-1, -1, 5]], dtype=float)

b = np.array([5, 3, 4], dtype=float)

# Menyelesaikan sistem persamaan
solution = gauss_elimination(A, b)

# Menampilkan hasil
print("Solusi sistem persamaan:")
print(f"I₁ = {solution[0]:.4f}")
print(f"I₂ = {solution[1]:.4f}")
print(f"I₃ = {solution[2]:.4f}")

# Verifikasi solusi
print("\nVerifikasi solusi:")
for i, eq in enumerate(A @ solution - b):
    print(f"Persamaan {i+1}: {abs(eq):.10f}")