import numpy as np

def matrix_transpose(A):
    A = np.asarray(A, dtype=float)
    rows, cols = A.shape
    B = np.zeros((cols, rows))
    
    for i in range(rows):
        for j in range(cols):
            B[j, i] = A[i, j]
            
    return B