import numpy as np

def gauss_elimination(A, b):
    n = len(b)
    # Gabungkan A dan b menjadi matriks augmented
    Ab = np.hstack([A, b.reshape(-1, 1)])
    
    # Eliminasi Gauss
    for i in range(n):
        # Mencari pivot
        max_row = np.argmax(np.abs(Ab[i:, i])) + i
        Ab[[i, max_row]] = Ab[[max_row, i]]  # Tukar baris
        
        # Membuat elemen di bawah pivot menjadi 0
        for j in range(i + 1, n):
            factor = Ab[j, i] / Ab[i, i]
            Ab[j] = Ab[j] - factor * Ab[i]
    
    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:n])) / Ab[i, i]
    
    return x

def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0, 0]
    if len(matrix) == 2:
        return matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]
    
    det = 0
    for c in range(len(matrix)):
        # Menghitung kofaktor
        minor = np.delete(np.delete(matrix, 0, axis=0), c, axis=1)
        det += ((-1) ** c) * matrix[0, c] * determinant(minor)
    
    return det

# Matriks koefisien
A = np.array([[4, -1, -1],
              [-1, 3, -1],
              [-1, -1, 5]])

# Vektor konstanta
b = np.array([5, 3, 4])

# Menghitung solusi dengan metode eliminasi Gauss
solution = gauss_elimination(A, b)
print("Solusi dari sistem persamaan adalah: I1 = {:.2f}, I2 = {:.2f}, I3 = {:.2f}".format(solution[0], solution[1], solution[2]))

# Menghitung determinan dari matriks koefisien
det_A = determinant(A)
print("Determinant dari matriks A adalah: {:.2f}".format(det_A))