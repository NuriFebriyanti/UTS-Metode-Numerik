import numpy as np

def determinant(matrix):
    """
    Menghitung determinan matriks menggunakan ekspansi kofaktor.
    
    Parameters:
    matrix : numpy array 2D - Matriks yang akan dihitung determinannya
    
    Returns:
    float - Nilai determinan matriks
    """
    # Kasus dasar: matriks 1x1
    if len(matrix) == 1:
        return matrix[0][0]
    
    # Kasus dasar: matriks 2x2
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for j in range(len(matrix)):
        # Membuat submatriks dengan menghapus baris pertama dan kolom j
        submatrix = np.delete(np.delete(matrix, 0, axis=0), j, axis=1)
        
        # Menghitung kofaktor
        cofactor = (-1) ** j * matrix[0][j] * determinant(submatrix)
        
        # Menambahkan ke total determinan
        det += cofactor
    
    return det

# Matriks koefisien dari sistem persamaan
A = np.array([[4, -1, -1],
              [-1, 3, -1],
              [-1, -1, 5]])

# Menghitung dan menampilkan determinan
det_A = determinant(A)
print(f"Determinan matriks A: {det_A}")

# Verifikasi dengan numpy
print(f"Verifikasi dengan numpy: {np.linalg.det(A)}")