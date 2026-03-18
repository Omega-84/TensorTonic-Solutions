import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    rows, cols = len(A), len(A[0])
    A_t = np.zeros([cols, rows])
    for r in range(rows):
        for c in range(cols):
            A_t[c][r] = A[r][c]
 
    return A_t