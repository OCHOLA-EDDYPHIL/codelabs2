import numpy as np


def add_matrices(A, B):
    # Add two matrices A and B
    return A + B


def subtract_matrices(A, B):
    # Subtract matrix B from matrix A
    return A - B


def strassen(A, B):
    """
    Perform matrix multiplication using the Strassen algorithm.
    This function handles both the base case of 2x2 matrices and
    the recursive division for larger matrices.
    """
    # Base case: 2x2 matrix
    if A.shape[0] == 2:
        # Decompose matrices A and B into their components
        a, b, c, d = A[0, 0], A[0, 1], A[1, 0], A[1, 1]
        e, f, g, h = B[0, 0], B[0, 1], B[1, 0], B[1, 1]

        # Compute the 7 products needed for the Strassen algorithm
        M1 = (a + d) * (e + h)
        M2 = (c + d) * e
        M3 = a * (f - h)
        M4 = d * (g - e)
        M5 = (a + b) * h
        M6 = (c - a) * (e + f)
        M7 = (b - d) * (g + h)

        # Combine the products to get the final components of the result matrix
        C11 = M1 + M4 - M5 + M7
        C12 = M3 + M5
        C21 = M2 + M4
        C22 = M1 - M2 + M3 + M6

        # Construct and return the resulting 2x2 matrix
        C = np.array([[C11, C12], [C21, C22]])
        return C

    # Recursive case: divide the matrices into quadrants
    else:
        n = A.shape[0] // 2

        # Divide matrices A and B into quadrants
        A11 = A[:n, :n]
        A12 = A[:n, n:]
        A21 = A[n:, :n]
        A22 = A[n:, n:]
        B11 = B[:n, :n]
        B12 = B[:n, n:]
        B21 = B[n:, :n]
        B22 = B[n:, n:]

        # Recursively apply Strassen algorithm to smaller matrices
        M1 = strassen(add_matrices(A11, A22), add_matrices(B11, B22))
        M2 = strassen(add_matrices(A21, A22), B11)
        M3 = strassen(A11, subtract_matrices(B12, B22))
        M4 = strassen(A22, subtract_matrices(B21, B11))
        M5 = strassen(add_matrices(A11, A12), B22)
        M6 = strassen(subtract_matrices(A21, A11), add_matrices(B11, B12))
        M7 = strassen(subtract_matrices(A12, A22), add_matrices(B21, B22))

        # Combine the results into the final components of the result matrix
        C11 = M1 + M4 - M5 + M7
        C12 = M3 + M5
        C21 = M2 + M4
        C22 = M1 - M2 + M3 + M6

        # Combine the components into a single matrix
        top = np.hstack((C11, C12))
        bottom = np.hstack((C21, C22))
        C = np.vstack((top, bottom))

        return C


# Example usage
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

result = strassen(A, B)
print("Resulting matrix:")
print(result)
