import numpy as np

def determinant(matrix):
    """Menghitung determinan matriks menggunakan ekspansi kofaktor."""
    if len(matrix) == 1:
        return matrix[0, 0]
    if len(matrix) == 2:
        return matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]

    det = 0
    for c in range(len(matrix)):
        minor = np.delete(np.delete(matrix, 0, axis=0), c, axis=1)
        det += ((-1) ** c) * matrix[0, c] * determinant(minor)

    return det

def adjoint(matrix):
    """Menghitung matriks adjoin (kofaktor transpos)."""
    n = matrix.shape[0]
    cofactors = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            # Minor untuk elemen (i, j)
            minor = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
            cofactors[i, j] = ((-1) ** (i + j)) * determinant(minor)
    
    return cofactors.T  # Transpose untuk mendapatkan adjoin

def inverse(matrix):
    """Menghitung invers matriks menggunakan metode adjoin."""
    det = determinant(matrix)
    if det == 0:
        raise ValueError("Matriks tidak memiliki invers (determinant = 0).")
    
    adj = adjoint(matrix)
    return adj / det  # Mengembalikan invers

# Contoh penggunaan
A = np.array([[4, -1, -1],
              [-1, 3, -1],
              [-1, -1, 5]])

try:
    inv_A = inverse(A)
    print("Invers dari matriks A adalah:")
    print(inv_A)
except ValueError as e:
    print(e)